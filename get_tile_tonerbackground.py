import urllib
import os

inicioX = 0
fimX=6
inicioY = 0
fimY=6
inicioZ = 1
fimZ=4
i=0

url="http://stamen-tiles-a.a.ssl.fastly.net/toner-background/{2}/{0}/{1}.png"
folder='TonerBackground'

for z in range(1,9):
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
