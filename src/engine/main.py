# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

import os
import time
import pickle
from engine.htmlFileParser import Parser

class Word:
    def __init__(self, doc_path, number):
        self.doc_path = doc_path
        self.number = number

    def __eq__(self, other):
        return self.doc_path == other.doc_path

    def __ne__(self, other):
        return not self.doc_path == other.doc_path

class DocumentLoader:
    def __init__(self):
        self.words = {}
        self.links = {}
        self.parser = Parser()

    def add_words(self, word_list, doc_path):
        for word in word_list:
            try:
                self.words[word]
                flag = False # da li vec postoji putanja
                for w in self.words[word]:
                    if doc_path == w.doc_path:
                        flag = True
                
                if not flag:
                    self.words[word].append(Word(doc_path, word_list.count(word)))
                    
            except KeyError:
                self.words[word] = []
                self.words[word].append(Word(doc_path, word_list.count(word)))

    def iterate(self, rootdir):
        for subdir, dirs, files in os.walk(rootdir):
            for f in files:
                file_path = os.path.join(subdir, f)
                
                if not file_path.endswith(".html"):
                    continue
                
                links, word_list = self.parser.parse(file_path)
                self.add_words(word_list, file_path)
                # TODO: addlinks

if __name__ == "__main__":
    doc_loader = DocumentLoader()
    
    print "Loading..."
    
    #start = time.time()
    #doc_loader.iterate('../html_files/')
    #end = time.time()

    #pickle.dump(doc_loader.words, open("words.dat", "wb"))
    doc_loader.words = pickle.load(open("words.dat", "rb"))

    word_to_find = raw_input("Unesite rec za pretragu: ")

    #print "Vreme prolaska kroz fajlove: " + str(end - start)
    
    print "\nFajlovi u kojima se nalazi rec \"" + word_to_find + "\":\n"
    
    try:
        for f in doc_loader.words[word_to_find]:
            print f.doc_path + " number: " + str(f.number)
    
    except KeyError:
        print "Rec \"" + word_to_find + "\" se ne nalazi ni u jednom fajlu."
        
        
        
        