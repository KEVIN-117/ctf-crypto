"""
Los sistemas criptográficos como RSA funcionan con números, pero los mensajes están compuestos de caracteres. ¿Cómo deberíamos convertir nuestros mensajes en números para poder aplicar operaciones matemáticas?

La forma más común es tomar los bytes ordinales del mensaje, convertirlos en hexadecimales y concatenarlos. Esto se puede interpretar como un número en base 16/hexadecimal y también se puede representar en base 10/decimal.


Para ilustrarlo:
    message: HELLO
    ascii bytes: [72, 69, 76, 76, 79]
    hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
    base-16: 0x48454c4c4f
    base-10: 310400273487

La biblioteca PyCryptodome de Python implementa esto con los métodos bytes_to_long() y long_to_bytes(). Primero deberá instalar PyCryptodome e importarlo con from Crypto.Util.number import *. Para obtener más detalles, consulte las preguntas frecuentes.

Convierte el siguiente entero nuevamente en un mensaje:
11515195063862318899931685488813747395775516287289682636499965282714637259206269
"""

from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(integer))