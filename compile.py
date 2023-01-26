import os

"""
Compile Output Options
--ast-compact-json   AST of all source files in a compact JSON format.
--asm                EVM assembly of the contracts.
--asm-json           EVM assembly of the contracts in JSON format.
--opcodes            Opcodes of the contracts.
--bin                Binary of the contracts in hex.
--bin-runtime        Binary of the runtime part of the contracts in hex.
--abi                ABI specification of the contracts.
--ir                 Intermediate Representation (IR) of all contracts.
--ir-optimized       Optimized intermediate Representation (IR) of all contracts.
--ewasm              Ewasm text representation of all contracts (EXPERIMENTAL).
--ewasm-ir           Intermediate representation (IR) converted to a form that can be translated directly into Ewasm text representation (EXPERIMENTAL).
--hashes             Function signature hashes of the contracts.
--userdoc            Natspec user documentation of all contracts.
--devdoc             Natspec developer documentation of all contracts.
--metadata           Combined Metadata JSON whose IPFS hash is stored on-chain.
--storage-layout     Slots, offsets and types of the contract's state variables.
"""
def compile(contract_dir='contracts'):
    for file_name in os.listdir(contract_dir):
        output_dir = f"artifacts/{file_name.split('.')[0]}"

        command = f'solc --overwrite -o {output_dir} --abi --bin contracts/{file_name}'

        os.system(command)


if __name__ == '__main__':
    compile()

# --bin
# --bin-runtime
# --abi