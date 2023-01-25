class ConversionOptions:
    HEX_TO_DEC = 0

def convert(option, value):
    if option == ConversionOptions.HEX_TO_DEC:
        return int(value, 16)