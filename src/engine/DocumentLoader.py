'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''
import os

from engine.Document import Document
from engine.Word import Word
from engine.htmlFileParser import Parser


class DocumentLoader:
    def __init__(self):
        self.words = {}
        self.documents = {}
        self.parser = Parser()

    def add_words(self, word_list, doc_path):
        for word in word_list:
            word = word.lower()
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

    def add_links(self, file_path, links):
        self.documents[file_path] = Document(file_path, links, 0)

    def iterate(self, rootdir):
        for subdir, dirs, files in os.walk(rootdir):
            for f in files:
                file_path = os.path.join(subdir, f)
                
                if not file_path.endswith(".html"):
                    continue
                
                links, word_list = self.parser.parse(file_path)
                self.add_words(word_list, os.path.abspath(file_path))
                self.add_links(os.path.abspath(file_path), links)