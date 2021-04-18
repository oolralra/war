import io

from django.utils import timezone
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet, mixins
from . import models
from . import serializers
import logging
from openpyxl import Workbook
import pandas as pd
import csv

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


class CsvUploadView(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.SignupSerializer

    def create(self, request, *args, **kwargs):
        data = request.FILES["file"]
        df = pd.read_csv(data, encoding='cp949')
        print(df)

        try:
            return Response({
                'success': 1,
                'message': '엑셀 업로드 성공'
            })
        except:
            return Response({
                'success': 0
            })

class CsvDownloadView(ListAPIView):

    def list(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = "attachment; filename={date}-delivery_information.xlsx".format(
            date=timezone.now().strftime("%Y-%m-%d"),
        )
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Delivery"

        # 컬럼명
        columns = [

        ]
        row_num = 1

        #  컬럼 헤더에 타이틀 설정
        for col_num, column_title in enumerate(columns, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title

        workbook.save(response)

        try:
            return Response({
                'success': 1,
                'message': '엑셀 업로드 성공'
            })
        except:
            return Response({
                'success': 0
            })
