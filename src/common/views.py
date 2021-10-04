from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from common.authentication import JWTAuthentication
from common.models import ExtendedUser
from common.serializers.authorize_user import AuthorizeUser
from common.serializers.list_patient import ListPatient


class AuthorizationViewSet(ModelViewSet):
    serializer_class = AuthorizeUser
    permission_classes = ()
    http_method_names = ('post',)
    queryset = ExtendedUser.objects.all()


class PatientViewSet(ModelViewSet):
    """
    get patients or patient ID
    """
    serializer_class = ListPatient
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, )
    http_method_names = ('get',)
    queryset = ExtendedUser.objects.filter(is_doctor=False).order_by('-id')
