### Author: RobDaSheep
### Date: 06/04/2020
### Text based game: Tulip Project


import time

decisions=['a', 'b']

print("--------TULIP PROJECT--------")
time.sleep(1)
print("-Initiating project-")
time.sleep(1)
print("-Loading server data-")
time.sleep(1)
print("-Creating avatar-")
time.sleep(1)
print("-Would you like to join Tulip Project?- ")
def start_game():
    """Decision to start the game, if player says no it quits"""
    print('YES OR NO')
    start_yes_no = ['yes', 'no']
    start = getstart(start_yes_no)
    if start == 'yes':
        getname()
    elif start == 'no':
        print('-Denying access-')
        time.sleep(1)
        quit()

def getstart(start_yes_no):
    """Checks if the player is answering to the question right and takes the decision"""
    start = input()
    if start in start_yes_no:
        return start
    else:
        print('-Please enter a valid option-')
        return getstart(start_yes_no)

def getname():
    """"Function to get name of the player"""
    print('-What is your name?-')
    name = input()
    print('\n-Welcome ' + name + ', to Tulip Project-')
    time.sleep(1)
    introduction()

def introduction():
    """This is the introduction to what tulip project is"""
    print("\nHey welcome to tulip project")
    time.sleep(2)
    print("this is a world where you can start from zero")
    time.sleep(2)
    print("here you will live and work for the queen Tulip")
    time.sleep(2)
    print("The mission to all players is to protect the realm")
    time.sleep(2)
    print("Now tell me which class fits you the most")
    time.sleep(1)
    print('\n-Assassin')
    print('-Mage')
    print('-Great Shielder')
    print('-Paladin')
    print('-Adventurer')
    print('-Ranger')
    print('-Berzerker')
    class_choosing()

def class_choosing():
    """Here the player chooses a class for the character"""
    classes = ['assassin', 'mage', 'great shielder', 'paladin', 'adventurer', 'ranger', 'berzerker']
    class_ = class_chosen(classes)
    if class_ == 'assassin' or 'mage' or 'great shielder' or 'paladin' or 'adventurer' or 'ranger' or 'berzerker':
        des1()

def des1():
    time.sleep(1)
    print('\nPerfect here’s your starter gear')
    time.sleep(1.5)
    print('From now on you will be working for the realm')
    time.sleep(2)
    print('I will be your quest master')
    time.sleep(1.5)
    print('As your first quest you need to get a tulip')
    time.sleep(1)
    print('\n1) Perfect I will go look for one')
    print('2) Huh a tulip?')
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        attmp_dissconection()
    elif des == '2':
        des1_2()

def des1_2():
    print("Yes a Tulip.")
    time.sleep(1)
    print("It is the flower of the queen as it is her name")
    time.sleep(2)
    print("It is only a formality")
    time.sleep(1)
    print("\n1) Okay, I guess I will look for one")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        attmp_dissconection()

def attmp_dissconection():
    """Change from player to AI (the character the player uses during the game to take decisions"""
    time.sleep(.5)
    print('\n-Attempting disconnection-')
    time.sleep(.5)
    print('-Attempting disconnection-')
    time.sleep(.5)
    print('-Attempting disconnection-')
    time.sleep(.5)
    print('-Attempting disconnection-')
    time.sleep(.5)
    print('-Attempting disconnection-')
    time.sleep(.5)
    print('-Attempting disconnection-')
    time.sleep(1)
    print("\nWhat's going on I didn't try to disconnect")
    time.sleep(1.5)
    print("\n1) Hey I am your personal assistant, I'm an IA, my name is Holly")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        des2()

## Next decisions are for going to a short story or a longer story, it asks more than one time if you want to ignore the investigation path

def des2():
    time.sleep(1)
    print("\nHey Holly, Why am I trying to disconnect?")
    time.sleep(1)
    print("\n1) It looks like someone is trying to disconect you for some reason")
    print("2) It appears to be an error, ignore it and keep going")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des2_1()
    elif des == '2':
        des_ignore()

def des2_1():
    time.sleep(1)
    print('\nWhat should I do?')
    print('\n1) I will run a test, please wait a minute')
    print("2) Just ignore it, maybe it's just an error")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des2_1_1()
    elif des == '2':
        des_ignore()

def des2_1_1():
    time.sleep(1)
    print('\nI will wait')
    time.sleep(.5)
    print('.....')
    time.sleep(.5)
    print('.....')
    time.sleep(.5)
    print("\n1) I don't think this is an error, we should try to investigate")
    print("2) It looks like it was an error, just ignore it")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des2_1_1_1()
    elif des == '2':
        des_ignore()

