import os, gzip, shutil
from Bio import SeqIO

listdir = os.listdir('C:\\Gene\\Metagenomics\\Code\\refseq_sum')

for i in range(3390, len(listdir)):
    try:
        with gzip.open(f'C:\\Gene\\Metagenomics\\Code\\refseq_sum\\{listdir[i]}', 'rb') as f_in:
            with open(f'C:\\Gene\\Metagenomics\\Code\\refseq_unzipped\\{listdir[i][:-2]}', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                

        with open(f'C:\\Gene\\Metagenomics\\Code\\refseq_unzipped\\{listdir[i][:-2]}', "r") as input_handle:
            with open(f'C:\\Gene\\Metagenomics\\Code\\refseq_fasta\\{listdir[i][:-7]}fasta', "w") as output_handle:
                sequences = SeqIO.parse(input_handle, "genbank")
                count = SeqIO.write(sequences, output_handle, "fasta")
                print(f"done {i} from {len(listdir)} | {round(i/len(listdir)*100, 1)}%")
    except EOFError:
        print(f"{i} - ERROR")