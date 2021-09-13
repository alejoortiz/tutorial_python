### variable type dictionary ###

mi_carro = {
  "marca": "Ferrary",
  "modelo": "Roma",
  "año": 2020
}

print(type(mi_carro))
print(mi_carro['marca'])

mi_carro['color'] = 'negro'
print(mi_carro)

mi_carro['modelo'] = 'Portofino'
mi_carro['color'] = 'rojo'
print(mi_carro)


collection_ferrari = {
  "marca": "Ferrary",
  "modelo": ["Roma", "Portofino", "F8spider", "F8tributo", "SF90stradale", "812superfast"],
  "año": [2020, 2021],
}
