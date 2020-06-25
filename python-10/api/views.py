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
                contagem[question] = (1 if contagem.get(question) is None else contagem[question]+1) 
            sort_orders = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
            
            soluction = []
            for item, qtd in sort_orders:
                soluction += [item] * qtd
                
            response["solution"] = soluction
        except Exception:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)
