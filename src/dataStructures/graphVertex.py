'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

class Vertex:

    def __init__(self, element):
        self._element = element
        
    def element(self):
        return self._element
    
    def __hash__(self):
        return hash(id(self))