# Dictionary Module

def translate(dictionaries):
    ''' 
    translates the input word from the user into the other language
    
    the module can be exited by entering 'm' during any input request
    
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary 
    '''
        
    inp = ""
    
    while inp != "m":
        
        inp = input("Type in a word: ")
    
        if inp in dictionaries[0]:
            print(inp + " in English is " + dictionaries[0][inp][0])

        elif inp in dictionaries[1]:
            print(inp + " in German is " + dictionaries[1][inp][0])
        
        elif inp == "m":
            print("You're back in the main menu.")
            break
            
        else: 
            print("Word not found.")