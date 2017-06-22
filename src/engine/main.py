'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

import pickle
import time

from engine.DocumentLoader import DocumentLoader
from engine.SearchEngine import SearchEngine


if __name__ == "__main__":
    doc_loader = DocumentLoader()
    
    print "Loading..."
    
    """
    # NOTE: Loading and parsing all files from folder
    start = time.time()
    doc_loader.iterate('../../html_files/')
    end = time.time()
    
    print "Loading and parsing time: " + str(end - start) + "s"
    
    # NOTE: Writting to file parsed data
    #pickle.dump(doc_loader.documents, open("../../documents.dat", "wb"))
    #pickle.dump(doc_loader.words, open("../../words.dat", "wb"))
    """
    
    # NOTE: Loading files with already parsed data
    doc_loader.words = pickle.load(open("../../words.dat", "rb"))
    doc_loader.documents = pickle.load(open("../../documents.dat", "rb"))
    
    search_engine = SearchEngine(doc_loader.words, doc_loader.documents)
    
    end = True
    while end:
        end = search_engine.start_search()
        search_engine.reset()
