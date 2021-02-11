def load():
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
    
    dictionary_de = {}
    dictionary_en = {}
    vocab_file = open("vocab.txt", "r+", encoding='utf8')
    dictionary_file = open("tryout.txt", "r")

    for line in vocab_file:
        word_entry = line.split(',')
        dictionary_de[word_entry[0]] = (word_entry[2], word_entry[1], list(word_entry[3]))
        dictionary_en[word_entry[2]] = (word_entry[0], word_entry[1], list(word_entry[4][:-1]))
        
    for line in dictionary_file:
        word = (line.split(','))
        
        if word[0] in dictionary_de:
            pass
        elif word[0] == '\n':
            pass
        else:
            vocab_entry = ""
            dictionary_de[word[0]] = [(word[1])[1:], (word[2])[1:-1], [0,0,0,"new"]]
            dictionary_en[word[1]] = [(word[0])[1:], (word[2])[1:-1], [0,0,0,"new"]]
            vocab_entry = str(word[0]) + ',' + str((word[1])[1:]) + ',' + str((word[2])[1:-1]) + ',' + "000n" + ',' + "000n"
            vocab_file.write(vocab_entry)
            vocab_file.write('\n')
    
    return [dictionary_de, dictionary_en]

    
def update(dictionaries):
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
    
    vocab_file = open("vocab.txt", "w", encoding='utf8')
    delimiter = ','
    for entry in dictionaries[0]:
        line = []
        line.append(entry)
        line.append(dictionaries[0][entry][1])
        line.append(dictionaries[0][entry][0])  
        line.append(str(int(dictionaries[0][entry][2][0])) + 
            str(int(dictionaries[0][entry][2][1])) + 
            str(int(dictionaries[0][entry][2][2])) + 
            str(dictionaries[0][entry][2][3]))
        
        eng = dictionaries[0][entry][0]
        line.append((str(int(dictionaries[1][eng][2][0])) + 
            str(int(dictionaries[1][eng][2][1])) + 
            str(int(dictionaries[1][eng][2][2])) + 
            str(dictionaries[1][eng][2][3])) + "\n")
            
        new_line = delimiter.join(line)    
        vocab_file.write(new_line)    