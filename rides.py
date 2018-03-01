from Ride.py import *
from vehicule.py import *

fichier = open("a_example.in", "r")
constants = fichier.readline().rstrip().split(' ')
rows = int(constants[0])
columns = int(constants[1])
nbVehic = int(constants[2])
nbRides = int(constants[3])
bonus = int(constants[4])
timeMax = int(constants[5])

listRides = []

for k in range(0, nbRides):
    listRides.append(Ride(map(lambda x: int(x), fichier.readline().rstrip().split(' ')), k))


vehicules = []
for k in range(0, nbVehic):
    vehicules.append(Vehicule())

#ici le code de l'algo

output = open("a_output.txt", "w")
for k in range(0, nbVehic):
    output.write(vehicules[k])