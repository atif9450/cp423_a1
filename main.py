from q3_q4 import *
from real_a1 import construct_inverted_index
import pickle

#try to load inverted index and file names if already created; create and save otherwise
inverted_index = None
try:
    inverted_index = pickle.load(open('inverted_index.pickle', 'rb'))
    file_names = pickle.load(open('file_names.pickle', 'rb'))
except:
    inverted_index, file_names = construct_inverted_index('data/') 
    pickle.dump(inverted_index, open('inverted_index.pickle', 'wb'))
    pickle.dump(file_names, open('file_names.pickle', 'wb'))

"""FOE TESTING - PRINT KEYS SO WE KNOW WHAT TERMS WE CAN USE TO TEST"""
keys = list(inverted_index.keys())
print(keys[:15])

#get queries
num_queries = int(input("Enter number of queries: "))
print("Please enter input sentences as such: {x y z} where x,y,z are all lowercase words")
print('Please enter input operations as such: {x y z} where x,y,z could be any of {OR, AND, ORNOT, ANDNOT}')
queries = []
for i in range(num_queries):
    print('\nQuery {}'.format(i+1))
    sentence = input("Input sentence: ")
    operations = input("Input operations: ")
    operations = operations.split(' ')
    queries.append([sentence, operations])

for q in queries: #iterate through queries
    words = q[0].split(' ')
    operations = q[1]
    print('\nQuery:')
    print('Input sentence: {}'.format(words))
    print('Input operations: {}'.format(operations))

    docs = inverted_index[words[0]]
    comparisons = 0
    term_number = 1
    for o in operations: #perform operations as necessary
        term = words[term_number]
        term_number += 1
        if o == 'OR':
            docs, comparisons = OR(docs, term, inverted_index, comparisons)
        elif o == 'AND':
            docs, comparisons = AND(docs, term, inverted_index, comparisons)
        elif o == 'ANDNOT':
            docs, comparisons = AND_NOT(docs, term, inverted_index, comparisons)
        else:
            docs, comparisons = OR_NOT(docs, term, inverted_index, comparisons)

    #output results
    print("\nNumber of matched documents: {}".format(len(docs)))
    print("Minimum number of comparisons required: {}".format(comparisons))
    print('Document names:')
    for d in docs:
        print(file_names[d])