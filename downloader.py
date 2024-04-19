import os
from Bio import SeqIO

bactList_file = open('C:\\Gene\\Metagenomics\\Code\\bact_data_filt.txt', 'r')
bactList = bactList_file.readlines()
for i in range(len(bactList)):
    bactList[i] = bactList[i][:-1]

for i in bactList:
    print(f"Running {i} - {bactList.index(i)} of {len(bactList)}")
    os.system(f"python       \\ncbi-genome-download-master\\ncbi-genome-download-runner.py --genera \"{i}\" bacteria")
    print(f"{round((bactList.index(i)/len(bactList))*100, 1)}% Completed\n")
    
    #123