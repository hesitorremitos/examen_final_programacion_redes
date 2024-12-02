# Fill in this file with the code from parsing JSON exercise
import json

with open("usuarios.json", "r") as json_file:
    ourjson = json.load(json_file)

print(ourjson)

# IMpresion de usuarios formateado
for user in ourjson:
    print(f"nombre: {user['nombre']}; edad: {user['edad']}")
