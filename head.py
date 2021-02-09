import loading_files as load
import dic as translate
import vocab
import madlibstwo as mad
dictionaries = load.load()
dict_de = dictionaries[0]
dict_en = dictionaries[1]

#dictionaries = vocab.trainer(dictionaries)
mad.madlib(dictionaries)

'''

# load vocab file
# read dictionary file
# check for new entries
# add them to vocab file while creating entry-objects


d1 = {'a': 100, 'b': 200, 'c':300}

# "Begrüßung"
# "Main Menü"


while input != "Exit!":
	
	while input != "out":
		
		if input == "Dic":
			
            word_input = input("Type in a word: ")
            translation = translate.translate(str(word_input))
            if translation[1] == "de":
                print(word_input + " in English is " + translation[0])
            elif translation[1] == "en":
                print(word_input + " in German is " + translation[0])
            else:
                pass
                
			show.main_menu()
			
		elif input == "Vocab":
			
			vocab()
			
			show.main_menu()
            
        elif input == "Grammar":
            
            grammar()
            
            show.main_menu()
            
        elif input == "MadLib":
            
            mad()
            
            show.main_menu()
            
        elif input == "Stats":
        
            stats()
            
            show.main_menu()
            
        elif input == "Help":
            
            print(help)
            
            show.main_menu()
          
        else:
            Error
'''

#write to VocabFile
load.update(dictionaries)
#"Bye"