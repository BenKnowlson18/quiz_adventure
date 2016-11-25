# An adventure game

from time import sleep
from random import randint

#BENDOG, [FRIENDLY] MAIN CHARECTAR, PREPARATION AND DECISION
bendog_health = 100
bendog_dmg = 4
bendog_money = 250

#NEGAN, [FRIENDLY] WEAPON DEALER
negan_health = 100
negan_dmg = 19
negan_money = 500

#ADBREZZ, [FRIENDLY] ARMOR DEALER
adbrezz_health = 100
adbrezz_dmg = 4
adbrezz_money = 1250

#TOTALLYNOTALEX, [TRAITOR] CURRENCY HOLDER (BANK)
totallynotalex_health = 100
totallynotalex_dmg = 4
totallynotalex_money = 4750

#BOZZMAN, [ENEMY] HACKER
bozzman_health = 100
bozzman_dmg = 1
bozzman_money = 1500
    
#BOSS MICKY, [MAFIA LEADER] MENTAL STRENGTH, LEADER OF BOZZMAN
bossmicky_health = 250
bossmicky_dmg = 75
bossmicky_money = 0

#MR CHARLTON, [CODE MAKER] TEACHER
charlton_health = 100
charlton_dmg = 4
charlton_money = 50

#100 is the base health, armor bought from adbrezz increases health
#4 is base damage, buying guns from Negan will increase base damage
#Alex will keep your money safe, or will he?

def pausedash():
    sleep(2)
    print("")
    print("---------------------------------------------------------------------------------------------")
    print("")

def intro():

#Intro to the game##################################################################################################################################################################################
    print("4:43 PM, Base of operations...")
    sleep(2)
    print("Negan: We must form an alliance to take out this Micky guy. He has been abusing to many innocent people online.")
    sleep(2)
    print("Alex: I know, Tom Pattison told me, he's caused at least 6 people to quit twitter in the last month...")
    sleep(2)
    print("Negan: Exactly, we must stop him before it gets out of hand, you guys in?")
    sleep(2)
    print("Alex: Yeah.")
    sleep(2)
    print("Adam: Sure.")
    sleep(2)
    intro1 = input("Negan: Bendog? (Yes/No): ")
    if intro1.lower() == "no":
        sleep(2)
        print("*Negan pull's out a Glock-18*")
        sleep(2)
        print("Negan: We must hide the evidence...")
        sleep(2)
        print("*Negan pulls the trigger aiming between your eyes*")
        sleep(2)
        print("")
        intro2 = input("Nice try, want to try again? (Yes/No): ")
        if intro2.lower() == "yes":
            sleep(2)
            print("You try again...")
            pausedash()
            intro()
        elif intro2.lower() == "no":
            sleep(2)
            print("Fair enough...")
            quit
    elif intro1.lower() == "yes":
        sleep(2)
        print("Negan: Nice, lets get going...")
        sleep(2)
        print("The team setup for their operation over the next couple of days, now the real story unfolds...")
        pausedash()
        story1()

# STORY 1 FUNCTIONS ################################################################################################################################################################################

def story1_1():

    global bendog_money, totallynotalex_money
    
    bendog_money == bendog_money - 250
    totallynotalex_money == totallynotalex_money + 250
    sleep(1)
    print("Alex: Cheers, I knew you could trust me mate")
    print("Alex: *puts money in pocket*")
    sleep(2)
    zzzzzz = input("Bendog: ")
    sleep(2)
    print("Alex: Right, I'll leave you to your thing. Seeya mate...")
    sleep(2)

def story1_2():

    sleep(1)
    print("Alex: Whatever, Negan and Adam said to meet them in the front room whenever you're ready...")
    sleep(2)
        
def story1fightresult():

    story1fight1()
    story1fight2()
    story1fight3()

def story1fight1():

    if x == 1:
        print("*You outsrength Alex and push him onto the floor, reducing his health by 10 and taking your money back*")
        totallynotalex_health = totallynotalex_health - 10
        sleep(2)
        print("Alex: Geez Ben, I was only trying to help")
        sleep(2)
        print("Bendog: Shut up man ya radgy, I'll knock ya block off")
        sleep(2)
        print("Negan: *Shouts* Ben, please come to the front room ASAP")

