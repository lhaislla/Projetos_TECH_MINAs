from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Iniciando{delay} segundo timporizador')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Concluido {delay} segundo timporizador')
        return text

async def main():
     # Inicia o cronômetro
    start_time = default_timer()

    # Simular outro processamento
    async with aiohttp.ClientSession() as session:
        # Vamos pegar nossos valores
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

         # Imprima nossos resultados
        await asyncio.sleep(1)
        print('Fazendo outro trabalho')

        # Let's go get our values
        two_result = await two_task
        three_result = await three_task

        # Print our results
        elapsed_time = default_timer() - start_time
        print(f'A operação levou {elapsed_time:.2} segundos' )

asyncio.run(main())
