from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Validator
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
#from .serializers import MovieSerializer
from .pagination import CustomPagination

#HY
from .validador_spam import validador
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes


class spam_ham_predict(APIView):
    def post(self, request, format=None):
        username = request.user.id
        texto = request.data['texto']
        print(username)
        q = Validator.objects.filter(creator=username)
        qu = q[0]
        if qu.resto > 0:
            response_dict = validador(texto, qu.resto)
            print(qu.resto, "Antes de restar")
            qu.resto -= 1 
            print(qu.resto)
            qu.save()
            m = Validator(texto= texto, predict= response_dict['result'], creator=request.user)
            m.save()
            return Response(response_dict, status=200)
        else:
            return Response({"status":"fail","message":"no quota left"})




@api_view(['GET'])
def history(request, N_EMAILS):
	username = request.user.id
	mails = Validator.objects.filter(creator=username).order_by('-created_at')[:int(N_EMAILS)]
	dic = []
	for m in mails:
		dic.append({"text":m.texto, "result":m.predict, "created_at":m.created_at})
	return Response(dic)