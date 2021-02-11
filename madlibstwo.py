import random

def madlib(dictionaries):
    ''' 
    creates and prints out three madlibs (unicorn, shakespeare, princess) on 'r'
    uses preferably known words from the English dictionary
        
    the module can be exited by entering 'm' during any input request
    
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary    
    '''
    
    inp = ""
    
    while inp != "m":
        
        inp = input()
        
        if inp == "r":
            noun_all = []             
            noun_known = []
            adjective_all = []
            adjective_known = []
            verb_all = []
            verb_known = []

            for entry in dictionaries[1]:
                if dictionaries[1][entry][1] == "(noun)":
                    noun_all.append(entry)      # list of all English nouns in the dictionary  
                    if dictionaries[1][entry][2][3] == "k":
                        noun_known.append(entry)    # list of all known English nouns in the dictionary
                    
                elif dictionaries[1][entry][1] == "(adj.)":
                    adjective_all.append(entry)
                    if dictionaries[1][entry][2][3] == "k":
                        adjective_known.append(entry)
                
                elif dictionaries[1][entry][1] == "(verb)":
                    verb_all.append(entry)
                    if dictionaries[1][entry][2][3] == "k":
                        verb_known.append(entry)
                 
                else: 
                    print("That's not a type I know.")
            
            ### UNICORN MADLIB ###
            # check if there are enough known words for this madlib in the respective list
            noun = noun_all if len(noun_known) < 3 else noun_known
            adjective = adjective_all if len(adjective_known) < 2 else adjective_known
            verb = verb_all if len(verb_known) < 1 else verb_known
            
            print("\nUNICORN MADLIB")
            print("--------------")
            print("A unicorn is nothing like a(n) " + (random.choice(noun)) + ". \nThey're " + random.choice(adjective) + 
                  " creatures. \nSome have a(n) " + random.choice(noun) + " mane of hair and others \nhave a(n) " + 
                  random.choice(adjective) + " " + random.choice(noun) + " on their head. \nI would love " + 
                  random.choice(verb) + " a unicorn one day.")
            
            ### SHAKESPEARE MADLIB ###
            noun = noun_all if len(noun_known) < 2 else noun_known
            adjective = adjective_all if len(adjective_known) < 1 else adjective_known
            verb = verb_all if len(verb_known) < 1 else verb_known
            
            print("\nSHAKESPEARE MADLIB")
            print("------------------")
            print ("To be, or not to be, that is the question: \n"
                   "Whether 'tis " + (random.choice(adjective)) + " in the mind " + random.choice(verb) + "\n" +
                   "The slings and " + random.choice(noun) + " of outrageous fortune, \n"
                   "Or to take arms against a " + random.choice(noun) + " of trouble \n"
                   "And by opposing end them.")
            
            ### PRINCESS MADLIB ###
            noun = noun_all if len(noun_known) < 1 else noun_known
            adjective = adjective_all if len(adjective_known) < 3 else adjective_known
            verb = verb_all if len(verb_known) < 1 else verb_known
            
            print("\nPRINCESS MADLIB")
            print("---------------")
            print ("There once lived a " + (random.choice(adjective)) + " princess in a " + (random.choice(adjective)) + " castle. \n"
                   "Her favorite hobby and greatest passion was it " + (random.choice(verb)) + ". \nShe did it every day and night.\n"
                   "One day she won a competition in this discipline. \nThe first prize was a " + random.choice(noun) +
                   " and she war very " + (random.choice(adjective)) + " about it.")
        
        elif inp == "m":
            print("You're back in the main menu.")
            break
            
        else:
            print("You can't do that here. Chose either r or m.")
