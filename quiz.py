# Our quiz!

def quiz():

    import time
    
    score = 0
    rank = ""

    print("This is the pokemon quiz!")
    time.sleep(1)

    username = input("Username: ")

    print("Hello " + username + ". Welcome to Ben Knowlson's pokemon quiz.")
    time.sleep(3)
    print("You will have to answer 20 questions and depending on your score you'll recieve a Poke'rank! Enjoy! :)")
    time.sleep(5)

    q1 = input("How many generations of Pokemon are there?: ")

    if q1 == "6":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q2 = input("Which company developed Pokemon?: ")

    if q2.lower() == "nintendo":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q3 = input("What year was the first Pokemon game released?: ")

    if q3 == "1996":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q4 = input("Name an original starter Pokemon: ")

    if q4.lower() in "squirtlecharmanderbulbasaur":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q5 = input("What is the name of the Professor who gives you your first pokemon?: ")

    if "oak" in q5.lower():
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    print("----------------------------------------------------------------------")
    print("So far your score is", score, "out of 5! Questions are now harder!")
    print("----------------------------------------------------------------------")
    time.sleep(3)

    q6 = input("Who is Raichu an evolution of?: ")

    if q6.lower() == "pikachu":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q7 = input("What is the original name of the young pokemon trainer you control throughout the Pokemon series?: ")

    if q7.lower() == "ash":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q8 = input("What generation is the legendary Pokemon 'Entei' from?: ")

    if q8 == "2":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q9 = input("Which lake is the Shiny Gyrados found in Pokemon Soul Silver?: ")

    if q9.lower() in "lake of rage":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q10 = input("How many evolutions of Eevee are their between Gen 1-2?: ")

    if q10 == "5":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)
    
    print("----------------------------------------------------------------------")
    print("So far your score is", score, "out of 10! Questions are now EVEN harder!")
    print("----------------------------------------------------------------------")
    time.sleep(3)

    q11 = input("Which ball is more powerful: Master ball or Ultra ball?: ")

    if "master" in q11.lower():
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q12 = input("What generation was the region of Sinnoh introduced?: ")

    if q12 == "4":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q13 = input("Where is Kanto in direcion North/East/South/West from Sinnow?: ")

    if "south" in q13.lower():
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q14 = input("Who are the original villains in the Kanto based Pokemon games/series'?: ")

    if q14.lower() == "team rocket":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q15 = input("What is the name of the only 1st gen Pokemon beginning with the letter I? (Hint: Starter pokemon evolution): ")

    if q15.lower() == "ivysaur":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    print("----------------------------------------------------------------------")
    if score > 10:
        print("Wow! Your score is", score, "out of 15! These questions should catch you off guard!")
    else:
        print(score, "score? Keep going", username, "and good luck with the following questions...")
    print("----------------------------------------------------------------------")
    time.sleep(3)

    print("The following questions are almost impossible unless you played Pokemon as much as myself...")
    time.sleep(2)

    q16 = input("Where is the glitched Pokemon mssingno found in Pokemon Red/Blue?: ")

    if "cinnibar island" in q16.lower():
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q17 = input("How many legendary pokemon are there in Gen 4?: ")

    if q17 == "14":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q18 = input("Who is the first pokemon to talk in the Anime TV series?: ")

    if q18.lower() == "meowth":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    q19 = input("Which Pokemon was the first to ever be created?: ")

    if q19.lower() == "rhydon":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)

    print("Now, the hardest question... You are", 20 - score, "score away from the legendary 20/20!")

    q20 = input("Which Pokemon is Gengar believed to be the shadow of?: ")

    if q20.lower() == "clefable":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
    time.sleep(1)
# SPARE SPACE TO CONTINUE QUIZ
#
#

    if score == 0:
        print("Wow,", score, "score? You're bad at Pokemon")

    if 0 < score <= 4:
        rank = "casual"

    elif 4 < score <= 8:
        rank = "trainer"

    elif 8 < score <= 12:
        rank = "expert"

    elif 12 < score <= 16:
        rank = "mythical"

    elif 16 < score <= 19:
        rank = "legend"

    elif score == 20:
        rank = "mewtwo"

    print("I have ranked you", rank, "based on your score of", score, "out of 20! GG", username)

    



# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()

