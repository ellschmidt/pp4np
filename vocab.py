# Vocabulary Module
import random
def trainer(dictionaries):
    
    answer = ""
    new_word = True
    update_counter = 0
    
    while answer != "xxx":
    
        if new_word == True:
            if update_counter == 0 or update_counter >= 10:
                test_list = create_test_list(dictionaries)
                update_counter = 0
            else:
                pass
            
            test_word = random.choice(test_list)
            print(test_word)
            if test_word[2] == "de":
                language = 0
            else: language = 1    
                  
            update_counter += 1
            print("What is the correct translation for the following word: " + test_word[0] + "?")
        
        else:
            pass
        
        answer = input()
       
        if answer == "pass":
            new_word = True
            dictionaries[language][test_word[0]][2][2] = int(dictionaries[language][test_word[0]][2][2]) + 1
            print("The correct answer would be: " + test_word[1])
            pass
        elif answer == "xxx":
            break
        elif answer == test_word[1]:
            new_word = True
            dictionaries[language][test_word[0]][2][1] = int(dictionaries[language][test_word[0]][2][1]) + 1
            print("That's correct!")
        else:
            new_word = False
            dictionaries[language][test_word[0]][2][2] = int(dictionaries[language][test_word[0]][2][2]) + 1
            print("I'm sorry, that wasn't correct. Try again:")
        
        dictionaries[language][test_word[0]][2][0] = int(dictionaries[language][test_word[0]][2][0]) + 1
        dictionaries[language][test_word[0]][2][3] = "k"
		
    return dictionaries
    
def create_test_list(dictionaries):
    
    test_list = []
    for entry in dictionaries[0]:
        #print(entry)
        #print(dictionaries[0])
        if int(dictionaries[0][entry][2][0]) != 0:    
            fail_ratio = int(dictionaries[0][entry][2][2])/int(dictionaries[0][entry][2][0])
        else: 
            fail_ratio = 0.5
        repeat = int(fail_ratio * 10) + 1
        entry = [entry, dictionaries[0][entry][0], "de"]
        print(repeat)        
        while repeat != 0:
            repeat += -1
            test_list.append(entry)
    
    for entry in dictionaries[1]:
        if int(dictionaries[1][entry][2][0]) != 0: 
            fail_ratio = int(dictionaries[1][entry][2][2])/int(dictionaries[1][entry][2][0])
        else: 
            fail_ratio = 0.5
        repeat = int(fail_ratio * 10) + 1
        entry = [entry, dictionaries[1][entry][0], "en"]
        print(repeat)
        while repeat != 0:
            repeat += -1
            test_list.append(entry)
                    
    return test_list