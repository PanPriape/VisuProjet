"""

	Script python permettant de traiter les données de l'objet 3D créer

"""

"""
  Acquisition des données utilisées pour modéliser le graphe dans tulip. On doit récupérer la positions de tout les noeuds ainsi que les arretes qui les lient.

"""
### Export des données dans le fichier texte 3DSanguin.txt.

import bpy

# obdata contient les données de notre object "Graphe_Art" représentant le flux sanguin
obdata = bpy.data.objects['Graphe_Art'].data

# on ouvre le fichier texte
f=open('/Users/Farfadet/Desktop/Cours - UQAC/trimestre - Ete/Visualisation/projet/blend/3DSanguin.txt','w')

# permet d'écrire tout les vertices/noeuds de l'objet 3D. Format : 'indexVertice, coordonnéeEnX, coordonnéeEnY, coordonnéeEnZ'
f.write('Vertices :\n')
for v in obdata.vertices:
    f.write('%s %s %s %s\n' % (v.index,v.co[0],v.co[1],v.co[2]))

# permet d'écrire tout les Edges/arretes de l'objet 3D. Format : 'indexEdge, indexVertice1, indexVertice2'
f.write('Edges :\n')
for e in obdata.edges:
    f.write('%s %s %s\n' % (e.index, e.vertices[0], e.vertices[1]))

# fermeture du fichier texte
f.close()

### Affichage des données dans la console python de Blender.

# obdata contient les données de notre object "Graphe_Art" représentant le flux sanguin
obdata = bpy.data.objects['Graphe_Art'].data

# permet d'afficher tout les vertices/noeuds de l'objet 3D. Format : 'indexVertice, coordonnéeEnX, coordonnéeEnY, coordonnéeEnZ'
print('Vertices :\n')
for v in obdata.vertices:
    print('{}. {} {} {}'.format(v.index, v.co.x, v.co.y, v.co.z)) 

# permet d'afficher tout les Edges/arretes de l'objet 3D. Format : 'indexEdge, indexVertice1, indexVertice2'
print('Edges :\n')
for e in obdata.edges:
    print('{}. {} {}'.format(e.index, e.vertices[0], e.vertices[1]))

"""
  Code permettant d'inverser le sens/la direction d'une arrete.

"""

obdata = bpy.data.objects['Graphe_Art'].data

for e in obdata.edges:
    if(e.index == 255):
        vtmp = e.vertices[0]
        e.vertices[0] = e.vertices[1]
        e.vertices[1] = vtmp


"""
  Code permettant de récupérer l'index des vertices/noeuds sélectionnés dans Blender(mode Edition).
  On l'utilise pour connaître l'index des noeuds représentant les capillaires sanguins; noeuds de transition
  entre les artères et les veines.

"""

selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
for v in selectedVerts:
    print(v.index)

