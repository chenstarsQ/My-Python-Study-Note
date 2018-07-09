number = 23
running = 1 #here 1 can be true

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations,you guessed it.')
        #this will make while order end
        running = 0 #here 0 can be false
    elif guess < number:
        print('No ,it is a little higher than that.')
    else:
        print('No,it is a little lower than that.')
else:
    print('The while loop is over.')
    #anythings you can do in here
print('Done')
