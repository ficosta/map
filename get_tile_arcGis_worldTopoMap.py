import urllib
import os

inicioX = 0
fimX=6
inicioY = 0
fimY=6
inicioZ = 1
fimZ=4
i=0

url='http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{2}/{1}/{0}'
folder='WorldTopoMap'

for z in range(1,11):
    for x in range(inicioX, (2**z) ):
        for y in range(inicioY, (2**z)):
            i+=1
            #urllib.urlretrieve ("http://a.osm.maptiles.xyz/{2}/{0}/{1}.png".format(x, y, z), '{0}_{1}_{2}.png'.format(x, y, z))
            if not os.path.isfile('{3}/{0}_{1}_{2}.png'.format(x, y, z, folder)):
                urllib.urlretrieve (url.format(x, y, z), '{3}/{0}_{1}_{2}.png'.format(x, y, z,folder))
                print(url.format(x, y, z))
                print('x={0} y={1} z={2}'.format(x, y, z))
            else:
                print('x={0} y={1} z={2} - existe'.format(x, y, z))

print(i)

# for z in range(1,4):
#     for x in range(inicioX, (2**z) - (fimX - inicioX) +1):
#         for y in range(inicioY, (2**z) - (fimY - inicioY)+1):
#             print('x={0} y={1} z={2}'.format(x, y, z))
