# TODO: remake compilation script
import os
import sys


def compile():
    for file_name in os.listdir('contracts'):
        output_dir = f"artifacts/{file_name.split('.')[0]}"

        command = f'solc -o {output_dir} --bin --ast-compact-json --asm contracts/{file_name}'

        os.system(command)

compile()