DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
position = 0
compliment = " "
while position <= len(DNA): 
    if DNA[position] == "A":
        compliment = compliment + "T"
    elif DNA[position] == "T":
        compliment = compliment + "T"
    elif DNA[position] == "C":
        compliment = compliment + "G"
    elif DNA[position] == "G":
        compliment = compliment + "C"
    position = position
print(compliment)
