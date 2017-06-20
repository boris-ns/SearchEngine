'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''

class Word:
    def __init__(self, doc_path, number):
        self.doc_path = doc_path
        self.number = number

    def __eq__(self, other):
        return self.doc_path == other.doc_path

    def __ne__(self, other):
        return not self.doc_path == other.doc_path
    