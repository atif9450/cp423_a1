#all the imports and downloads
import os
from nltk.tokenize import word_tokenize
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
import re

"""CAN WE DELETE LINES 11 TO 21?"""
#def doc_lower(file1, file2):
#    for line in file1:
#        line = line.lower()
#        file2.write(line)
#   return

#def doc_tok(file, list_tok):
#    for line in f:
#        fs = word_tokenize(line) 
#        list.append(fs)
#    return list

#function for replacing a files contents 
def fill(out, inp):
    for lines in inp:
        out.write(lines)
    return
def construct_inverted_index(path=""):
    #declaring all empty lists and counters
    dict = {}
    file_num = 0
    set_of_words = set()
    total_list = []
    file_names = []

    #path to folder with all the files
    folder = path

    #walking through every single file in the folder
    for root, dirs, files in os.walk(folder):

        #getting each file from folder 
        for name in files:
            docs_list_of_words = []
            f = open(path + name, "r+" , errors="ignore")
            f2 = open("text.txt","w")

            #lowers the files words and places it on another file
            for line in f:
                line = line.lower()
                f2.write(line)
            #doc_lower(f, f2)

            f.close()
            f2.close()

            f = open(path + name, "w",  errors="ignore")
            f2 = open("text.txt", "r")

            #replaces the original files uppercase words and the rest of words with lowercase from the other file
            fill(f,f2)
            f.close()
            f2.close()

            list = []
            f = open(path + name, "r+" )

            #tokenizing the words from the file
            for line in f:
                fs = word_tokenize(line) 
                #adding tokenized words to list
                list.append(fs)
            #doc_tok(f, list)
            f.close()

            #taking out each word from the tokenized list
            for word in list:
            
            #taking each letter from the tokenized word
                for letter in word:

                    #only takes the letters that are in the alphabet or numbers
                    only_alphnum = re.sub("[^A-Za-z0-9]","",letter)  

                    #makes sure the length of every word is more than 1
                    if (len(word) > 1):
                        if (only_alphnum in stopwords.words('english')):
                            f = 0
                        #only takes the words that are not stopwords
                        else:
                            docs_list_of_words.append(only_alphnum)

            #docs_list_of_words is added to total_list which is a total list of all words in all docsss
            total_list.extend(docs_list_of_words)

            #creating a set of words using total_list
            set_of_words.update(total_list)

            #gets words from the set of all words
            for dict_word_key in set_of_words:
                
                #creates a list called doc that is a value list for the key which in this case is a word
                docs = []

                #checks if the key (word) is in the dict 
                if dict_word_key not in dict:

                    #creates the key value pair to aviod future error
                    dict[dict_word_key] = [-1]
                
                #checks if the dictionary (dict) word is in the file
                if dict_word_key in docs_list_of_words:
                    
                    #extends the list of documents that have that word in the docs list
                    docs.extend(dict[dict_word_key])

                    #appending the file number/id into docs list
                    docs.append(file_num)

                    #removing the -1 if it was in docs list as it was originally put there to prevent an error
                    if docs[0] == -1:
                        docs.pop(0)

                    #adds the docs list as teh vale in the key value pair
                    dict[dict_word_key] = docs
            
            #creates a list of all the files names and the indices are the doc numbers/ids
            file_names.append(name)
            
            #ensures the doc numbers/indices are the same in file_names
            file_num +=1

    return dict, file_names 
