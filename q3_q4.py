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
    
    #sort updated list of documents
    docs.sort()
    docs = docs[::-1]
    
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
    add_docs = [] #documents to add
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] == term_docs[term_docs_pointer]: #if found match, append to add_docs
            add_docs.append(docs[docs_pointer])
            docs_pointer += 1
            term_docs_pointer += 1
            total_comparisons += 1
        elif docs[docs_pointer] < term_docs[term_docs_pointer]: #increment docs_pointer
            docs_pointer += 1
            total_comparisons += 1
        else: #increment term_docs_pointer
            term_docs_pointer += 1
            total_comparisons += 1
    docs += add_docs #add matching documents

    #sort updated list of documents
    docs.sort()
    docs = docs[::-1]

    return docs, total_comparisons

def NOT(docs: list, term: str, inverted_index: dict, total_comparisons: int) -> (list, int):
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
    remove_docs = [] #documents to remove
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] == term_docs[term_docs_pointer]: #if found match, append to remove_docs
            remove_docs.append(docs[docs_pointer])
            docs_pointer += 1
            term_docs_pointer += 1
            total_comparisons += 1
        elif docs[docs_pointer] < term_docs[term_docs_pointer]: #increment docs_pointer as necessary
            docs_pointer += 1
            total_comparisons += 1
        else: #increment term_docs_pointer as necessary
            term_docs_pointer += 1
            total_comparisons += 1
    
    #remove matching documents
    for r in remove_docs:
        docs.remove(r)
    
    #sort updated list of documents
    docs.sort()
    docs = docs[::-1]
    
    return docs, total_comparisons