def des2_1_1_1():
    time.sleep(1)
    print("\nI guess we should, where should we start?")
    time.sleep(2)
    print("\n1) For now we should complete the first quest")
    print("2) Let's ignore it for now")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        desQM()
    elif des == '2':
        des_ignore()

def desQM():
    time.sleep(1)
    print("\nIt sounds good, I will look for the tulip and hand it to the quest master")
    time.sleep(2)
    print("\n1) Okay I will show up after that")
    print("2) Do what you want")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        desTulip_look()
    elif des == '2':
        des_rude1()

def des_rude1():
    time.sleep(1)
    print("\nHuh?, Don't be that rude")
    desTulip_look()

def desTulip_look():
    time.sleep(1)
    print("\n.....")
    time.sleep(.5)
    print("Hey, I'm back now what?")
    time.sleep(1)
    print("\n1) Hey back, I am holly, do whatever you want")
    print("2) You are free now perhaps a bit of grinding")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des_rude2()
    elif des == '2':
        des_grind()

def des_rude2():
    time.sleep(.5)
    print("\nWhy are you answering like this?")
    time.sleep(1)
    print("\n1) Never mind, we should just grind a bit")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        des_grind()

def des_grind():
    time.sleep(1)
    print("\nSounds good I guess")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print("I feel prepared now, I have new gear")
    time.sleep(1)
    print("Can we investigate now?")
    time.sleep(1)
    print("\n1) I guess we can, where would you like to start?")
    print("2) We should.")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        desbar_inn()
    elif des == '2':
        desbar_inn()

## Investigation path of the game

def desbar_inn():
    time.sleep(1)
    print("\nMaybe at a bar or an inn?")
    time.sleep(1)
    print("\n1) I guess a bar")
    print("2) An inn sounds good")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des_bar()
    elif des == '2':
        des_inn()

def des_bar():
    time.sleep(1)
    print("\nPerfect I will tell you what I found at the bar")
    des_inv()

def des_inn():
    time.sleep(1)
    print("\nPerfect I will tell you what I found at the inn")
    des_inv()

