import urllib
inicioX = 0
fimX=6
inicioY = 0
fimY=6
inicioZ = 1
fimZ=4
i=0
for z in range(1,4):
    for x in range(inicioX, (2**z) ):
        for y in range(inicioY, (2**z)):
            i+=1
            #urllib.urlretrieve ("http://a.osm.maptiles.xyz/{2}/{0}/{1}.png".format(x, y, z), '{0}_{1}_{2}.png'.format(x, y, z))
            urllib.urlretrieve ("http://c.tile.stamen.com/watercolor/${2}/${0}/${1}.jpg".format(x, y, z), 'WaterColor/{0}_{1}_{2}.png'.format(x, y, z))
            print('x={0} y={1} z={2}'.format(x, y, z))

print(i)

# for z in range(1,4):
#     for x in range(inicioX, (2**z) - (fimX - inicioX) +1):
#         for y in range(inicioY, (2**z) - (fimY - inicioY)+1):
#             print('x={0} y={1} z={2}'.format(x, y, z))
