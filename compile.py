import os


if __name__ == '__main__':
    for file_name in os.listdir('contracts'):
        output_dir = f"artifacts/{file_name.split('.')[0]}"

        command = f'solc --overwrite -o {output_dir} --asm-json contracts/{file_name}'

        os.system(command)