from threading import Thread, Event
import time

def message1(threads, event):
    event.wait()    # Espera a que se haya iniciado el hilo 5 (para esperar directamente al 4 se podria haber usado otro evento).
    threads[3].join() # Se bloquea hasta que termine el hilo 4.
    print(' are made of coffee?')

def message2():
    print('  Do you know',end="")

def message3(threads, event):
    event.wait()    # Espera a que se haya iniciado el hilo 5.
    threads[4].join() # Se bloquea hasta que termine el hilo 5.
    print(' it!')

def message4(threads):
    threads[1].join() # Se bloquea hasta que termine el hilo 2.
    print(' that our bodies',end="")

def message5(threads):
    threads[0].join() # Se bloquea hasta que termine el hilo 1.
    print('-Try drinking',end="")

def concurrency_with_coffe():
    print("- I'm tired, Bob!")
    event = Event() # Se usa para que los hilos 1 y 3 no puedan llamar a hilos aun no creados (4y5).
    threads = []
    threads.extend( [ Thread(target=message1, args=(threads,event)), Thread(target=message2), 
                Thread(target=message3, args=(threads,event)), Thread(target=message4, args=(threads,)), 
                Thread(target=message5, args=(threads,))
             ] )
    for thread in threads:
        thread.start()
    event.set() # Indica que ya estan iniciados todos los hilos.
    threads[2].join()
    print('- You’re right!')

if __name__ == "__main__":
    concurrency_with_coffe()
