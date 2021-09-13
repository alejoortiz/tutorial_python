class Router:

    # class attribute
    network = "claro"

    def __init__(self, hostname, interfaces, role, vendor, software):
        # instance attribute
        self.hostname = hostname
        self.interfaces = interfaces
        self.role = role
        self.vendor = vendor
        self.software = software

    def __str__(self):
        return f"""
        Hostname: {self.hostname}
        Interfaces: {self.interfaces}
        Vendor {self.vendor}
        Role {self.role}
        Software {self.software}
        """

    def upgrade(self, new_software):
        # instance method
        self.software = new_software
        

router_1 = Router("Router1", 10, "Core", "Cisco", "XR")
print(router_1)

router_2 = Router("Router2", 10, "Core", "Huawei", "HarmonyOS")
print(router_2)
