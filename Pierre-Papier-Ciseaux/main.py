import random 
Cheat = True

def play():
    computer = random.choice(['p', 'f', 'c'])

    if Cheat:
        print(computer) 
    user = input("(p) pour la pierre, (f) pour feuille, (c) pour ciseaux : ")

    if user == computer:
        return 'Même choix'

    if is_win(user, computer):
        return 'Vous avez gagné'

    return 'Vous avez perdu'
    
    # r > s, s > p, p > r 

def is_win(player, opponent):
    if (player == 'p' and opponent == 'c') or (player == 'c' and opponent == 'f') \
        or (player == 'f' and opponent == 'p'):
        return True

print(play())
