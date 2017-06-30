# Python:   2.7.13
#
# Author:   Chris Ling
#
# Program:  Grandma's Birthday Cash!
#
# Summary:  Grandma gives you a nice card and a dollar for every year in your age to spend at the store.
#           What are you going to buy, and what are you going to do with the change?


'''***UTILITY FUNCTIONS***'''

#Function that makes user press <Enter> before continuing the program, to give more time to read.
def progress():
    raw_input('\n[Press <Enter> to continue]')

#Function that provides mostly aesthetic spacing between different sections of the program.
def makespace():
    print('\n\n\n\n****************************')

#Function that provides awkward ellipses based on a timer.
#9. Use of a for loop.
def awkward():
    for x in range (0,3):
        print('...')
        sleep(1)

'''***PROGRAM FUNCTIONS***'''

#Function to start the program
def start(name='',age=0, generous='',cash=0.0, bag={}):

    game_intro()
    
    #Get user's name and age and stores in var name, age, generous
    name = get_name(name)
    age = get_age(age)
    generous = get_generous(generous)

    #Receiving birthday card and cash from grandma
    name,age,generous,cash,bag = get_cash(name,age,generous,cash,bag)


#Function for getting user name and age

def game_intro():
    print('\n*******Welcome to "Grandma\'s Birthday Cash"!*******')
    print('\nThis is a fun little text adventure where you get to relive the fond')
    print('memories of getting your annual birthday gift from your grandma, and,')
    print('of course, HOW you end up spending that gift!')
    progress()
        
    print('\nBefore we get started, we want to know more about you, the person of honor!')
    sleep(1)
    makespace()

    
def get_name(name):
    stop = True
    while stop:
        if name == '':
            #2. Assign a string to a variable.
            name = raw_input('\nTo get started, what is your first name? ').title()
            if name != '':
                #4. Using the print function and .format() notation to print out the variable you assigned.
                print('\nHappy Birthday {}! I hope it\'s been a great day so far!'.format(name))
                stop = False
    return name

def get_age(age):
    stop = True
    while stop:
        if age == 0:
            try:
                #1. Assign an integer to a variable.
                age = int(raw_input('\nNext, how old are you today? '))
                if age > 0:
                    print('\nReally? I would have never guessed you were {} years old!'.format(age))
                    stop = False
            except:
                print('\n*Please put in a whole number greater than 0!*')
    return age

def get_generous(generous):
    stop = True
    print('\nFinally, one last question... this might be a touchy subject, but just level with me here.')

    #8.Use of a while loop.
    while stop:
        if generous == '':
            generous = raw_input('\nWould you consider your grandma to be generous? [(v)ery, (s)ometimes, or (n)ever?] ').lower()
            #6. Use of logical operators; 7. Use of conditional statements.
            if generous == 'v' or generous =='s' or generous=='n':
                awkward()
                print('\nVery interesting. Well, thanks for being honest... I know it\'s awkward, but it\'s an important question for this program.')
                stop = False

            else:
                print('\n[Please only use the letters "v", "s", or "n"!]')
                generous=''
    return generous

#Function to get cash from birthday card

def get_cash(name,age,generous,cash,bag):
    print('\nWell, enough chit-chat! Let\'s get started with our story...')
    progress()
    makespace()
    
    print('\nIt\'s a beautiful morning! The powers that be must know that today is your birthday, and that of course means presents!')
    print('You rush outside and grab the mail from your mailbox, and see your annual card from crazy ol\' grandma!')
    progress()
    
    print('\nYou open it and take a look...')
    print('\n******************************')
    print('\n"Dear {},\n'.format(name))
    print('\nHappy birthday! I can\'t believe you\'re already {} years old! I remember when you were just a tiny little baby.'.format(age))

    #3. Assign a float to a variable; 5. Using the * operator
    if generous == 'v':
        print('I wanted to celebrate YOU this year by giving you $2 for every year in your wonderful life! I hope you get something fun and impractical!')
        cash = 2.0*age

    elif generous == 's':
        print('Inside this card, I\'ve given you $1 for every year you\'ve been alive.  Get yourself something nice and sensible.')
        cash = 1.0*age

    elif generous == 'n':
        print('I GUESS I have to give you something... fifty cents for each year of your life should be enough. Don\'t be wasteful and spend all of it at once!')
        cash = 0.5*age

    print('<3 Grandma\"')
    progress()
    
    print('\n[You received ${}0!]'.format(cash))
    progress()

    print('\nAfter doing some thinking, you decide that it would be a good idea to check out the Quikstop, the one-stop-shop for everything.')
    print('You\'ll hopefully find something to spend Grandma\'s cash on there. You grab your bag and put your cash in your pocket, then start heading to the Quikstop.')
    progress()

    spend_cash(name,age,generous,cash,bag)

