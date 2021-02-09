import random

def madlib(dictionaries):
    #print(dictionaries)
    noun = []
    adjective = []
    verb = []

    for entry in dictionaries[1]:
        #print(entry)
        #print(dictionaries[1][entry][1])
        if dictionaries[1][entry][1] == "(noun)":
            #print("NOUN")
            noun.append(entry)
        
        elif dictionaries[1][entry][1] == "(adj.)":            
            #print("ADJ")
            adjective.append(entry)
        
        elif dictionaries[1][entry][1] == "(verb)":
            #print("VERB")
            verb.append(entry)
         
        else: 
            print("That's not a type I know.")


    print("A unicorn is nothing like a(n) " + (random.choice(noun)) + ". They're " + random.choice(noun) + 
          " creatures. Some have a(n) " + random.choice(noun) + " mane of hair and others have a(n) " + 
          random.choice(adjective) + " " + random.choice(noun) + " on their head. I would love " + 
          random.choice(verb) + " a unicorn one day.")
