import os


class ConversionOptions:
    HEX_TO_DEC = 0


def convert(option, value):
    if option == ConversionOptions.HEX_TO_DEC:
        return int(value, 16)


def compile():
    for file_name in os.listdir('contracts'):
        output_dir = f"artifacts/{file_name.split('.')[0]}"

        command = f'solc --overwrite -o {output_dir} --bin --abi contracts/{file_name}'

        os.system(command)