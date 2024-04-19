from Bio import SeqIO

with open("C:\Gene\Metagenomics\Data\OQRU01.1.gbff", "r") as inp:
    with open("C:\Gene\Metagenomics\Data\OQRU01.1.fasta", "w") as out:
        seq = SeqIO.parse(inp, "genbank")
        count = SeqIO.write(seq, out, "fasta")
