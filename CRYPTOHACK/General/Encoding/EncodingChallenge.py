"""
Ahora que ya conoces las distintas codificaciones que encontrarás, veamos cómo automatizarlas.

¿Podrás pasar los 100 niveles para conseguir la bandera?

El archivo 13377.py adjunto a continuación es el código fuente de lo que se está ejecutando en el servidor. El archivo pwntools_example.py proporciona el inicio de una solución.

Para obtener más información sobre cómo conectarse a desafíos interactivos, consulte las preguntas frecuentes. ¡Si no está de humor para un desafío de codificación, puede saltar directamente a la criptografía!

Si desea ejecutar y probar el desafío localmente, consulte las preguntas frecuentes para descargar el módulo utils.listener.

Conéctese en socket.cryptohack.org 13377
"""
from Crypto.Util.number import long_to_bytes
from cffi.backend_ctypes import long
#!/usr/bin/env python3

from pwn import * # pip install pwntools
import base64
import json
import codecs

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decoder(encoded_type, encoded_flag):
    print(f"Decoding {encoded_type} with value {encoded_flag}")
    if encoded_type == "base64":
        return base64.b64decode(encoded_flag).decode()
    elif encoded_type == "hex":
        return bytes.fromhex(encoded_flag).decode()
    elif encoded_type == "rot13":
        return codecs.decode(encoded_flag, 'rot_13')
    elif encoded_type == "bigint":
        return long_to_bytes(int(encoded_flag, 16)).decode()
    elif encoded_type == "utf-8":
        return "".join([chr(x) for x in encoded_flag])
    else:
        raise ValueError(f"Unknown encoding type: {encoded_type}")


for _ in range(100):
    received = json_recv()
    print(f"Level {_ + 1}: {received}")
    encoded_type = received["type"]
    encoded_flag = received["encoded"]
    decoded_value = decoder(encoded_type, encoded_flag)
    print("Decoded value: ")
    print(decoded_value)

    to_send = {
        "decoded": decoded_value,
    }

    json_send(to_send)

final_response = json_recv()
print("Final response: ")
print(final_response)