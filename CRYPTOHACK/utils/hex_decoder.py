def hex_decoder(hex_string: str):
    """
    This function decodes the given hex string
    :param hex_string: string of hex
    :return: string of decoded hex
    : helper: En Python, la función bytes.fromhex() se puede utilizar para convertir hexadecimales a bytes. El método de instancia .hex() se puede llamar en cadenas de bytes para obtener la representación hexadecimal.
    """
    return bytes.fromhex(hex_string)