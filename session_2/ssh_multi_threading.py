from netmiko import ConnectHandler
from threading import Thread
from queue import Queue
import os
import time

class SSH:

    def __init__(self,device_list, username, password, max_threads):
        self.device_list = device_list
        self.username = username
        self.password = password
        self.max_threads = max_threads

    def write_output(self,output,device):
        device_name = device.replace(".","_")
        file_name = f"{device_name}_multi_threading.txt"
        with open(file_name,'a') as file_output:
            file_output.write(output)

    def send_commands(self,q):
        while not q.empty():
            device = q.get()
            device_parameters = {}
            device_parameters["device_type"] = "cisco_xr"
            device_parameters["ip"] = device
            device_parameters["username"] = self.username
            device_parameters["password"] = self.password
            with ConnectHandler(**device_parameters) as device_session:
                output = device_session.send_command("show clock")
                self.write_output(output, device)
            q.task_done()

    def create_workers(self,q):
        min_threads = min(self.max_threads,len(self.device_list))
        for thread_number in range(min_threads):
            thread_name = f'Thread-{thread_number}'
            worker = Thread(name=thread_name,target=self.send_commands, args=(q,))
            worker.start()
        q.join()

    def run(self):
        q = Queue(maxsize=0)
        for device in self.device_list:
            q.put(device)
        self.create_workers(q)

device_list = ["172.18.104.43","172.18.104.58","172.18.87.32","172.18.87.35","172.18.87.48","172.18.87.51"]
my_username = os.environ['CISCO_USERNAME']
my_password =  os.environ['CISCO_PASSWORD']
get_clock = SSH(device_list=device_list, username=my_username, password=my_password, max_threads=1)

start_time = time.time()
get_clock.run()
print("--- %s seconds ---" % (time.time() - start_time))
