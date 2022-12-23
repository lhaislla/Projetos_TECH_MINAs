import functools
from colorama import init, Fore
init()

def color(color):
    def wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            print(color + 'Colorindo de Azul')
            func(*args, **kwargs)
        return runner
    return wrapper

@color(color=Fore.BLUE)
def greeter():
    print('Olá!!')
    print('Novamente')

greeter()