#Made by Kevin Perez
import random

rand = random.randint(1,100) 

while True: #Will loop through.
    num = input('Guess the number from 1 to 100:')
    dig = num.isdigit() #the function .isdigit() tells whether the input is a valid digit or not. Will output True or False
    
    if dig == True: 
        num = int(num) #turns the input from a string to a number after it passes whether is a real digit

        if num != rand: #if the number is not equal to the random number
            
            if num < rand:
                print('The number you chose is too low')
                continue
            
            else:
                print('The number you chose is too big')
                continue
        
        else:
            print('You guessed the correct number')
            break
    
    else: # it will loop since the variable dig is False
        print('Enter a digit')


