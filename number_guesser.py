import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleas type a number larger than 0 nex time .")
        quit()
else:
    print("Pleas type a number larger than 0 nex time .")
    quit()

rendom_number = random.randint(0,top_of_range)
print (rendom_number)

guesses = 0 

while True:
    guesses+=1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("pleas type a number next time . ")
        continue

    if user_guess == rendom_number:
        print("you got it !")
        break
    elif user_guess > rendom_number:
        print("you where above the number ")
    else:
         print("you where below the number ")
print("you got !" ,guesses, " guesses")



