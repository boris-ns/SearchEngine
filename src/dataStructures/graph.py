'''
Created on Jun 19, 2017

@author: Boris Sulicenko
'''

class Graph:

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        
    def is_directed(self):
        return self._outgoing is not self._incoming
    
    def vertex_count(self):
        return len(self._outgoing)
        
    def vertices(self):
        return self._outgoing.keys()
    
    def edge_count(self):
        total = sum(len(self. outgoing[v]) for v in self. outgoing)
        return total if self.is_directed( ) else total // 2
    
    def edges(self):
        result = set()
        
        for tmp_map in self._outgoing.values():
            result.update(tmp_map.values())
            
        return result
    
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        adj = self. outgoing if outgoing else self. incoming
        for edge in adj[v].values( ):
            yield edge

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self. outgoing[v] = { }
        if self.is_directed( ):
            self. incoming[v] = { }
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e   
