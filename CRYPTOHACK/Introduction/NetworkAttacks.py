#!/usr/bin/env python3

"""
Varios de los desafíos son dinámicos y requieren que te comuniques con nuestros servidores de desafíos a través de la red. Esto te permite realizar ataques de intermediarios contra personas que intentan comunicarse o atacar directamente un servicio vulnerable. Para mantener la coherencia, nuestros servidores interactivos siempre envían y reciben objetos JSON.

Esta comunicación en red se puede realizar fácilmente en Python con el módulo pwntools. Este no forma parte de la biblioteca estándar de Python, por lo que debe instalarse con pip mediante la línea de comandos pip install pwntools.

Para este desafío, conéctese a socket.cryptohack.org en el puerto 11112. Envíe un objeto JSON con la clave de compra y el indicador de valor.

El siguiente script de ejemplo contiene el comienzo de una solución que puede modificar y reutilizar para desafíos posteriores.

Conéctese en socket.cryptohack.org 11112
"""

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)
