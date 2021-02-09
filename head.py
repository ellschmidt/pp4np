import loading_files as load
import dic as translate
import vocab
import madlibstwo as mad
import grammar
dictionaries = load.load()
dict_de = dictionaries[0]
dict_en = dictionaries[1]

print("Begrüßung")
print("------------")
print("Main Menü")
print("###################")

inp = ""

while inp != "Exit!":
	
	inp = input()
			
	if inp == "1":
		
		word_input = input("Type in a word: ")
		translation = translate.translate(str(word_input))
		if translation[1] == "de":
			print(word_input + " in English is " + translation[0])
		elif translation[1] == "en":
			print(word_input + " in German is " + translation[0])
		else:
			pass
			
		#show.main_menu()
		
	elif inp == "2":
		
		dictionaries = vocab.trainer(dictionaries)
		
		#show.main_menu()
		
	elif inp == "3":
		
		grammar.grammar(dictionaries)
		
		#show.main_menu()
		
	elif inp == "4":
		
		mad.madlib(dictionaries)
		
		#show.main_menu()
		
	elif inp == "Stats":
	
		stats()
		
		#show.main_menu()
		
	elif inp == "Help":
		
		print("help")
		
		#show.main_menu()
	  
	else:
		print("Error")


#write to VocabFile
load.update(dictionaries)
print("Bye")