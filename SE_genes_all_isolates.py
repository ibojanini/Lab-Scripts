
import os #operative system

SE_gene_list=open("SE_gene_list.txt","w")
with open ('text_SE_gene_presence_absence.txt','r') as SE_file:
    # parse file =ir de linea en linea
    line_list = []
    newdictionary= {}
    numberofisolates={}
    dictofgenes={}
    for ticker, line in enumerate(SE_file):
        if ticker>0:
            line= line.strip('\n')
            line = line.split('\t') #to separate where there are TABS
            listofgenes=line[14:]
            numberofisolates[line[0]]=int(line[3])
            dictofgenes[line[0]]=listofgenes

            
    for gene,number in numberofisolates.items():
        if number <=6:
            newdictionary[gene]=number   
    genelist=[]
    #print(genelist)    
    for number,isolates in dictofgenes.items():
        for genename in isolates:
            #print(genename)
            if genename: #por cada item en la lista, : es si el item existe
                genelist.append(genename)
                break

gff_path = r"/clusterfs/vector/instrumentData/almeida/isabel/sepopulationwroot/" # make sure to put the 'r' in front
gff_filepaths  = [os.path.join(gff_path, name) for name in os.listdir(gff_path)]


genedict={}

for path in gff_filepaths:
    with open(path, 'r') as f:
        file = f.readlines()
        for line in file:
            nodesplit=line.split()
            for item in genelist:
                if item in line:
                    genedict[item]=[nodesplit[0],nodesplit[6], nodesplit[3], nodesplit[4]]
#print(genedict) #works so far
                
fasta_path = r"/clusterfs/vector/instrumentData/almeida/isabel/test_blast_fasta/" # make sure to put the 'r' in front
fasta_filepaths  = [os.path.join(fasta_path, name2) for name2 in os.listdir(fasta_path)]


for path2 in fasta_filepaths:
    with open(path2, 'r') as f2:
        file2 = f2.readlines()
        print(path2)
        
nodegenedict = {}
for genename in genedict:
    nodegenedict[genedict[genename][0]]=genename #we are defining what nodegenedict is.
    for path2 in fasta_filepaths:
        
        with open (path2,'r') as f2:
            sequencestring = '' 
                    
            currentkey=None
            previouskey=None
            
            for ticker, line in enumerate(f2):
                if '>' in line:
                    if currentkey:
                        
                        previouskey = currentkey
                        genedict[currentkey].append(sequencestring)
                       
                    switch = False
                    
                    linenode = line.split()[0][1:]
                    if linenode in nodegenedict: 
                        switch = True
                        currentkey = nodegenedict[linenode]
                if switch:
                    if '>' not in line: 
                        strippedline=line.strip()
                        sequencestring+= strippedline
                else: 
                    sequencestring = ''
                    currentkey = None
            if not previouskey and sequencestring:
                genedict[currentkey].append(sequencestring)
                    
##PARTE 3
constructdict = {}

reversecomplement=''
for nodesequence,key in genedict.items(): 
    endpos =   int(key[3])+1
    startpos = int(key[2])-1
    
    if startpos > 0 and endpos > 0:
        construct=key[4][startpos:endpos] 
    
    constructdict[nodesequence]=[construct]

for genenamex,sequence in constructdict.items():
    SE_gene_list.write(str(genenamex)+ ' ')
    #print(str(gene)+ ' ')
    SE_gene_list.write(str(sequence)+ '\n')
    #print(str(window)+ '\n')
SE_gene_list.close()

