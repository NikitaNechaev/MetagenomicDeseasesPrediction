import shutil, os

listdir = os.listdir('C:\\Gene\\Metagenomics\\Code\\refseq_fasta')

with open("C:\\Gene\\Metagenomics\\Code\\DB.fasta", "wb") as db:
    for i in range(len(listdir)):
        with open(f'C:\\Gene\\Metagenomics\\Code\\refseq_fasta\\{listdir[i]}', "rb") as fd:
            shutil.copyfileobj(fd, db)
            print(f"done {i} of {len(listdir)} | {round(i/len(listdir)*100, 1)}%")