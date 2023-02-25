import importlib

# import module
import module_m # Singleton

# import module from package
from package import module

print('Este módulo se chama', __name__)

print('------ Import module -------')
print(module_m.variavel_module)

print('------ Import module from package -------')
print(module.soma_do_modulo(1, 2))


# Recarregar import 
print('------ Reload module -------')
for i in range(3):
	importlib.reload(module_m)
