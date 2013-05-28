'''
Created on May 27, 2013

@author: debanjan
'''
class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.key)+"Connected to:"+str([x.key for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.key
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numberOfVertices = 0
        
    
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        self.numberOfVertices += 1
        
    def addEdge(self, s, t, weight=0):
        if s not in self.vertexList:
            self.addVertex(s)
        if t not in self.vertexList:
            self.addVertex(t)
            
        self.vertexList[s].addNeighbor(self.vertexList[t],weight)
        
    def getVertex(self,key):
        if key in self.vertexList:
            return self.vertexList[key] 
        else:
            return None
        
    def __contains__(self,v):
        return v in self.vertexList
    
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())
            
            
            
g = Graph()
for i in range(10):
    g.addVertex(i)
print g.vertexList

g.addEdge(0,1,5)
g.addEdge(0,5,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1) 


for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))      