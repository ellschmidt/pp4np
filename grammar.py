# Grammar Module

in1=input("Build a german sentence \(*-*)/\n"
      "Type a pronoun and press enter:")

if in1 in pronoun_list:
    pass
else: 
    print("This is not a correct pronoun! Use one of the following: ich, du, er, sie, es, wir, ihr, sie")
    
in2=input("a form of to be: ")




in3=input("and an adjective: ")




sentence = in1 + " " + in2 + " " + in3 + "."

pronoun_list = ["ich", "du", "er", "sie", "es", "wir", "ihr", "sie"]
be_list = ["bin", "bist", "ist", "sind", "seid"]
combo_list = ["ich bin", "du bist", "er ist", "sie ist", "es ist", "wir sind", "ihr seid", "sie sind"]



combo = in1 + " " + in2

if combo in combo_list:
    print("Your senctence: " + sentence + " is correct.")
else:
    print("Your senctence: " + sentence + " is not correct. Try again, you got this!")