import random
number=random.randint(0,11)
chances=0
print("Guess a Number Between 0 and 11")
while chances<5:
    #enter a number between 0 and 11
    guess=int(input("Enter your Guess:- "))
    #compare the user entered number with the number to be guessed
    if guess==number:
        #if number entered by the user is same as the generated
        #number by randint function then break from the loop using loop control statement"break"
        print("Congratulations You Won")
        break
    #check if the user entered number is smaller than the generated number
    elif guess<number:
        print("Your Guess Was Too Low Guess A Number Higher Than",guess)
    elif guess>number:
        print("Your Guess Was Too High Guess A Number Lower Than",guess)
    #increase the value of chances by 1
    chances+=1
#check whether the user guessed the correct number
if not chances<5:
    print("You Lose The Correct Number Is ",number)
