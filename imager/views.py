from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from imager.pagination import ImagerPagination
from imager.models import Imager
from imager.serializer import ImagerSerializer



class ImagerView(ListAPIView):
    query_set = Imager.objects.all()
    serializer_class = ImagerSerializer
    permission_classes = (IsAuthenticated,) 
    pagination_class = ImagerPagination

    def get(self,request, id = None):

        if id:
            imager = Imager.objects.filter(user=request.user,id=id)
            imagerSerializer = ImagerSerializer(imager,many=True)
            
            return Response(imagerSerializer.data,status=status.HTTP_200_OK)
            
        imager = self.paginate_queryset(Imager.objects.filter(user=request.user).order_by('-date','-time'))
        imagerSerializer = ImagerSerializer(imager,many=True)

        return self.get_paginated_response(imagerSerializer.data,)


    #Accept post request
    #Return id of upload
    def post(self,request, *args, **kwargs):
        postData = ImagerSerializer(
            data = request.data,
            context={
                'request': request
            }
        )
        postData.is_valid()
        postData.save()
        if postData.is_valid():
            p = postData.save()
            return Response({"id":p.id},status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class Logout(ListAPIView):
    permission_classes = (IsAuthenticated,) 
    def post(self, request, format=None):
        
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({"status":"success"},status=status.HTTP_200_OK)