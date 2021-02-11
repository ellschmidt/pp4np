# Grammar Module

def grammar(dictionaries):
    ''' 
    lets the user create short sentences with the verb 'to be' in German
     and checks the correct conjugation
    
    the module can be exited by entering 'm' during any input request
    
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary    
    '''
    
    inp = ""
    inp1 = ""
    inp2 = ""
    inp3 = ""
    broken = False      # boolean to check wether 'm' was inserted and the second level while-loop therefore broken
    
    pronoun_list = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie"]
    be_list = ["bin", "bist", "ist", "sind", "seid"]
    adjective = []
    for entry in dictionaries[0]:       # create list of all German adjectives currently in the dictionary
        if dictionaries[0][entry][1] == "(adj.)":
            adjective.append(entry)
        else:
            pass
                
    while inp != "m" and inp1 != "m" and inp2 != "m" and inp3 != "m":    # to exit the module enter 'm' at any time
       
        print("Build a german sentence \(*-*)/\n")
        
        in1 = input("Type a pronoun and press enter: ")
        while in1 not in pronoun_list:      # keep asking until the user choses a correct pronoun
            if in1 == "m":
                broken = True
                break
            print("This is not a correct pronoun! Use one of the following: ich, du, er, sie, es, wir, ihr, sie")
            in1 = input("Type a pronoun and press enter: ")
        if broken == True:
            print("You're back in the main menu.")
            break
            
        in2 = input("\na form of to be: ")
        while in2 not in be_list:       # keep asking until the user choses a correct for of 'to be' in German
            if in2 == "m":
                broken = True
                break
            print("This is not a correct form of 'to be'. Use one of the following: bin, bist, ist, sind, seid")
            in2 = input("\na form of to be: ")
        if broken == True:
            print("You're back in the main menu.")
            break
        
        in3 = input("\nand an adjective: ")
        while in3 not in adjective:     # keep asking until the user choses an adjective from the dictionary
            if in3 == "m":
                broken = True
                break
            print("This is not an adjective from the dictionary.")
            in3 = input("\nand an adjective: ")
        if broken == True:
            print("You're back in the main menu.")
            break
            
        sentence = in1 + " " + in2 + " " + in3 + "."
        
        #list of correct solutions
        combo_list = ["ich bin", "du bist", "er ist", "sie ist", "es ist", "wir sind", "ihr seid", "sie sind"]
        combo = in1 + " " + in2

        if combo in combo_list:
            print("Your senctence: \"" + sentence + "\" is correct.")
        else:
            print("Your senctence: \"" + sentence + "\" is not correct. Try again, you got this!")