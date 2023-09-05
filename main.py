import  random 

def guess(x) : 
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess A number between 1 and {x}: "))
        if guess < random_number:
            print("sorry guess again too low")
        elif guess > random_number:
            print("Sorry Guess to high try again ")
        else:
            print("yay congrats you got it right ")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is guess to hight {guess} (H), too low (L) or correct (C)??").lower

guess(10)