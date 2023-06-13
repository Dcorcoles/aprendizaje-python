import random

def adivinar(x):
    numero_aleatorio = random.randint(1, x)
    guess = 0
    while guess != numero_aleatorio:
        guess = int(input(f'Adivina un numero entre el 1 y el {x}: '))
        print(guess)
        if guess < numero_aleatorio:
            print('Lo siento, intentalo de nuevo. Demasiado bajo.')
        elif guess > numero_aleatorio:
            print('Lo siento, intentalo de nuevo. Demasiado alto.')
    print(f'Jaja, felicidades. Has acertado el numero aleatorio {numero_aleatorio} correctamente!!')
    
adivinar(10)