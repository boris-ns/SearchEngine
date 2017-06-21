# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

import os
import pickle
import time

from engine.DocumentLoader import DocumentLoader
from engine.SearchEngine import SearchEngine


if __name__ == "__main__":
    doc_loader = DocumentLoader()
    
    print "Loading..."
    
    """
    # NAPOMENA: Ucitavanje i parsiranje svih fajlova
    start = time.time()
    doc_loader.iterate('../../html_files/')
    end = time.time()
    
    print "Vreme prolaska kroz fajlove: " + str(end - start) + "s"
    
    # NAPOMENA: Upis u fajl
    #pickle.dump(doc_loader.documents, open("../../documents.dat", "wb"))
    #pickle.dump(doc_loader.words, open("../../words.dat", "wb"))
    """
    # NAPOMENA: Fajlovi u kojima se vec nalaze isparsirani podaci
    doc_loader.words = pickle.load(open("../../words.dat", "rb"))
    doc_loader.documents = pickle.load(open("../../documents.dat", "rb"))
        
    search_engine = SearchEngine(doc_loader.words, doc_loader.documents)
    
    end = True
    while end:
        end = search_engine.start_search()
        search_engine.reset()
