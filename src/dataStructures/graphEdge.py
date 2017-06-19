'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

class Edge:

    def __init__(self, origin, destination, element):
        self._origin = origin
        self._destination = destination
        self._element = element
    
    def endpoints(self):
        return (self._origin, self._destination)
        
    def opposite(self, v):
        return self._destination if v is self._origin else self._origin
        
    def element(self):
        return self._element
        
    def __hash__(self):
        return hash((self._origin, self._destination))