fichier = open("a_example.in", "r")
constants = fichier.readline().rstrip().split(' ')
rows = int(constants[0])
columns = int(constants[1])
nbVehic = int(constants[2])
nbRides = int(constants[3])
bonus = int(constants[4])
timeMax = int(constants[5])

for k in range(1, nbRides+1):
    ride = fichier.readline().rstrip().split(' ')