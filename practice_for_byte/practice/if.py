number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # new block begin
    print('Congratulations,you guessed it.')
    print('(but you do not win any prizes!)')
    if guess == 23:
        print('you are idiot')
    # new block end
elif guess < number:
    # another code block
    print('No,it is a little higher than that')
    # anythings you want to do in here
else:
    print('No, it is a little lower than that')
    # you must guess a bigger than number to goto there

print('Done')
# this is end code
# if order has be done
