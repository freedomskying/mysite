from django.http import JsonResponse
from django.views import generic
from rest_framework import status
from rest_framework.decorators import api_view

from .models import DwDowjRecordIndex
from .serializers import WatchlistSerializer, IdentifyResultSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'watchlist/index.html'
    context_object_name = 'record_list'

    def get_queryset(self):
        return DwDowjRecordIndex.objects.all()[0:200]


class DowjIdentifyView(APIView):

    def get(self, request, format=None):
        # records = DwDowjRecordIndex.objects.all()[0:4]
        # serializer = WatchlistSerializer(records, many=True)
        return Response('', status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        # 计算匹配结果，每一种匹配类型是一个占位符，
        # 0，不匹配
        # 1，完全匹配
        # 2，证件类型、证件号码匹配
        # 3，姓名、证件号码匹配
        # 4，姓名匹配
        # 5，证件号码匹配

        identify_json = {'return_code': '0', 'return_info': 'dowj jones black list identification successful!'}

        identify_dic = {'record_name': request.data.get('req_data').get('record_name', ''),
                        'id_value': request.data.get('req_data').get('id_value', ''),
                        'id_type': request.data.get('req_data').get('id_type', ''),
                        'result': 0}

        # 完全匹配情况
        if identify_dic['record_name'] != '' and identify_dic['id_type'] != '' and identify_dic['id_value'] != '':
            identity_result = DwDowjRecordIndex.objects.filter(record_name=identify_dic['record_name']).filter(
                id_type=identify_dic['id_type']).filter(id_value=identify_dic['id_value'])
            if len(identity_result) > 0:
                identify_dic['result'] = 1
        else:

            # 证件类型、证件号码匹配
            if identify_dic['id_type'] != '' and identify_dic['id_value'] != '':
                identity_result = DwDowjRecordIndex.objects.filter(id_type=identify_dic['id_type']).filter(
                    id_value=identify_dic['id_value'])
                if len(identity_result) > 0:
                    identify_dic['result'] = identify_dic['result'] + 10

            # 姓名、证件号码匹配
            if identify_dic['record_name'] != '' and identify_dic['id_value'] != '':
                identity_result = DwDowjRecordIndex.objects.filter(record_name=identify_dic['record_name']).filter(
                    id_type=identify_dic['id_type']).filter(id_value=identify_dic['id_value'])
                if len(identity_result) > 0:
                    identify_dic['result'] = identify_dic['result'] + 100

        identify_json['rsp_data'] = identify_dic
        print(identify_json)

        serializer = IdentifyResultSerializer(data=identify_json)

        if serializer.is_valid():
            print(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
