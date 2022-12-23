from timeit import default_timer
import requests

def load_data(delay):
    print(f'Iniciando {delay} segundo temporizador')
    text = requests.get(f'http://httpbin.org/delay/{delay}').text
    print(f'Concluído {delay} segundo temporizador')

def run_demo():
    start_time = default_timer()

    two_data = load_data(2)
    three_data = load_data(3)

    elapsed_time = default_timer() - start_time
    print(f'A operação levou {elapsed_time:.2} segundos')

def main():
    run_demo()

main()
