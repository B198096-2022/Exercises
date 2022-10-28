DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
DNAs = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
acount = 0
aloc = DNAs.find('A')
while aloc>=0:
    acount = acount + 1
    rest = DNAs.find('A') + 1
    DNAs = DNAs[rest:]
    aloc = DNAs.find('A')
print("A count is"acount)


DNAs = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
tcount = 0
tloc = DNAs.find('T')
while tloc>=0:
    tcount = tcount + 1
    rest = DNAs.find('T') + 1
    DNAs = DNAs[rest:]
    tloc = DNAs.find('T')
print("T count is"tcount)

AT = acount + tcount
ATratio = AT/DNA.len()
print(AT)
print(ATratio)
