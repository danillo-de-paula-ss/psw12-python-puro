import sys, os
from datetime import datetime

sys.path.append(os.path.abspath(os.curdir))

def input_datetime(prompt: str, *, format_: str, return_str: bool = False) -> str | datetime:
    while True:
        response = input(prompt)
        try:
            response_d = datetime.strptime(response, format_)
            if return_str:
                return response
            return response_d
        except ValueError:
            print(f'\033[31mFormato incorreto! Responda de acordo com o formato {format_}\033[m')

def input_float(prompt: str) -> str:
    while True:
        response = input(prompt)
        try:
            float(response)
            return response
        except ValueError:
            print('\033[31mValor incorreto! Digite somente números inteiros ou decimais\033[m')
