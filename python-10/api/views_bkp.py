from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np

@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        response = dict()
        response['solution'] = []
        try:
            questions_dict = request.data
            if questions_dict['question'] == []:
                response['solution'] = []
                return Response(response,status=status.HTTP_200_OK)
            if request.data == {}:
                return Response(response,status=status.HTTP_200_OK)

            questions = questions_dict['question']
            contagem = {}
            for question in questions:
                contagem[question] = contagem[question]+1

            question_serie = questions.value_counts()
            question_serie = question_serie.iloc[np.lexsort([-question_serie.index,-question_serie.values])]
            # Tenho a lista dos numeros e quantas vezes é necessário repetir
            soluction = []
            for number, qtd_repetitions in question_serie.iteritems():
                soluction += [number] * qtd_repetitions
            response["solution"] = soluction
        except Exception:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)
