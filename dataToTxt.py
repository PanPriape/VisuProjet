import bpy

obdata = bpy.context.object.data

print('Vertices:')
for v in obdata.vertices:
    print('{}. {} {} {}'.format(v.index, v.co.x, v.co.y, v.co.z))

print('Edges:')
for e in obdata.edges:
    print('{}. {} {}'.format(e.index, e.vertices[0], e.vertices[1]))

/*
	bpy.data.objects['Cube']
*/