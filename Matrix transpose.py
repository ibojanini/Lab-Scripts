

import pandas as pd
import numpy as np

data=pd.read_csv('CA_nov_gene_presence_absence.Rtab', sep='\t') 

data_transpose=data.transpose()
data_transpose.to_csv('2data_transpose_csv.csv')

with open ('2data_transpose_csv.csv','r') as gene_presence_absence_fasta:
    line_list = []
    for ticker, line in enumerate(gene_presence_absence_fasta):
        if ticker>1:
            line = line.replace(',', '') 
            line_split = line.split('_') 
            gene_name = '>{0}'.format('_'.join(line_split[:-1]))
            gene_name+='_{0}\n{1}'.format(line_split[-1][:2],line_split[-1][2:])
            line_list.append(gene_name)
            print(line_list)
            
    
fasta= open("CAfasta_file2.fasta", "w")
for line in line_list:
    fasta.write(str(line))
fasta.close





