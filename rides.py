from Ride import *
from vehicule import *

"""
Lecture fichier
"""

fichier = open("a_example.in", "r")
constants = fichier.readline().rstrip().split(' ')
rows = int(constants[0])
columns = int(constants[1])
nbVehic = int(constants[2])
nbRides = int(constants[3])
bonus = int(constants[4])
timeMax = int(constants[5])

listRides = []
ridesToDo =[]

for k in range(0, nbRides):
    listRides.append(Ride(list(map(lambda x: int(x), fichier.readline().rstrip().split(' '))), k))
    ridesToDo.append(Ride(list(map(lambda x: int(x), fichier.readline().rstrip().split(' '))), k))
fichier.close()

vehicules = []
for k in range(0, nbVehic):
    vehicules.append(Vehicule())

"""
Ici le coeur de l'algo
"""

listRides.sort(key=lambda x: x.earlyStart)

"""
Ecriture du fichier d'output
"""

output = open("a_output.txt", "w")

for k in range(0, nbVehic):
    l = str(len(vehicules[k].rides_done))
    for id_ in vehicules[k].rides_done:
        l += " " + str(id_)
    output.write(l)

output.close()

"""
Calcul du score
"""

score = 0

for v in vehicules:
    rides_done = v.rides_done
    t = 0
    x, y = 0, 0
    
    for id_ in rides_done:
        score += listRides[id_].time
        x_, y_ = listRides[id_].posStart
        
        if(t + abs(x - x_) + abs(y - y_) <= listRides[id_].earlyStart):
            score += bonus
            t = listRides[id_].earlyStart + listRides[id_].time
        else:
            t = t + abs(x - x_) + abs(y - y_) + listRides[id_].time

print(score)




