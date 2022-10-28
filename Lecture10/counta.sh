#!/usr/local/bin/python3
DNAs = ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
count = 0
while DNAs.find(`A') > 0
    count = count + 1
    aloc = DNAs.find(`A')
    DNAs = DNAs[loc:]
print("A count is" count)
