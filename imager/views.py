from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


from imager.serializer import ImagerSerializer


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



class ImagerView(APIView):
    serializer_class = ImagerSerializer

    #Accept post request
    #Return id of upload
    def post(self,request, *args, **kwargs):
        data = request.data
        print(request.user)
        data['user'] = request.user
        postData = ImagerSerializer(data = request.data)
        
        if postData.is_valid():
            p = postData.save()
            return Response({"id":p.id},status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (IsAuthenticated,) 
    def post(self, request, format=None):
        
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({"status":"success"},status=status.HTTP_200_OK)