def load():
    dictionary_de = {}
    dictionary_en = {}
    vocab_file = open("vocab.txt", "r+", encoding='utf8')
    dictionary_file = open("tryout.txt", "r")

    for line in vocab_file:
        word_entry = line.split(',')
        #print(word_entry)
        dictionary_de[word_entry[0]] = (word_entry[2], word_entry[1], list(word_entry[3]))
        dictionary_en[word_entry[2]] = (word_entry[0], word_entry[1], list(word_entry[4][:-1]))
    
    #print(dictionary_de)    
    for line in dictionary_file:
        word = (line.split(','))
        #print(word)
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
    vocab_file = open("vocab.txt", "w", encoding='utf8')
    delimiter = ','
    for entry in dictionaries[0]:
        line = []    
        #print(entry)
        line.append(entry)
        line.append(dictionaries[0][entry][1])
        line.append(dictionaries[0][entry][0])
        #print(dictionaries[1][dictionaries[0][entry][0]][2][0])    
        line.append(str(int(dictionaries[0][entry][2][0])) + 
            str(int(dictionaries[0][entry][2][1])) + 
            str(int(dictionaries[0][entry][2][2])) + 
            str(dictionaries[0][entry][2][3]))
        eng = dictionaries[0][entry][0]
        
        line.append((str(int(dictionaries[1][eng][2][0])) + 
            str(int(dictionaries[1][eng][2][1])) + 
            str(int(dictionaries[1][eng][2][2])) + 
            str(dictionaries[1][eng][2][3])) + "\n")
        #print(line)    
        new_line = delimiter.join(line)    
        vocab_file.write(new_line)    