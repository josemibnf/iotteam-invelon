from threading import Thread
import time

def message1(threads):
    time.sleep(1)
    threads[3].join() # Se bloquea hasta que termine el hilo 4.
    print('“are made of coffee?')

def message2():
    print('Do you know')

def message3(threads):
    time.sleep(1)
    threads[4].join() # Se bloquea hasta que termine el hilo 5.
    print('it!')

def message4(threads):
    threads[1].join() # Se bloquea hasta que termine el hilo 2.
    print(' that our bodies')

def message5(threads):
    threads[0].join() # Se bloquea hasta que termine el hilo 1.
    print('-Try drinking')

def concurrency_with_coffe():
    print("- I'm tired, Bob!")
    threads = []
    threads.extend( [ Thread(target=message1, args=(threads,)), Thread(target=message2), 
                Thread(target=message3, args=(threads,)), Thread(target=message4, args=(threads,)), 
                Thread(target=message5, args=(threads,))
             ] )
    for thread in threads:
        thread.start()
    threads[2].join()
    print('- You’re right!')

if __name__ == "__main__":
    concurrency_with_coffe()
