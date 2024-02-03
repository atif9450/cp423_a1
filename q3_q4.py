from copy import deepcopy

def OR(left: list, right: list, total_comparisons: int) -> (list, int):
    """
    Parameters:
        left: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        left: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    left += right #OR operation, union sets of documents
    
    #remove duplicates and sort
    left = set(left)
    left = list(left)
    left.sort()
    
    return left, total_comparisons

def AND(left: list, right: list, total_comparisons: int) -> (list, int):
    """
    Parameters:
        left: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        left: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    left_pointer = 0 #pointer
    right_pointer = 0 #pointer
    new_docs = [] #new list of documents
    while left_pointer < len(left) and right_pointer < len(right) and \
        left[left_pointer] <= max(right) and right[right_pointer] <= max(left):
        if left[left_pointer] == right[right_pointer]: #append to new_docs using AND logic
            new_docs.append(left[left_pointer])
            left_pointer += 1
            right_pointer += 1
            total_comparisons += 1
        elif left[left_pointer] < right[right_pointer]: #increment left_pointer
            left_pointer += 1
            total_comparisons += 1
        else: #increment right_pointer
            right_pointer += 1
            total_comparisons += 1

    return new_docs, total_comparisons

def AND_NOT(left: list, right: list, total_comparisons: int) -> (list, int):
    """
    Parameters:
        left: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        left: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    right_pointer = 0 #pointer
    left_pointer = 0 #pointer
    new_docs = [] #new list of documents
    while left_pointer < len(left) and right_pointer < len(right) and \
        left[left_pointer] <= max(right) and right[right_pointer] <= max(left):
        if left[left_pointer] != right[right_pointer]: #append to new_docs using NAND logic
            new_docs.append(left[left_pointer])
            total_comparisons += 1

            #increment pointers appropriately
            if left[left_pointer] < right[right_pointer]:
                left_pointer += 1
            else:
                right_pointer += 1

        else: #increment apprioprately
            left_pointer += 1
            right_pointer += 1
    
    return new_docs, total_comparisons

def OR_NOT(left: list, right: list, total_comparisons: int) -> (list, int):
    """
    Parameters:
        left: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        left: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    return left, total_comparisons

def query_cost(words: list, operation: list, inverted_index: dict) -> list:
    left = inverted_index[words[0]]
    right = inverted_index[words[1]]
    if operation == 'OR':
        return len(left) + len(right)
    elif operation == 'AND':
        return min(len(left), len(right))
    elif operation == 'ANDNOT':
        return max(len(left), len(right))
    else:
        return len(left)
    
def prioritize_query(cost_dict: dict) -> (list, list):
    print(cost_dict)
    words = []
    operations = []
    one = True
    for k in cost_dict.keys():
        key_words = cost_dict[k][0]
        for kw in key_words:
            if kw not in words:
                words.append(kw)
        operations.append(cost_dict[k][1])
    return words, operations