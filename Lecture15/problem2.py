#!/bin/python3
#Convert any dna sequence into an amino acid sequence
#And provide all three reading frames (offset and forward/reverse)

#I need to start by establishing the library
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#Now here is the final function 
#The steps are provided below
def alltranscripts(dna):
    #Lets first make the compliment
    dna = dna.upper()
    compseq = ""
    for base in dna:
        if base == "A":
            compseq = compseq + "T"
        if base == "T":
            compseq = compseq + "A"
        if base == "C":
            compseq = compseq + "G"
        if base == "G":
            compseq = compseq + "C"
    #Now we go through and define the functions to
    #Generate the 3mer codon list
    def codongen(dna):
        kmerlist = []
        count = 0
        y = 0
        while y < len(dna):
            x = int(count * 1)
            y = int(x + 3)
            kmerlist.append(dna[x:y])
            count = count + 1
        return(kmerlist)
    def codongen2(dna):
        kmerlist = []
        count = 0
        y = 0
        dna = dna[1:]
        while y < len(dna):
            x = int(count * 1)
            y = int(x + 3)
            kmerlist.append(dna[x:y])
            count = count + 1
        return(kmerlist)
    def codongen3(dna):
        kmerlist = []
        count = 0
        y = 0
        dna = dna[2:]
        while y < len(dna):
            x = int(count * 1)
            y = int(x + 3)
            kmerlist.append(dna[x:y])
            count = count + 1
        return(kmerlist)
    #Call the function for each reading frame
    #And do it for the compliment
    codons1 = codongen(dna)
    codons2 = codongen2(dna)
    codons3 = codongen3(dna)
    revcodon1 = codongen(compseq)
    revcodon2 = codongen2(compseq)
    revcodon3 = codongen3(compseq)
    #Make a list with all the codon lists
    allframes = [codons1, codons2, codons3, revcodon1, revcodon2, revcodon3]
    #setup the counts and final output object
    framecount = 0
    allseqs = ""
    #For every codon frame in the list you add counter
    #And empty the aaseq
    for frame in allframes:
        framecount = framecount + 1
        aaseq = ""
        #Then you go through and assign the aa by codon
        for codon in frame:
            aaseq = aaseq + gencode[codon]
        allseqs = allseqs + "frame-" + str(framecount) + " " + aaseq + " "
    return(allseqs)

#Now we are outputting the sequences to user 
#First asking for sequence
dna = input("Enter dna sequence:")
#Now calling the function
allseqs = alltranscripts(dna)
#And splitting the outputs into a list
allseqlist = allseqs.split()
#Now making a range to pul only the sequences
#Could have been avoided by only returning seqs in function
#But this is good practice using a range
seqs = list(range(1,len(allseqlist),2))
#Set counter to 0 and make a list of the frame names
count = 0
frame = ['frame1','frame2','frame3','compliiment1','compliment2','compliment3']
#Now I am making a dictionary for these outputs 
#And putting the frame name and sequences into it 
seqdict = {}
for index in seqs:
    seqdict[frame[count]] = allseqlist[index]
    count = count + 1
#Lastly I am printing the sequences 
for frame, seq in seqdict.items():
    print(frame, seq)
