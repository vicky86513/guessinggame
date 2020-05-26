import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval +(highval -lowval) //2
        #if guess is in the middle ,it is found !
        if guess == randnum:
            return count

        #if "guess" is greater than the number.
        #if must be found in the lower hlaf of the  set of numbers
        #between the lowetr value and the guess
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
        #the number must be in the upper set of numbers
        #between the guess and the upper value
        else:
            count = count + 1
            return computerGuess(guess-1 , highval, randnum, count)

    else:
        #number not found
        return -1
    #end of function

#generate a ramdon number between 1 to 100
randnum = random.randint(1,101)
count = 0
guess = -99

while (guess != random):
    #get the user's guess
    guess= (int) (input("Enter your guess betwenn 1 and 100 :"))
    if guess < randnum :
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("you guessed it !")
        break
    count =count + 1
    #end of while loop

print("You tool " + str(count) + "step to guess the number")
print("computer took " + str (computerGuess(1,100,randnum)) + " steps!")
