'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''
import sys
from dataStructures.graph import Graph

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
        for d in self.words[word]:
            self.documents[d.doc_path].score += d.number / 2
            
    def check_if_word_exists(self, word):
        try:
            self.words[word]
        except KeyError:
            return False
            
        return True
    
    def print_docs_with_word(self, word):
        print "Br.dokumenata koji sadrzi trazenu rec: " + str(len(self.words[word]))
        
        list_docs = []
        for d in self.words[word]:
            list_docs.append(self.documents[d.doc_path])
            
        list_docs.sort(reverse=True)
        
        c = 1
        for d in list_docs[:10]:
            print "{:3} {:6}   {}".format("#" + str(c), d.score, d.path)
            c += 1
            
    def start_search(self):
        word_to_find = raw_input("Unesite rec za pretragu: ")
        word_to_find = word_to_find.lower()
        words_to_find = self.split_input(word_to_find)
        
    
        if not self.check_if_word_exists(word_to_find):
            print "Rec \"" + word_to_find + "\" se ne nalazi ni u jednom fajlu."
            sys.exit(0)

        print "\nFajlovi u kojima se nalazi rec \"" + word_to_find + "\":\n"
            
        self.add_word_count_to_score(word_to_find)
        graph = self.generate_graph(word_to_find)
        self.change_score_with_incoming_vertices(graph, word_to_find)
        self.print_docs_with_word(word_to_find)
        
    def split_input(self, word_to_find):
        words_to_find = word_to_find.split(",")
        for w in words_to_find:
            w = w.strip()
            
        return words_to_find
        
    def generate_graph(self, word_to_find):
        graph = Graph(directed=True)
        
        for doc in self.words[word_to_find]: # Dodavanje fajlova u kojima se nalazi trazena rec u graf
            graph.insert_vertex(self.documents[doc.doc_path])
            
        for doc in self.words[word_to_find]: 
            v1 = graph.is_vertex_in_graph(doc.doc_path)
            
            for link_path in self.documents[doc.doc_path].links:
                v2 = graph.is_vertex_in_graph(link_path)
                if v2 == None: # Nije u grafu
                    v2 = graph.insert_vertex(self.documents[doc.doc_path])
                    graph.insert_edge(v1, v2)
                else:
                    graph.insert_edge(v1, v2)
        '''
        print "Edges count " + str(graph.edge_count())
        print "Vertex count" + str(graph.vertex_count())
        print "Docs found " + str(len(self.words[word_to_find]))
        
        broj = 0
        for d in self.words[word_to_find]:
            broj += len(self.documents[d.doc_path].links)
            
        print "Link count " + str(broj)
        '''
        return graph
            
    def change_score_with_incoming_vertices(self, graph, word_to_find):
        for doc in self.words[word_to_find]:
            v1 = graph.is_vertex_in_graph(doc.doc_path)
            
            num_of_edges = 0
            num_of_words = 0
            for e in graph.incident_edges(v1, outgoing=False):
                num_of_edges += 1
                origin_vertex = e.endpoints()[0]
                
                num_of_words += self.find_word_count(origin_vertex, word_to_find)
            
            self.documents[doc.doc_path].score += num_of_edges
            self.documents[doc.doc_path].score += num_of_words
            
    def find_word_count(self, origin_vertex, word_to_find):
        c = 0
        for doc in self.words[word_to_find]:
            if origin_vertex.element().path == doc.doc_path:
                c += 1
                
        return c