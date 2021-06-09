from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet, mixins
from . import models
from . import serializers

class SingUpViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = serializers.SignupSerializer
    queryset = models.User.objects.all()
    # def get_queryset(self):
    #     qs = models.User.objects.all()
    #     return qs

    def create(self, request, *args, **kwargs):
        """
        배송관리 - 주문상품별 (완료)

        ### Parameter

            params : {
            }

        ### Response
            {
            }

        """
        # super(SingUpViewSet).create(self, request, *args, **kwargs):


        return Response({"success": 1,"result": {}})