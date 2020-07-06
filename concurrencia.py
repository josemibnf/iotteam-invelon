from threading import Thread

def message1():
    wait(4)
    print('“are made of coffee?')

def message2():
    print('Do you know')

def message3():
    wait(5)
    print('it!')

def message4():
    wait(2)
    print(' that our bodies')

def message5():
    wait(1)
    print('-Try drinking')

def concurrency_with_coffe():
    print("- I'm tired, Bob!")
    threads = [ Thread(target=message1()), Thread(target=message2()), 
                Thread(target=message3()), Thread(target=message4()), 
                Thread(target=message5())
             ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('- You’re right!')
