# Grammar Module

def grammar(dictionaries):
    
    adjective = []
    for entry in dictionaries[0]:
        if dictionaries[0][entry][1] == "(adj.)":
            adjective.append(entry)
        else:
            pass
    
    pronoun_list = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie"]
    be_list = ["bin", "bist", "ist", "sind", "seid"]
    
    print("Build a german sentence \(*-*)/\n")
    in1 = input("Type a pronoun and press enter: ")

    while in1 not in pronoun_list:
        print("This is not a correct pronoun! Use one of the following: ich, du, er, sie, es, wir, ihr, sie")
        in1 = input("Type a pronoun and press enter: ")
        
    in2 = input("\na form of to be: ")

    while in2 not in be_list:
        print("This is not a correct form of 'to be'. Use one of the following: bin, bist, ist, sind, seid")
        in2 = input("\na form of to be: ")

    in3 = input("\nand an adjective: ")

    while in3 not in adjective:
        print("This is not an adjective from the dictionary.")
        in3 = input("\nand an adjective: ")

    sentence = in1 + " " + in2 + " " + in3 + "."
    combo_list = ["ich bin", "du bist", "er ist", "sie ist", "es ist", "wir sind", "ihr seid", "sie sind"]
    combo = in1 + " " + in2

    if combo in combo_list:
        print("Your senctence: \"" + sentence + "\" is correct.")
    else:
        print("Your senctence: \"" + sentence + "\" is not correct. Try again, you got this!")