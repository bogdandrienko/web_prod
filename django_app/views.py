from django.contrib.auth.models import User
from django.core.cache import caches
from django.views.generic import TemplateView
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import serializers as django_app_serializers, utils as django_app_utils
import openpyxl

RedisCache = caches["default"]


def func1():
    workbook: Workbook = openpyxl.Workbook()
    worksheet: Worksheet = workbook["Лист1"]

    dataa1: int = worksheet.cell(1, 1).value  # 'Sholpan'
    dataa1.split()


class HomeView(TemplateView):
    template_name = "index.html"


@django_app_utils.logging(log_response=True)
@api_view(http_method_names=["GET"])
def users_f(request: Request, pk: int) -> Response:
    """
    Чтение выбранного пользователя
    """
    try:
        usr_json = RedisCache.get(f"{request.path} {request.method} {pk}")
        if usr_json is None:
            usr_obj = User.objects.get(id=pk)
            usr_json = django_app_serializers.UserSerializer(instance=usr_obj, many=False)
            RedisCache.set(f"{request.path} {request.method} {pk}", usr_json, 3)
        return Response(data=usr_json.data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(data=str(error), status=status.HTTP_400_BAD_REQUEST)