def des_inv():
    time.sleep(1)
    print("\n.....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(1)
    print("It seems that some players disconnect people that they feel are dangerous")
    time.sleep(1)
    print("\n1) That's odd you were just a new player")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        des_inv2()

def des_inv2():
    time.sleep(1)
    print("\nYeah I know, maybe it was a mistake")
    time.sleep(1)
    print("\n1) I don't think that was a mistake")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        des_inv3()

def des_inv3():
    time.sleep(1)
    print("\nHow?")
    time.sleep(1)
    print("\n1) Just saying, it's too weird")
    print("2) We should forget about it")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des_inv4()
    elif des == '2':
        des_attk()

def des_inv4():
    time.sleep(1)
    print("\nWell I talked to a guy and he told me that, he gave me a potion too")
    time.sleep(1)
    print("\n1) Don't drink it!")
    print("2) Drink it.")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des_dont_drink()
    elif des == '2':
        des_drink()

def des_dont_drink():
    time.sleep(1)
    print("\nWhy? I don't think anything bad could happen")
    des_drink()

def des_drink():
    time.sleep(1)
    print("\n.....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print("I’m starting to feel dizzy, I think I am going to pass out")
    time.sleep(1)
    print("\n-STATUS: SLEEP  30:00 min-")
    des_connect()

def des_ignore():
    time.sleep(1)
    print("\n.....")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("I completed the first quest, what now?")
    time.sleep(1)
    print("\n1) For now you are free, you should grind a bit.")
    print("2) Grinding would be the best, you need new gear")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1' or '2':
        des_grind2()

def des_grind2():
    time.sleep(1)
    print("\nI got better gear now")
    time.sleep(1)
    print("\n1) Let's head back to the capital")
    print("2) Go to the quest master")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1':
        des_grind3()
    elif des == '2':
        des_grind3()

def des_grind3():
    time.sleep(1)
    print("\nI will be on my way")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    des_attk()

def des_attk():
    time.sleep(1)
    print("\nI think I'm being followed")
    time.sleep(1)
    print("-STATUS: FROZEN-")
    time.sleep(1)
    print("What is this? I can't move")
    time.sleep(1)
    print("-STATUS: SLEEP-")
    des_connect()

## Conection of the history, both paths take to this part

def des_connect():
    time.sleep(1)
    print("\n1) Hey")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        time.sleep(.5)
        print("\n1) Hey")
        des_list = ['1']
        des = getdes(des_list)
        if des == '1':
            time.sleep(.5)
            print("\n1) Hey")
            des_list = ['1']
            des = getdes(des_list)
            if des == '1':
                time.sleep(.5)
                print("\n1) Wake up")
                des_list = ['1']
                des = getdes(des_list)
                if des == '1':
                    wakes_up()

def wakes_up():
    time.sleep(1)
    print("\nHuh? What happened?")
    time.sleep(1)
    print("\n1) You fell asleep")
    des_list = ['1']
    des = getdes(des_list)
    if des == '1':
        time.sleep(1)
        print("\nIt looks like I'm on a kind of abandoned house")
        time.sleep(2)
        print("\n1) Can you see anyone?")
        print("2) Do you se anything?")
        des_list = ['1', '2']
        des = getdes(des_list)
        if des == '1' or '2':
            time.sleep(1)
            print("\nI see a silhouette but I cant move")
            time.sleep(1)
            print("I will try to get their attention")
            time.sleep(1)
            print("\n1) Sounds good, at least we will know something")
            print("2) NO!!!!")
            des_list = ['1', '2']
            des = getdes(des_list)
            if des == '1' or '2':
                time.sleep(1)
                print("Hmmm, doesn't seem like they care")
                time.sleep(1)
                print("\n1) Can you try to get out?")
                print("2) Try to free yourself")
                des_list = ['1', '2']
                des = getdes(des_list)
                if des == '1' or '2':
                    time.sleep(1)
                    print("\nI managed to free myself but It looks like they noticed, he looks mad!")
                    time.sleep(1)
                    print("\n1) Stay and fight")
                    print("2) Run")
                    des_list = ['1', '2']
                    des = getdes(des_list)
                    if des == '1':
                        time.sleep(1)
                        print("\nI will try")
                    elif des == '2':
                        time.sleep(1)
                        print("\nThere's no place to run, I will try to fight")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print("I don't think I’m going to make it, he says I must be eliminated of the game")
                    time.sleep(2)
                    print("He says his boss thinks I’m dangerous")
                    time.sleep(1)
                    print("This makes more sense")
                    time.sleep(1)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print("He says they need to kill the queen, that she has a soul")
                    time.sleep(2)
                    print("I see the door")
                    time.sleep(1)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print("Oh no there's more people")
                    time.sleep(1)
                    print("-STATUS: Health boosted")
                    time.sleep(.5)
                    print("-STATUS: Speed boosted")
                    time.sleep(.5)
                    print("-STATUS: Jump boosted")
                    time.sleep(1)
                    print("It looks like something helped me escape, do you know what?")
                    time.sleep(2)
                    print("\n1) It was the queen")
                    print("2) It looks like it was someone")
                    des_list = ['1', '2']
                    des = getdes(des_list)
                    if des == '1':
                        time.sleep(1)
                        print("\nIt can't be, maybe she knows something")
                    elif des == '2':
                        time.sleep(1)
                        print("\nWho?")
                        time.sleep(.5)
                        print("\n1) Tulip")
                        des_list = ['1']
                        des = getdes(des_list)
                        if des == '1':
                            time.sleep(.5)
                            print("\nThe queen?")
                            time.sleep(.5)
                            print("\n1) Yes")
                            des_list = ['1']
                            des = getdes(des_list)
                            if des == '1':
                                print("\nIt can't be, maybe she knows something")
                    time.sleep(1)
                    print(".....")
                    time.sleep(.5)
                    print("\nDo you think she is a person trapped?")
                    time.sleep(1)
                    print("\n1) She might be, we should help her")
                    print("2) Maybe she is just an IA like me")
                    des_list = ['1', '2']
                    des = getdes(des_list)
                    if des == '1' or '2':
                        time.sleep(1)
                        print("\nI want to help her, I will go to the castle")
                        time.sleep(1)
                        print(".....")
                        time.sleep(.5)
                        print(".....")
                        time.sleep(.5)
                        print("The guards won't let me in")
                        time.sleep(1)
                        print("\n1) Run through them")
                        print("2) Look for another entrance")
                        des_list = ['1', '2']
                        des = getdes(des_list)
                        if des == '1':
                            final_1()
                        elif des == '2':
                            final_2()
                        # This decision goes to one of two finals

# Here the first final starts, it had two options
def final_1():
    time.sleep(1)
    print("\nThey are trying to detain me")
    time.sleep(1)
    print("\n1) Keep trying")
    print("2) Fight them")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1' or '2':
        time.sleep(1)
        print("\nThey are arresting me")
        time.sleep(1)
        print("\n1) Don't let them")
        print("2) Let them, they will take you inside")
        des_list = ['1', '2']
        des = getdes(des_list)
        if des == '1':
            time.sleep(1)
            print("\nThey are to many, I can't with all of them")
            time.sleep(.5)
            print(".....")
            time.sleep(.5)
            print(".....")
            time.sleep(.5)
            print("Well now I'm on a dungeon, how do I get out of here?")
            time.sleep(1)
            print("They took everything I had")
            time.sleep(1)
            print("\n1) Call a guard")
            print("2) Wait for a guard to pass")
            des_list = ['1', '2']
            des = getdes(des_list)
            if des == '1' or '2':
                time.sleep(1)
                print("\nHe is here, what now?")
                time.sleep(1)
                print("\n1) Distract him and get the keys")
                des_list = ['1']
                des = getdes(des_list)
                if des == '1':
                    time.sleep(1)
                    print("\nIt didn't work")
                    time.sleep(1)
                    print("\n1) Try to persuade him")
                    des_list = ['1']
                    des = getdes(des_list)
                    if des == '1':
                        time.sleep(1)
                        print("\nIt says I don't have the right skill")
                        time.sleep(1)
                        print("\n1) Try to explain him what's happening")
                        print("2) Tell him about the queen")
                        des_list = ['1', '2']
                        des = getdes(des_list)
                        if des == '1' or '2':
                            time.sleep(.5)
                            print("\n.....")
                            time.sleep(1)
                            print("He says the queen is in her room and nothing can happen to her")
                            time.sleep(1)
                            print(".....")
                            time.sleep(.5)
                            print(".....")
                            time.sleep(.5)
                            print("They say I'm no danger and they will set me free")
                            time.sleep(1)
                            print("\n1) Try to escape and go to the queen")
                            print("2) Run from them")
                            des_list = ['1', '2']
                            des = getdes(des_list)
                            if des == '1' or '2':
                                time.sleep(1)
                                print("\nThey are still behind me")
                                final_1_1()
        elif des == '2':
            time.sleep(1)
            print("\nThey put me in the dungeons, they only took my weapons")
            time.sleep(1)
            print("\n1) Drink a strenght potion")
            print("2) Punch the bars with your armour")
            des_list = ['1', '2']
            des = getdes(des_list)
            if des == '1' or '2':
                time.sleep(1)
                print("\nI'm out the cell now")
                time.sleep(1)
                print("\n1) Get a weapon")
                des_list = ['1']
                des = getdes(des_list)
                if des == '1':
                    time.sleep(1)
                    print("\nI can see a sword")
                    time.sleep(1)
                    print("\n1) Grab it and run")
                    print("2) Take it!")
                    des_list = ['1', '2']
                    des = getdes(des_list)
                    if des == '1' or '2':
                        time.sleep(1)
                        print("\nI'm on my way to the queen's room now")
                        time.sleep(1)
                        print(".....")
                        time.sleep(1)
                        print(".....")
                        final_1_1()

# In this function both options connect for the first final

def final_1_1():
    time.sleep(1)
    print(".....")
    time.sleep(.5)
    print("I think I'm close")
    time.sleep(1)
    print("I hear someone")
    time.sleep(1)
    print("Wait, it sounds like more than one person")
    time.sleep(1)
    print("\n1) Go in now!")
    print("2) There is no other option, try to help!")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1' or '2':
        time.sleep(1)
        print("\nIt....")
        time.sleep(1)
        print("It's....")
        time.sleep(1)
        print("To late")
        time.sleep(1)
        print("\n1) What happened?")
        print("2) What do you mean?")
        des_list = ['1', '2']
        des = getdes(des_list)
        if des == '1' or '2':
            time.sleep(1)
            print("\nShe....")
            time.sleep(1)
            print("Is dead")
            time.sleep(1)
            print("The queen is in the floor, there is a man with a sword")
            time.sleep(1)
            print("It was him")
            time.sleep(1)
            print(".....")
            time.sleep(.5)
            print(".....")
            time.sleep(.5)
            print("-EXTERIOR SOUND-")
            time.sleep(.5)
            print("-EXTERIOR SOUND-")
            time.sleep(.5)
            print("Holly, I think there is someone trying to get in my house")
            time.sleep(1)
            print("\n1) Call the police")
            des_list = ['1']
            des = getdes(des_list)
            if des == '1':
                time.sleep(1)
                print("\nThere is no signal on my phone")
                time.sleep(1)
                print("\n1) Call the police")
                des_list = ['1']
                des = getdes(des_list)
                if des == '1':
                    time.sleep(1)
                    print("\nI live on a third floor")
                    time.sleep(1)
                    print("There is nowhere to go")
                    time.sleep(1)
                    print(".....")
                    time.sleep(.5)
                    print(".....")
                    time.sleep(.5)
                    print("-PLAYER HAS DISCONNECTED-")
                    end()

# This goes to the second final

def final_2():
    time.sleep(1)
    print("\nI think I can climb the outside wall")
    time.sleep(1)
    print("\n1) Do it!")
    print("2) Hurry up!")
    des_list = ['1', '2']
    des = getdes(des_list)
    if des == '1' or '2':
        time.sleep(1)
        print("\nI can see the queen's room from here")
        time.sleep(1)
        print("\n1) Go stealthily")
        print("2) Run towards it")
        des_list = ['1', '2']
        des = getdes(des_list)
        if des == '1':
            time.sleep(1)
            print("\nI need to hurry")
        elif des == '2':
            time.sleep(1)
            print("\nI'm on my way")
        time.sleep(1)
        print(".....")
        time.sleep(.5)
        print("I think I'm here, I'll go in")
        time.sleep(1)
        print("\n1) Be careful")
        print("2) Go!")
        des_list = ['1', '2']
        des = getdes(des_list)
        if des == '1' or '2':
            time.sleep(1)
            print("\nThey are in here, the queen has a sword in her hand")
            time.sleep(1)
            print("\n1) Go help her")
            print("2) Stop talking and fight")
            des_list = ['1', '2']
            des = getdes(des_list)
            if des == '1' or '2':
                time.sleep(1)
                print("\nThere's three of them")
                time.sleep(1)
                print(".....")
                time.sleep(.5)
                print("They look strong")
                time.sleep(1)
                print(".....")
                time.sleep(.5)
                print("I'm taking a lot of damage")
                time.sleep(1)
                print(".....")
                time.sleep(.5)
                print("There is one left")
                time.sleep(1)
                print(".....")
                time.sleep(.5)
                print("She is safe")
                time.sleep(1)
                print("-Message received-")
                time.sleep(1)
                print("\n1) What does it say?")
                print("2) Read it")
                des_list = ['1', '2']
                des = getdes(des_list)
                if des == '1' or '2':
                    time.sleep(1)
                    print("\nIt says creator")
                    time.sleep(1)
                    print("Apparently i just saved his project")
                    time.sleep(1)
                    print("The queen says she is an experiment to make better AIs")
                    time.sleep(2)
                    print("More intelligent and human like")
                    time.sleep(1)
                    print("Well I think someone is behind the creator and his project")
                    time.sleep(2)
                    print("\n1) Be careful the could be after you now")
                    print("2) At least you helped")
                    des_list = ['1', '2']
                    des = getdes(des_list)
                    if des == '1' or '2':
                        time.sleep(1)
                        print("\nI guess everything is good now")
                        time.sleep(1)
                        print("I'll go rest, I have a life too you know")
                        time.sleep(1)
                        print("-PLAYER HAS DISCONNECTED-")
                        end()

# Credits I made just because

def end():
    time.sleep(1)
    print("\n-The END-")
    time.sleep(1)
    print("\n.....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print("\n Story by: Roberto Vazquez Lopez")
    time.sleep(.5)
    print("\n.....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print("\nCode by: Roberto Vazquez Lopez")
    time.sleep(.5)
    print("\n.....")
    time.sleep(.5)
    print(".....")
    time.sleep(.5)
    print("\nThanks for playing")
    time.sleep(1)
    quit()



def getdes(des_list):
    """Checks if the decision the player takes is valid"""
    des = input()
    if des in des_list:
        return des
    else:
        print('-Please enter a valid option-')
        return getdes(des_list)

def class_chosen(classes):
    """Checks if the class the player chose is valid"""
    class_ = input('\nClass: ')
    if class_ in classes:
        return class_
    elif class_.title() in classes:
        return class_
    elif class_.upper() in classes:
        return class_
    else:
        print('-Please enter a valid class-')
        return class_chosen(classes)

def quit():
    """Quits the game"""
    exit()

if __name__ == "__main__":
    start_game()