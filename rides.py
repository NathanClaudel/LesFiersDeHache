fichier = open("a_example.in", "r")
constants = fichier.readline().rstrip().split(' ')
rows = constants[0]
columns = constants[1]
nbVehic = constants[2]
nbRides = constants[3]
bonus = constants[4]
timeMax = constants[5]

for k in range(1, nbRides+1):
    ride = fichier.readline().rstrip().split(' ')


