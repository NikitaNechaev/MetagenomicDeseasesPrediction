import json
filename = "C:\\Users\\user\\Downloads\\TBJ2ACSS01N-Alignment.json"
outfile = "C:\\Gene\\Metagenomics\\Code\\out.txt"
of = open(outfile, 'w')
total = {}
with open(filename, "rt") as f:
    result = json.loads(f.read(),)
for i, rep in enumerate(result.get('BlastOutput2')):
    hits = rep.get('report').get('results').get('search').get('hits')
    for hit in hits:
        desc = hit.get('description')[0].get('sciname')
        ev = hit.get('hsps')[0].get('evalue')
        if (i not in total) or (total[i].get('ev') > ev):
            total[i] = {'desc': desc, 'ev': ev}
for e in total:
    of.write(f"In [{e}]: {total[e]=}\n")
    print(f"In [{e}]: {total[e]=}")