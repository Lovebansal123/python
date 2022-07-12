import random
randNumber = random.randint(1, 100)

userno = None
guesses = 0
while userno!=randNumber :
    userno = int(input("Enter a number from 1 to 100: "))
    guesses+=1
    if userno==randNumber:
        print("Congratulations! you won")
    elif userno>randNumber:
        print("Try Smaller Number")
    else:
        print("Try Greater Number")

print(f"You took {guesses} guesses to get correct number.")
with open("highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You made new Highscore")
    with open("highscore.txt","w") as f:
      f.write(str(guesses))
else:
    print(f"Least number of guesses are {highscore}")