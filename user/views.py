from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet, mixins
from . import models
from . import serializers
import logging

logger = logging.getLogger(__name__)

class SingUpViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = serializers.SignupSerializer
    queryset = models.User.objects.all()
    # def get_queryset(self):
    #     qs = models.User.objects.all()
    #     return qs


    def list(self, request, *args, **kwargs):
            # logger.error('Something went wrong!')
        # super(SingUpViewSet).create(self, request, *args, **kwargs):
        try:
            if sfdsafsadf:
                pass
        except:
            logger.error('Something went wrong!')

        return Response({"success": 1,"result": {}})

    def create(self, request, *args, **kwargs):
        if sfdsafsadf:
            logger.error('Something went wrong!')
        # super(SingUpViewSet).create(self, request, *args, **kwargs):


        return Response({"success": 1,"result": {}})