def spend_cash(name,age,generous,cash,bag):
    makespace()
    print('\nAs you enter the Quikstop, your nose picks up a mixed fragrance of buttered popcorn, burnt sugar, and stale farts.')
    print('Not really a confidence-builder in terms of the quality of its wares, but beggars can\'t be choosers.')
    progress()

    print('\nYou walk up to the counter. The lone store clerk seems completely uninterested in being friendly or helpful to the customers.')
    print('You also see a sign that says, "We Don\'t Provide Full Refunds, So Don\'t Even Ask For One." Classy.')
    progress()

    store_clerk(name,age,generous,cash,bag)

def store_clerk(name,age,generous,cash,bag):
    inventory = {1:['adult magazine', 6.0], 2:['6-pack beer',9.0], 3:['candy bar',1.0], 4:['pack of cigarettes',8.0], 5:['kung fu video',11.0], 6:['hot dog',2.0], 7:['soda',1.0]}
    
    stop=True
    while stop:
        print('\nThe clerk looks at you with a glazed look and asks in a slurred voice, "What do you want, brah?"')
        current_action = raw_input('[(b)uy item, (r)eturn Item, (c)heck bag, or (l)eave]: '.lower())

        if current_action == 'b':
            name,age,generous,cash,bag = buy_item(name,age,generous,cash,bag,inventory)

        elif current_action == 'r':
            name,age,generous,cash,bag = return_item(name,age,generous,cash,bag,inventory)

        elif current_action == 'c':
            name,age,generous,cash,bag = check_bag(name,age,generous,cash,bag,inventory)

        elif current_action == 'l':
            print('\nOkay, whatever.  Have like a good day, brah.')
            stop=False
            get_big_bills(name,age,generous,cash,bag,inventory)

        else:
            print('\n[Please only use the letters "b", "r", "c", or "l"!]\n')

def buy_item(name,age,generous,cash,bag,inventory):
    print('\n"Here\'s what I got in stock, brah:"\n')
    stop=True

 #10-11.  I did not end up using a tuple because it didn't make sense to do it within my program, but I used a dictionary to iterate, which I think incorporates many similar concepts to lists and tuples.
    while stop:
        #5. Using the = operator
        x=1
        while x <= len(inventory):
            current_item = inventory[x]
            print(str(x)+': '+current_item[0]+': $'+str(current_item[1])+'0').title()
            #5. Using the += operator
            x += 1

        print('\nCurrent Cash: $'+str(cash)+'0')
        selection = raw_input('\nWhat do you want to buy? [Enter item (#) or (n)ever mind]: ')
        if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == '5' or selection == '6' or selection == '7':

            purchase = inventory[int(selection)]
            if purchase[1] <= cash:
                cash = cash-purchase[1]
                
                try:
                    bag[purchase[0].title()] += 1
                except:
                    bag[purchase[0].title()] = 1
                    
                print('\n[You bought a(n) {}! You have ${}0 of cash left.]'.format(purchase[0].title(), cash))
                print('\nYour bag now has the following items:')
                print bag
                
            else:
                print('\n"You don\'t have enough money to spend on this! Buy something else or leave!"')

        elif selection == 'n':
            print('\n"Hey, if you\'re not going to buy anything, don\'t waste my time, brah!"')
            stop=False
            store_clerk(name,age,generous,cash,bag)

        else:
            print('\n[Please only use the numbers 1 through 7 or "n"!]\n')
            

