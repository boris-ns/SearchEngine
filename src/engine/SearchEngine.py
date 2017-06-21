'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''
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
            
    def add_word_count_to_score(self, word):
        # Povecava skor svakog dokumenta za broj ponavljanja trazene reci
        for d in self.words[word.strip()]:
            self.documents[d.doc_path].score += d.number
            
    def check_if_word_exists(self, words):
        try:
            for w in words:
                self.words[w.strip()]
        except KeyError:
            return False
            
        return True
    
    def print_docs_with_word(self, docs):
        print "Br.dokumenata koji sadrzi trazene reci: " + str(len(docs))
        
        docs_to_print = []
        for d in docs:
            docs_to_print.append(self.documents[d.doc_path])
            
        docs_to_print.sort(reverse=True)
        
        c = 1
        for d in docs_to_print[:10]:
            print "{:3} {:6}   {}".format("#" + str(c), d.score, d.path)
            c += 1
            
    def start_search(self):
        word_to_find = raw_input("\nUnesite rec za pretragu: ")
        word_to_find = word_to_find.lower()
        words_to_find = self.split_input(word_to_find)
        
        if word_to_find == "q":
            return False
    
        if not self.check_if_word_exists(words_to_find):
            print "Ne postoji ni 1 fajl sa unetim recima."
            return True

        print "\nRezultat pretrage:\n"
        
        all_docs = []
        for w in words_to_find:
            self.add_word_count_to_score(w.strip())
            for doc in self.words[w.strip()]:
                all_docs.append(doc)
        
        docs = []
        for d in all_docs:
            if len(words_to_find) != 1 and all_docs.count(d) == 1:
                continue
            else:
                if not d in docs:
                    docs.append(d)

        graph = self.generate_graph(docs)
        self.change_score_with_incoming_vertices(graph, docs)
        self.print_docs_with_word(docs)
        
        return True
        
    def reset(self):
        for key, value in self.documents.iteritems():
            value.score = 0 - len(value.links)
        
    def split_input(self, word_to_find):
        words_to_find = word_to_find.split(",")
        return words_to_find
        
    def generate_graph(self, docs_to_search):
        graph = Graph(directed=True)
        
        for doc in docs_to_search: # Dodavanje fajlova u kojima se nalazi trazena rec u graf
            graph.insert_vertex(self.documents[doc.doc_path])
            
        for doc in docs_to_search:
            v1 = graph.is_vertex_in_graph(doc.doc_path)
                
            for link_path in self.documents[doc.doc_path].links:
                v2 = graph.is_vertex_in_graph(link_path)
                if v2 == None: # Nije u grafu
                    v2 = graph.insert_vertex(self.documents[doc.doc_path])
                    graph.insert_edge(v1, v2)
                else:
                    graph.insert_edge(v1, v2)

        #print "Edges count " + str(graph.edge_count())
        #print "Vertex count " + str(graph.vertex_count())
        #print "Docs found " + str(len(docs_to_search))
        
        return graph
            
    def change_score_with_incoming_vertices(self, graph, docs_to_search):
        for doc in docs_to_search:
            v1 = graph.is_vertex_in_graph(doc.doc_path)
                
            num_of_edges = 0
            num_of_words = 0
            for e in graph.incident_edges(v1, outgoing=False):
                num_of_edges += 1
                origin_vertex = e.endpoints()[0]
                    
                num_of_words += self.find_word_count(origin_vertex, doc.word)
                
            self.documents[doc.doc_path].score += num_of_edges
            self.documents[doc.doc_path].score += num_of_words
            
    def find_word_count(self, origin_vertex, word_to_find):
        c = 0
        for doc in self.words[word_to_find]:
            if origin_vertex.element().path == doc.doc_path:
                c += 1
                
        return c