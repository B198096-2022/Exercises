DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
position = 0
count = 0
compliment = " "
while count <= len(DNA): 
    if DNA[position] == "A":
        compliment = compliment + "T"
        position = position + 1
    elif DNA[position] == "T":
        compliment = compliment + "T"
        position = position + 1
    elif DNA[position] == "C":
        compliment = compliment + "G"
        position = position + 1
    elif DNA[position] == "G":
        compliment = compliment + "C"
        position = position + 1
    count = count + 1

print(compliment)