def return_item(name,age,generous,cash,bag,inventory):
    print('\n"What do you want to return, brah? We only give a 50% return on merch, FYI."\n')
    stop=True

    while stop:           
        x=1
        while x <= len(inventory):
            current_item = inventory[x]
            item_name = current_item[0].title()

            try:
                print(str(x)+': '+item_name+' (In Bag: '+str(bag[item_name])+'): $'+str((current_item[1]/2))+'0').title()
                x += 1
                
            except:
                print(str(x)+': '+item_name+' (In Bag: '+str(0)+'): $'+str((current_item[1]/2))+'0').title()
                x += 1

        print('\nCurrent Cash: $'+str(cash)+'0')
        print bag
        
        selection = raw_input('\nWhat do you want to return? [Enter item (#) or (n)ever mind]: ')
        if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == '5' or selection == '6' or selection == '7':

            purchase = inventory[int(selection)]
            purchase_name = purchase[0].title()
            if bag[purchase_name] > 0:
                #5. Using the + operator.
                cash = cash+(purchase[1]/2)
                bag[purchase_name] -= 1
                print('\n[You returned a(n) {}! You have ${}0 of cash left.]'.format(purchase_name, cash))
                print('\nYour bag now has the following items:')
                print bag
                
            else:
                print('\n"You don\'t have a(n) {} to return! Return something else or leave!"'.format(purchase_name))

        elif selection == 'n':
            print('\n"Hey, if you\'re not going to return anything, don\'t waste my time, brah!"')
            stop=False
            store_clerk(name,age,generous,cash,bag)

        else:
            print('\n[Please only use the numbers 1 through 7 or "n"!]\n')

#12-13.  This function calls both a string variable (cash) + a dictionary, which is used within the program.
def check_bag(name,age,generous,cash,bag,inventory):
    print('\nYour bag has the following items:')
    print bag
    print('\nCurrent Cash: $'+str(cash)+'0')
    progress()
    store_clerk(name,age,generous,cash,bag)

def get_big_bills(name,age,generous,cash,bag,inventory):
    makespace()
    print('\nAs you turn to leave, you realize that you should see if you can get some larger bills.')
    print('Grandma gave you your gift in $1 bills. You don\'t want to look shady with a fat wad of cash.')
    print('You ask the clerk, "Hey buddy, do you think you could change me up to some fivers?" and hand him your mega load.')
    progress()

    if cash > 5:
        #5. Using the % operator.
        change = str(cash % 5)
        five_dollar = int(cash/5)

        print('\nWith a very audible and painful-sounding groan, the clerk counts up your cash.')
        print('He hands you back a smaller stack of bills and says, "Here\'s {} five(s), and ${}0 in change."'.format(str(five_dollar), change))
        
    else:
        print('\nThe clerk looks at you like you\'re the biggest moron on the planet. "Learn to count, brah.  You don\'t even have five dollars."')

    print('\n"Now, get the hell out of here, man.  You\'re harshing my vibe, totally."')
    progress()
    print('\nYou hurry on your way home, feeling for the most part that Grandma\'s birthday gift was well spent.  You can\'t wait until next year!\n')
    print('**********THE END**********')


    play_again(name,age,generous,cash,bag,inventory)

def play_again(name,age,generous,cash,bag,inventory):
    stop=True
    print('\nAt the end of the game, your bag has the following items:\n')
    print bag
    print('\nFinal Cash: $'+str(cash)+'0')
    progress()

    while stop:
        again = raw_input('Do you want to play again? [y/n] ')
        if again == 'y':
            print('Great!  Let\'s reset the game!')
            progress()
            cash=0.0
            bag={}
            stop=False
            get_cash(name,age,generous,cash,bag)

        elif again == 'n':
            print('Okie-doke!  Thanks for a great game! See you next time!')
            stop=False
            exit()
            
        else:
            print('\n[Please only use the letters "y" or "n"!]')

    



''' RUN PROGRAM '''

if __name__ == "__main__":
    from time import sleep
    start()
