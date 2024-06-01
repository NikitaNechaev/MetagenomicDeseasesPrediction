import pandas as pd

data_stock = pd.read_csv('C:\Gene\Metagenomics\Code\out.csv', delimiter=';')

data = {''.join(str(data_stock['detection'][a]).split(' ')[1:3]): data_stock['prob'][a] for a in range(len(data_stock['detection']))}
print(data)
