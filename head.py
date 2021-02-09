import loading_files as load
import dic as translate
import vocab
import madlibstwo as mad
import grammar
dictionaries = load.load()
dict_de = dictionaries[0]
dict_en = dictionaries[1]

grammar.grammar(dictionaries)

'''
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
			
			dictionaries = vocab.trainer(dictionaries)
			
			show.main_menu()
            
        elif input == "Grammar":
            
            grammar.grammar(dictionaries)
            
            show.main_menu()
            
        elif input == "MadLib":
            
            mad.madlib(dictionaries)
            
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