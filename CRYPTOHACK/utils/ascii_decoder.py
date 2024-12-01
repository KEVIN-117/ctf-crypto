import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


def ascii_decoder(ords, type=""):
    """
    This function decodes the given list of integers to the given type
    :param ords: list of integers
    :param type: type of decoding
    :return: decoded string
    """
    if type == "ascii":
        """
        En Python, la función chr() se puede utilizar para convertir un número ordinal ASCII en un carácter (la función ord() hace lo contrario).
        """
        return "".join(chr(o) for o in ords)
    elif type == "binary":
        return "".join(format(o, "08b") for o in ords)
    elif type == "hex":
        return "".join(format(o, "02x") for o in ords)
    else:
        return "".join(chr(o ^ 0x32) for o in ords)