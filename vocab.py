# Vocabulary Module

import random
import csv

def trainer(dictionaries):
    ''' 
    provides a random word and asks the user for the translation into the other language
    performance is recorded  with counting how many times a word was tested, how many times 
     the user gave the correct answer and how many times they failed
        
    the module can be exited by entering 'm' during any input request
    
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary
    
    Return
    ------
    the dictionaries with updated statistics    
    '''
    
    answer = ""
    new_word = True
    update_counter = 0
    
    while answer != "m":
    
        if new_word == True:
            if update_counter == 0 or update_counter >= 10:
                # a new list containing the words for testing is created after ten querys 
                # to include the updated statistics counts, but decrease computation time 
                test_list = create_test_list(dictionaries)      
                update_counter = 0
            else:
                pass
            
            test_word = random.choice(test_list)    # select a random word for testing
            
            language = 0 if test_word[2] == "de" else 1
               
            update_counter += 1
            print("What is the correct translation for the following word: " + test_word[0] + "?")
        
        else:
            pass
        
        answer = input()
       
        if answer == "pass":    # fail-count of the current word is upped and a new word is selected
            new_word = True
            dictionaries[language][test_word[0]][2][2] = int(dictionaries[language][test_word[0]][2][2]) + 1
            print("The correct answer would be: " + test_word[1])
            pass
        elif answer == "m":     # exit the module
            print("You're back in the main menu.")
            break
        elif answer == test_word[1]:    # success-count of the current word is upped and a new word is selected
            new_word = True
            dictionaries[language][test_word[0]][2][1] = int(dictionaries[language][test_word[0]][2][1]) + 1
            print("That's correct!")
        else:
            new_word = False    # fail-count of the current word is upped, but no new word is selected
            dictionaries[language][test_word[0]][2][2] = int(dictionaries[language][test_word[0]][2][2]) + 1
            print("I'm sorry, that wasn't correct. Try again:")
        
        dictionaries[language][test_word[0]][2][0] = int(dictionaries[language][test_word[0]][2][0]) + 1
        dictionaries[language][test_word[0]][2][3] = "k"    # word's status is changed from new to known (needed in MadLib Module)
		
    return dictionaries
    

def create_test_list(dictionaries):
    ''' 
    creates a list of words to test in the vocabulary trainer
    contents of the list are made dependent on the current statistics in the dictionaries
    new words are added five times to the list
    words with a high failed/tested-ratio are added more often (up to eleven times)
    words with a zero-fail-rate are still added once
        
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary    
    
    Return
    ------
    list of [the word, the translation, the word's language]
    '''
    
    test_list = []
    
    for entry in dictionaries[0]:
        if int(dictionaries[0][entry][2][0]) != 0:    
            fail_ratio = int(dictionaries[0][entry][2][2])/int(dictionaries[0][entry][2][0])
        else: 
            fail_ratio = 0.5
        repeat = int(fail_ratio * 10) + 1
        entry = [entry, dictionaries[0][entry][0], "de"]        
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
        while repeat != 0:
            repeat += -1
            test_list.append(entry)
                    
    return test_list


def statistics(dictionaries):
    ''' 
    exports the current statistics of the dictionary to statistics.csv
    German words and their English translations are in consecutive rows
    tested/successful/failed-counts as well as the (un)known-status in 
     each row respect the direction of translation
    
    Parameters
    ----------
    dictionaries : list
        dictionaries[0] = German dictionary
        dictionaries[1] = English dictionary    
    '''
    
    vocab_file = open("vocab.txt", "r", encoding='utf8')
    statistics_file = open("statistics.csv", "w")
    statistics_writer = csv.writer(statistics_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    statistics_writer.writerow(['Word', 'tested', 'successful', 'failed', 'new/known'])
    
    for line in vocab_file:
        word_entry = line.split(',')
        
        german_line = [word_entry[0]]
        for i in word_entry[3]:
            german_line.append(i)
        
        english_line = [word_entry[2]]
        for j in word_entry[4][:-1]:
            english_line.append(j)
        
        statistics_writer.writerow(german_line)
        statistics_writer.writerow(english_line)