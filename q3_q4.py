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
    term_docs = inverted_index[term]
    docs += term_docs
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
    term_docs = inverted_index[term]
    docs_pointer = 0
    term_docs_pointer = 0
    add_docs = []
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] == term_docs[term_docs_pointer]:
            add_docs.append(docs[docs_pointer])
            total_comparisons += 1
        elif docs[docs_pointer] < term_docs[term_docs_pointer]:
            docs_pointer += 1
            total_comparisons += 1
        else:
            term_docs_pointer += 1
            total_comparisons += 1
    docs += add_docs
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
    term_docs = inverted_index[term]
    remove_docs = []
    term_docs_pointer = 0
    docs_pointer = 0
    while docs_pointer < len(docs) and term_docs_pointer < len(term_docs) and \
        docs[docs_pointer] <= max(term_docs) and term_docs[term_docs_pointer] <= max(docs):
        if docs[docs_pointer] == term_docs[term_docs_pointer]:
            remove_docs.append(docs[docs_pointer])
            total_comparisons += 1
        elif docs[docs_pointer] < term_docs[term_docs_pointer]:
            docs_pointer += 1
            total_comparisons += 1
        else:
            term_docs_pointer += 1
            total_comparisons += 1
    for r in remove_docs:
        docs.remove(r)
    docs.sort()
    docs = docs[::-1]
    return docs, total_comparisons