def story1fight2():

    if x == 2:
        print("*Alex swings a hefty right hook and hits you in the temple where it could be fatal*")
        bendog_money = bendog_money - 250
        totallynotalex_money = totallynotalex_money + 250
        sleep(2)
        xx = randint(1, 10)
        if xx == 10:
            print("*It does prove fatal, how embarrasing...*")
            sleep(2)
            print("")
            print("GAME OVER, and you don't get to retry because your death scene was too embarrasing, sorry :)")
            exit
        else:
            print("*It wasn't fatal, but you do lose 10 health*")
            sleep(2)
            print("Alex: Cheers hew...")
            sleep(2)
            print("Bendog: Feeble ####!")
            sleep(1)
            print("Alex: Oh, also Negan wants to see you at the front room marra, you'd best clean up first")

def story1fight3():

    if x == 3:
        print("*The bundle of money tears in half*")
        bendog_money = bendog_money - 250
        sleep(2)
        print("Bendog: Well that was brilliant, wasn't it")
        sleep(2)
        print("Alex: Shouldn't have fought back")
        sleep(2)
        print("Bendog: #### off ya cocky #####...")
        sleep(2)
        print("Alex: Calm down, Negan says he wants you in the front room before long anyway")  

def nofight():

    print("*Alex takes the money and puts it in his pocket*")
    bendog_money = bendog_money - 250
    totallynotalex_money = totallynotalex_money + 250
    sleep(2)
    print("Bendog: Whyaye man...")
    sleep(2)
    print("Alex: Hah, taxed")
    sleep(2)
    print("Bendog: Better keep it safe, me nan gave is that for me birthday")
    sleep(2)
    print("*Alex smiles, savagely*")
    sleep(1)
    print("Alex: I will, Negan said to see him in the front room, catch you in a bit")
    sleep(2)
    print("Bendog: Aight...")
    story2()

def story1():

    global bendog_health
    global bendog_money
    global totallynotalex_health
    global totallynotalex_money

    print("12:53 AM, Base of operations...")
    sleep(2)
    print("Alex: I'm now the financial organiser, want me to keep your money in the pot? I see you have 250 quid...")
    sleep(1)
    print("A: Aye, go on then")
    print("B: Nor, sorry pal")
    print("C: Can't I just keep it myself?")
    story1a = input("A, B or C: ")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    if story1a.lower() == "a":
        story1_1()
    elif story1a.lower() == "b":
        story1_2()
    elif story1a.lower() == "c":
        sleep(1)
        print("Alex: Nah, give it here.")
        sleep(1)
        ("*Alex tries to snatch the money*")
        sleep(2)
        story1ac = input("Fight back? (Yes/No): ")
    if story1ac.lower() == "yes":
        sleep(2)
        x = randint(1, 3)
    if story1ac.lower() == "yes":
        story1fightresult()
    elif story1ac.lower() == "no":
        nofight()
    story2()

# STORY 2, JUST A SMALL CUTSCENE... ##############################################################################################################################################################

def story2():

    pausedash()

    print("1:05 PM, Frontroom, Base of operations")
    sleep(2)
    print("Negan: Ok guys, we are ready to start with this operation")
    sleep(2)
    print("Adam: Nice one")
    sleep(2)
    print("Negan: As you all know we have sorted our roles in this operation")
    sleep(2)
    print("Bendog: I didn't know")
    sleep(2)
    print("Negan: Well, I'm going to be dealing weapons")
    sleep(1)
    print("Adam: I'll get protection and armor sorted")
    sleep(1)
    print("Alex: I'll tax yer cash")
    sleep(1)
    print("Bendog: And I'll take charge of this mission")
    sleep(1)
    print("Negan: Sound. Then lets get stuck in!")
    



def hubguide():
# This is going to be a menu, and a guide for it

    pausedash()

    sleep(2)
        
    
    
    
# This is no where near done hew :(
    






# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    intro()
