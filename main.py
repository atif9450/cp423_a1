from q3_q4 import *
from real_a1 import *
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
    
    #apply preprocessing
    sentence = preprocess_sentence(sentence)
    sentence = sentence.split(' ')
    operations = operations.split(' ')

    queries.append([sentence, operations]) #add query

cost_dict = {} #for keeping track of query costs
pqueries = [] #list for prioritized queries
for q in queries:
    words = q[0]
    ops = q[1]
    for i in range(len(ops)): #calculate costs for different queries and construct cost_dict
        op_words = [words[i], words[i+1]]
        cost = query_cost(op_words, ops[i], inverted_index)
        cost_dict.update({i: [op_words, ops[i], cost]})

    cost_dict = dict(sorted(cost_dict.items(), key=lambda item: item[1][2])) #sort cost_dict in order of ascending document frequency
    pqueries.append(prioritize_query(cost_dict)) #construct list of priotized queries

for q in pqueries: #iterate through queries
    words = q[0]
    operations = q[1]

    #display current query
    print('\nQuery:')
    print('Input sentence: {}'.format(words))
    print('Input operations: {}'.format(operations))

    left = inverted_index[words[0]]
    word_pointer = 1
    comparisons = 0
    for o in operations: #iterate through the operations in the query
        right = inverted_index[words[word_pointer]]
        word_pointer += 1

        if o == 'OR':
            left, comparisons = OR(left, right, comparisons)
        elif o == 'AND':
            left, comparisons = AND(left, right, comparisons)
        elif o == 'ANDNOT':
            left, comparisons = AND_NOT(left, right, comparisons)
        else:
            left, comparisons = OR_NOT(left, right, comparisons)

    #output results
    print("\nNumber of matched documents: {}".format(len(left)))
    print("Minimum number of comparisons required: {}".format(comparisons))
    print('Document names:')
    for l in left:
      print(file_names[l])
