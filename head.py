import loading_files as load
import dic as translate
import vocab
import madlibstwo as mad
import grammar

dictionaries = load.load()

print("Begrüßung")
print("------------")
print("Main Menu")
print("###################")

inp = ""

while inp != "e":
	    
	inp = input()
			
	if inp == "1":
		
		translate.translate(dictionaries)     # enter Dictionary-Module
				
	elif inp == "2":
		
		dictionaries = vocab.trainer(dictionaries)  # enter Vocabulary-Module
		
	elif inp == "3":
		
		grammar.grammar(dictionaries)   # enter Grammar-Module
		
	elif inp == "4":
		
		mad.madlib(dictionaries)    # enter MadLib-Module
		
	elif inp == "5":
		
		load.update(dictionaries)       
		vocab.statistics(dictionaries)  #update statistics in statistics.csv
		
	elif inp == "i":
		
		print("Info")   # print information about the program and underlying processes
	
	elif inp == "m":
		
		print("Main Menu")    # print directions again
	
	else:
		print("You can't do that here. Enter 'm' to see where you can go.")


load.update(dictionaries)   #save progress to vocab.txt
print("Bye")