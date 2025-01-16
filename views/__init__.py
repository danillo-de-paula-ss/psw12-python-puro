from typing import Iterable
import sys, os

sys.path.append(os.path.abspath(os.curdir))

def input_ask(prompt: str, *, valid_answers: Iterable[str] = 'yn') -> str:
    assert len(valid_answers) > 0, "valid_answers should be more than 0"
    while True:
        response = input(prompt)
        if response in valid_answers and response != '':
            return response
        else:
            a = len(valid_answers) - 2
            b = len(valid_answers) - 1
            message = ''.join([f'"{v}", ' if a > k else f'"{v}" ou ' if b > k else f'"{v}"' for k, v in enumerate(valid_answers)])
            print(f'\033[31mResposta Incorreta! Responda somente {message}.\033[m')
