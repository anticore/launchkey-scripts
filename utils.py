import os
import importlib


def load_programs(program_dir):
    programs = []

    for filename in os.listdir(program_dir):
        if filename.endswith(".py"):
            program_name = filename[:-3]
            module = importlib.import_module(f'{program_dir}.{program_name}')
            programs.append(getattr(module, program_name))

    return programs
