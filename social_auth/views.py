from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer


class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        Send an google id_token to get an user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
