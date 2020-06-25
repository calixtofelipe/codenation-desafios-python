import pandas as pd
import numpy as np
# Create your tests here.
listquestion = [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]
#ordenation = pd.Series(listquestion).value_counts(
#).sort_values(axis=0, ascending=False).sort_index(level=1, sort_remaining=False)
request_vazio = dict({})
request_semitens = dict({})
request_semitens['question'] = None
question_serie = pd.Series(listquestion)
question_serie = question_serie.value_counts()
question_serie = question_serie.iloc[np.lexsort([-question_serie.index,-question_serie.values])]

print("question_serie: ", question_serie)
print("question_serie - values: ",question_serie.values)
soluction = []
for number, qtd_repetitions in question_serie.iteritems():
    soluction += [number] * qtd_repetitions

response = dict({})
response['solution']="null"
print('response-vazio',response)
response['solution'] = soluction
print(response)
print(request_vazio == {})
print(request_semitens['question'] == None)
