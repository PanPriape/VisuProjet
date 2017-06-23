from random import randint
import time
from tulip import *

class Projet(object):

	def __init__(self, graph):
		super(Projet, self).__init__()
		self.graph = graph
		self.blue = tlp.Color(0,0,255)
		self.red = tlp.Color(255,0,0)

	def importData(self, graph): 

		for n in self.graph.getNodes():
		    X = graph["coordX"][n]
		    Y = graph["coordY"][n]
		    Z = graph["coordZ"][n]
		    graph["viewLayout"][n] = tlp.Coord(X,Y,Z)
		    graph["viewSize"][n] = tlp.Size(0.001,0.001,0.001)
		    graph['NBPass'][n] = 0
		    graph['viewColor'][n] = self.blue
		
		for e in self.graph.getEdges():
			graph['viewColor'][e] = self.blue

	def propagationStep(self,node):
	
		graph['viewColor'][node] = self.red		
		graph['NBPass'][node] = graph['NBPass'][node] + 1
		
		for edge in self.graph.getOutEdges(node):
			graph['viewColor'][edge] = self.red
			graph['NBPass'][edge] = graph['NBPass'][edge] + 1
		
		updateVisualization()
		return [n for n in self.graph.getOutNodes(node)]
		
		
	def propagation(self,node,iter,time_sleep,debug):
		
		tmp_id = graph['id'][node]
		print "Propagation a partir de : "+str(tmp_id)
		if iter == 0:
			print "Propagation jusqu'a la fin"
		else:
			print "Propagation sur "+str(iter)+" iterations"
		print "Temps entre iteration : "+str(time_sleep)+" seconde(s)"
		print "Mode verbeux : "+str(debug)
		print "\n"
		
		list_node = []
		list_attente = []
		stop = True
		count = 0
		while stop:
			updateVisualization()
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
			
			
			# Pause pour visualiser la propagation
			time.sleep(time_sleep)
		
	def run(self):
		self.importData(graph)
		updateVisualization()
		
		print "Modele : OK"
		print "Debut propagation"
		print "\n"
		
		list_node = [node for node in self.graph.getNodes()]
		
		#index = randint(0,len(list_node)-1)
		index = 0
		self.propagation(list_node[index],0,1,True)
		
def main(graph):
	pr = Projet(graph)
	pr.run()
