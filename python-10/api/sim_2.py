import pandas as pd
import numpy as np
# Create your tests here.
resposta = [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]
listquestion = [2, 2, 2, 3, 3, 3, 3, 5, 5, 12, 12, 4]
#ordenation = pd.Series(listquestion).value_counts(
#).sort_values(axis=0, ascending=False).sort_index(level=1, sort_remaining=False)
contagem = {}
for question in listquestion:
    contagem[question] = (1 if contagem.get(question) is None else contagem[question]+1) 
sort_orders = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
soluction = []
for item, qtd in sort_orders:
    soluction += [item] * qtd

print(soluction)
