import loading_files as load


dictionaries = load.load()


dict_de = dictionaries[0]
dict_en = dictionaries[1]
def translate(word):
    if word in dict_de:
        return [dict_de[word][0], "de"]

    elif word in dict_en:
        return [dict_en[word][0], "en"]

    else: 
        print("Word not found.")    