import base64

"""
Otro esquema de codificación común es Base64, que nos permite representar datos binarios como una cadena ASCII utilizando un alfabeto de 64 caracteres. Un carácter de una cadena Base64 codifica 6 dígitos binarios (bits), y por lo tanto, 4 caracteres de Base64 codifican tres bytes de 8 bits. 
Base64 es el más utilizado en línea, por lo que los datos binarios, como las imágenes, se pueden incluir fácilmente en archivos HTML o CSS. 
Tome la siguiente cadena hexadecimal, descodifíquela en bytes y luego codifíquela en Base64.
cadena_hexadecimal = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
"""

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decoded_bytes = bytes.fromhex(hex_string)
print(decoded_bytes)
converted_base64 = base64.b64encode(decoded_bytes)
print(converted_base64)