import random

def madlib(dictionaries):
    noun = []
    adjective = []
    verb = []

    for entry in dictionaries[1]:
        if dictionaries[1][entry][1] == "(noun)":
            noun.append(entry)
        
        elif dictionaries[1][entry][1] == "(adj.)":
            adjective.append(entry)
        
        elif dictionaries[1][entry][1] == "(verb)":
            verb.append(entry)
         
        else: 
            print("That's not a type I know.")

    print("\nUNICORN MADLIB")
    print("--------------")
    print("A unicorn is nothing like a(n) " + (random.choice(noun)) + ". \nThey're " + random.choice(adjective) + 
          " creatures. \nSome have a(n) " + random.choice(noun) + " mane of hair and others have a(n) " + 
          random.choice(adjective) + " " + random.choice(noun) + " on their head. \nI would love " + 
          random.choice(verb) + " a unicorn one day.")
    
    print("\nSHAKESPEARE MADLIB")
    print("------------------")
    print ("To be, or not to be, that is the question: \n"
           "Whether 'tis " + (random.choice(adjective)) + " in the mind " + random.choice(verb) + "\n" +
           "The slings and " + random.choice(noun) + " of outrageous fortune, \n"
           "Or to take arms against a " + random.choice(noun) + " of trouble \n"
           "And by opposing end them.")
    
    print("\nPRINCESS MADLIB")
    print("---------------")
    print ("There once lived a " + (random.choice(adjective)) + " princess in a " + (random.choice(adjective)) + " castle. \n"
           "Her favorite hobby and greatest passion was it " + (random.choice(verb)) + ". \nShe did it every day and night.\n"
           "One day she won a competition in this discipline. \nThe first prize was a " + random.choice(noun) +
           "and she war very " + (random.choice(adjective)) + " about it.")
