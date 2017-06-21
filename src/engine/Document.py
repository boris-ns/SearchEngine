'''
Created on Jun 20, 2017

@author: Boris Sulicenko
'''

class Document:

    def __init__(self, path, links, score):
        self.path = path
        self.links = links
        self.score = score

    def __eq__(self, other):
        return self.score == other.score
    
    def __ne__(self, other):
        return not self.score == other.score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score