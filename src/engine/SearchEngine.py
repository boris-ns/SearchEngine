'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''
import sys

class SearchEngine:

    def __init__(self, words, documents):
        self.words = words
        self.documents = documents
        
        self.prepare_doc_scores()
        
    def prepare_doc_scores(self):
        # Smanjuje skor svakog dokumenta za broj linkova koje sadrzi
        for key, value in self.documents.iteritems():
            value.score -= len(value.links)
            #print str(key) + " SCORE : " + str(value.score)
            
    def add_word_count_to_score(self, word):
        # Povecava skor svakog dokumenta za broj ponavljanja trazene reci
        for key, value in self.documents.iteritems():
            for d in self.words[word]:
                if key == d.doc_path:
                    value.score += d.number
            
    def check_if_word_exists(self, word):
        try:
            self.words[word]
        except KeyError:
            return False
            
        return True
    
    def print_docs_with_word(self, word):
        print "Br.dokumenata koji sadrzi trazenu rec: " + str(len(self.words[word]))
        for d in self.words[word]:
            print d.doc_path + " number: " + str(d.number) + " score: " + str(self.documents[d.doc_path].score)
            
    def start_search(self):
        word_to_find = raw_input("Unesite rec za pretragu: ")
        print "\nFajlovi u kojima se nalazi rec \"" + word_to_find + "\":\n"
    
        if not self.check_if_word_exists(word_to_find):
            print "Rec \"" + word_to_find + "\" se ne nalazi ni u jednom fajlu."
            sys.exit(0)
            
        self.add_word_count_to_score(word_to_find)
        self.print_docs_with_word(word_to_find)        
    