from parser import Parser
import os

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

    def iterate(self):
        parser = Parser()
        
        rootdir = 'html_files/'

        for subdir, dirs, files in os.walk(rootdir):
            for f in files:
                file_path = os.path.join(subdir, f)
                links, word_list = parser.parse(file_path)
                #addlinks
                self.add_words(word_list, file_path)

if __name__ == "__main__":
    doc_loader = DocumentLoader()
    
    start = time.time()
    doc_loader.iterate()
    end = time.time()

    word_to_find = raw_input("Unesite rec za pretragu: ")

    print "\n\n"
    print "Vreme prolaska kroz fajlove: " + str(end - start)
    print len(doc_loader.words[word_to_find])
    
    print "\nFajlovi u kojima se nalazi rec \"" + word_to_find + "\"\n"
    for f in doc_loader.words[word_to_find]:
        print f.doc_path + " number: " + str(f.number)