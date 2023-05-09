import random
cheat = False

def guess(x):
    random_number = random.randint(1, x)
    if cheat: 
        print(random_number)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Deviner le nombre entre 1 et {x} ! : "))
        if guess < random_number: 
            print("Désoler, essaye encore. Plus haut")
        elif guess > random_number:
            print("Désoler, essaye encore. Plus bas")
    print("Bravo vous avez trouvé le nombre juste !")

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''

    while feedback != 'C':
        if low != high: 
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Mon nombre est : {guess}, Ecrit (L) pour Plus Bas ,(H) pour Plus Haut , si l\'ordinateur à trouvé votre nombre (C) ! : ')
        if feedback == 'L':
            high = guess - 1
        elif feedback == 'H':
            low = guess + 1
    print(f"L'ordinateur à trouvé votre nombre, C'était : {guess}")

computer_guess(10)
