from copy import deepcopy

def OR(docs: list, term: str, inverted_index: dict, total_comparisons: int) -> (list, int):
    """
    Parameters:
        docs: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        docs: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    term_docs = inverted_index[term] #document list for term
    docs += term_docs #OR operation, union sets of documents
    
    #remove duplicates and sort
    docs = set(docs)
    docs = list(docs)
    docs.sort()
    
    return docs, total_comparisons

def AND(docs: list, term: str, inverted_index: dict, total_comparisons: int) -> (list, int):
    """
    Parameters:
        docs: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        docs: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    term_docs = inverted_index[term] #document list for term
    docs_pointer = 0 #pointer
    term_docs_pointer = 0 #pointer
    new_docs = [] #new list of documents
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] == term_docs[term_docs_pointer]: #append to new_docs using AND logic
            new_docs.append(docs[docs_pointer])
            docs_pointer += 1
            term_docs_pointer += 1
            total_comparisons += 1
        elif docs[docs_pointer] < term_docs[term_docs_pointer]: #increment docs_pointer
            docs_pointer += 1
            total_comparisons += 1
        else: #increment term_docs_pointer
            term_docs_pointer += 1
            total_comparisons += 1

    return new_docs, total_comparisons

def AND_NOT(docs: list, term: str, inverted_index: dict, total_comparisons: int) -> (list, int):
    """
    Parameters:
        docs: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        docs: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    term_docs = inverted_index[term] #document list for term
    term_docs_pointer = 0 #pointer
    docs_pointer = 0 #pointer
    new_docs = [] #new list of documents
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] != term_docs[term_docs_pointer]: #append to new_docs using NAND logic
            new_docs.append(docs[docs_pointer])
            total_comparisons += 1

            #increment pointers appropriately
            if docs[docs_pointer] < term_docs[term_docs_pointer]:
                docs_pointer += 1
            else:
                term_docs_pointer += 1

        else: #increment apprioprately
            docs_pointer += 1
            term_docs_pointer += 1
    
    return new_docs, total_comparisons

def OR_NOT(docs: list, term: str, inverted_index: dict, total_comparisons: int) -> (list, int):
    """
    Parameters:
        docs: current list of documents
        term: current term in query
        inverted_index: inverted index of terms/documents
        total_comparisons: total number of comparisons till now
    Returns:
        docs: updated list of documents
        total_comparisons: updated number of comparisons after query
    """
    return docs, total_comparisons