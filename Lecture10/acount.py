DNAs = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
count = 0
aloc = DNAs.find('A')
while aloc>=0:
    count = count + 1
    rest = DNAs.find('A') + 1
    DNAs = DNAs[rest:]
    aloc = DNAs.find('A')
print(count)
