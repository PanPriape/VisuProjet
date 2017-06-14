# -*- coding:utf-8 -*-

from random import randint
from tulip import *

class Projet(object):

	def __init__(self, graph):
		super(Projet, self).__init__()
		self.graph = graph
		self.blue = tlp.Color(0,0,255)
		self.red = tlp.Color(255,0,0)
		
	def newNode(self,size,color,position,name):
		node = self.graph.addNode()
		graph['viewSize'][node] = size
		graph['viewColor'][node] = color
		graph['viewLayout'][node] = position
		graph['Name'][node] = name
		graph['NBPass'][node] = 0
		
		return node

	def newEdge(self,depart,arrive,double,color):
	
		if(double):
			edge = self.graph.addEdge(arrive,depart)
			graph['viewColor'][edge] = color
			graph['NBPass'][edge] = 0
	
		edge = self.graph.addEdge(depart,arrive)
		graph['viewColor'][edge] = color
		graph['NBPass'][edge] = 0
		
		return edge
		
	def generationModel(self):

		# Entre du sang dans la main
		node0000 = self.newNode(tlp.Size(4,4,4),self.blue,tlp.Coord(0,0,0),"node0000")
		
		#Premier niveau de carrefour
		node0100 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(8,-8,0),"node0100")
		node0200 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(6,-14,0),"node0200")
		node0300 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(4,-25,0),"node0300")
		node0400 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(0,-30,0),"node0400")
		node0500 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(-4,-25,0),"node0500")
		node0600 = self.newNode(tlp.Size(3,3,3),self.blue,tlp.Coord(-8,-20,0),"node0600")
		
		self.newEdge(node0000,node0100,False,self.blue)
		self.newEdge(node0100,node0200,False,self.blue)
		self.newEdge(node0200,node0300,False,self.blue)
		self.newEdge(node0300,node0400,False,self.blue)
		self.newEdge(node0400,node0500,False,self.blue)
		self.newEdge(node0500,node0600,False,self.blue)
		self.newEdge(node0600,node0000,False,self.blue)
		
		#Deuxieme niveau de carrefour
		node0110 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(12,-10,0),"node0110")
		node0210 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(23,-40,0),"node0210")
		node0310 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(15,-45,0),"node0310")
		node0410 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(5,-48,0),"node0410")
		node0510 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-5,-50,0),"node0510")
		node0610 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-13,-23,0),"node0610")
		node0620 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-17,-33,0),"node0620")
		node0630 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-17,-48,0),"node0630")
		node0640 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-23,-46,0),"node0640")
		node0650 = self.newNode(tlp.Size(2,2,2),self.blue,tlp.Coord(-33,-38,0),"node0650")
		
		self.newEdge(node0100,node0110,False,self.blue)
		self.newEdge(node0200,node0210,False,self.blue)
		self.newEdge(node0300,node0310,True,self.blue)
		self.newEdge(node0400,node0410,True,self.blue)
		self.newEdge(node0500,node0510,True,self.blue)
		self.newEdge(node0600,node0610,True,self.blue)
		self.newEdge(node0610,node0620,True,self.blue)
		self.newEdge(node0650,node0610,False,self.blue)
		self.newEdge(node0630,node0620,False,self.blue)
		self.newEdge(node0620,node0640,False,self.blue)
		
		# Troisieme niveau de carrefour
		node0211 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(33,-58,0),"node0211")
		node0311 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(30,-59,0),"node0311")
		node0312 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(21,-68,0),"node0312")
		node0411 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(18,-69,0),"node0411")
		node0412 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(4,-78,0),"node0412")
		node0511 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(1,-78,0),"node0511")
		node0512 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(-15,-69,0),"node0512")
		node0631 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(-18,-68,0),"node0631")
		node0641 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(-35,-57,0),"node0641")
		node0651 = self.newNode(tlp.Size(1,1,1),self.blue,tlp.Coord(-39,-55,0),"node0651")
		
		
		self.newEdge(node0210,node0211,False,self.blue)
		self.newEdge(node0311,node0310,False,self.blue)
		self.newEdge(node0310,node0312,False,self.blue)
		self.newEdge(node0411,node0410,False,self.blue)
		self.newEdge(node0410,node0412,False,self.blue)
		self.newEdge(node0511,node0510,False,self.blue)
		self.newEdge(node0510,node0512,False,self.blue)
		self.newEdge(node0631,node0630,False,self.blue)
		self.newEdge(node0640,node0641,False,self.blue)
		self.newEdge(node0651,node0650,False,self.blue)
		
		# Relié les terminaisons
		self.newEdge(node0211,node0311,False,self.blue)
		self.newEdge(node0312,node0411,False,self.blue)
		self.newEdge(node0412,node0511,False,self.blue)
		self.newEdge(node0512,node0631,False,self.blue)
		self.newEdge(node0641,node0651,False,self.blue)

		
	def propagationStep(self,node):
	
		graph['viewColor'][node] = self.red		
		graph['NBPass'][node] = graph['NBPass'][node] + 1
		
		for edge in self.graph.getOutEdges(node):
			graph['viewColor'][edge] = self.red
			graph['NBPass'][edge] = graph['NBPass'][edge] + 1
		
		updateVisualization()
		return [n for n in self.graph.getOutNodes(node)]
		
		
	def propagation(self,node,iter,debug):
		
		list_node = []
		list_attente = []
		stop = True
		count = 0
		while stop:

			# Initialise la liste de propagation
			if len(list_node) == 0 and count == 0:
				list_node = self.propagationStep(node)
			
			for nodeStep in list_node:
				tmp_list = self.propagationStep(nodeStep)
				for tmp_node in tmp_list:
					list_attente.append(tmp_node)
			
			
			# Affiche les valeurs de debug
			if debug:
				print "Propagation tour : "+str(count)
				print "La prochaine propagation se fait sur les noeuds :"
				print list_attente
				print "\n"
			
			list_node = list_attente
			list_attente = []
					
			test = True
			for edge in self.graph.getEdges():
				if (graph['viewColor'][edge] == self.red):
					test = test and True
				else:
					test = False
			stop = not test
			
			count +=1
			if iter != 0 and count > iter:
				stop = False
		
	def run(self):
		self.graph.clear();
		self.generationModel()
		
		list_node = [node for node in self.graph.getNodes()]
		
		index = randint(0,len(list_node)-1)
		print graph['Name'][list_node[index]]
		
		self.propagation(list_node[index],2,True)
		
def main(graph):
	pr = Projet(graph)
	pr.run()
