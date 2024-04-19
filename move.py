import os, shutil
dir = 'C:\\Gene\\Metagenomics\\Code\\refseq\\bacteria'
listdir = os.listdir(dir)
for i in listdir:
    for j in os.listdir(f"C:\\Gene\\Metagenomics\\Code\\refseq\\bacteria\\{i}"):
        print(f"move C:\\Gene\\Metagenomics\\Code\\refseq\\bacteria\\{i}\\{j}, C:\\Gene\\Metagenomics\\Code\\refseq_sum\\{j}")
        shutil.move(f"C:\\Gene\\Metagenomics\\Code\\refseq\\bacteria\\{i}\\{j}", f"C:\\Gene\\Metagenomics\\Code\\refseq_sum\\{j}")

