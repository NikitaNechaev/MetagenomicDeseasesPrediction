import csv

data = open('C:\\Gene\\Metagenomics\\HGMA\\data.csv', 'r')
bacts = open('C:\\Gene\\Metagenomics\\Code\\bact_data_filt.txt', 'r').readlines()
dlist = data.readlines()

for i in range(len(bacts)):
    bacts[i] = bacts[i][:-1]
    
for i in range(1, len(dlist)):
    if dlist[i][0] == ';':
        dlist[i] = f"{dlist[i-1].split(';')[0]}{dlist[i]}"
    if not (dlist[i-1].split(';')[0] in bacts):
        dlist[i-1] = ""
        
with open('C:\\Gene\\Metagenomics\\Code\\diseases_data_filt.txt', 'w') as f:
    for i in dlist:
        f.write(i)