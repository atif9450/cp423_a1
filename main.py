from q3_q4 import *
from real_a1 import construct_inverted_index
import pickle

#try to load inverted index if already created; create and save otherwise
inverted_index = None
try:
    inverted_index = pickle.load(open('inverted_index.pickle', 'rb'))
except:
    inverted_index, file_names = construct_inverted_index('data/') #construct unverted index
    pickle.dump(inverted_index, open('inverted_index.pickle', 'wb')) #save index so we don't have to make it every time (save computation time/resources)

"""FOE TESTING - PRINT 10 KEYS SO WE KNOW WHAT TERMS WE CAN USE TO TEST"""
keys = list(inverted_index.keys())
print(keys[:10])
print()

#get queries
num_queries = int(input("Enter number of queries: "))
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
    print(docs)