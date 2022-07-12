import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's' and you=='r':
            return True
    elif comp == 'r' and you=='p':
            return True
    elif comp == 'p'and you=='s':
            return True
    else:
        return False


while(1):
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 'r'

    you = input("Your Turn: Scissor(s) Paper(p) or Rock(r)?\n")

    a = gameWin(comp, you)

    print(f"Computer chose {comp}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
    e = input("Do you want to exit? Yes(y) or No(n)")
    if e=='y':
        exit()

