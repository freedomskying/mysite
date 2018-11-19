from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from django.contrib import auth
import datetime
import time

# from silk.profiling.profiler import silk_profile

from .models import *
from .serializers import IdentifyResultSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

import logging.handlers

logger = logging.getLogger(__name__)


def audit_log_insert(user_id, username, oper_type, oper_memo):
    al = DwDowjAuditLog()
    al.user_id = user_id
    al.username = username
    al.oper_type = oper_type
    al.oper_memo = oper_memo
    al.save()

    return True


# Create your views here.

@login_required
def record_result(request):
    record_name = request.POST['record_name']
    id_type = request.POST['id_type']
    id_value = request.POST['id_value']

    logger.info('[INFO] WATCHLIST LOG : User [' + auth.get_user(
        request).username + '] query person watchlist, name = [' + record_name + '] id_type = [' + id_type + '] id_value = [' + id_value + ']')

    if record_name == '' and id_type == '' and id_value == '':
        record_list = ''
    else:

        record_filter = DwDowjRecordIndex.objects.all()

        if record_name != '':
            record_filter = record_filter.filter(record_name=record_name)

        if id_type != '':
            record_filter = record_filter.filter(id_type=id_type)

        if id_value != '':
            record_filter = record_filter.filter(id_value=id_value)

        record_list = record_filter

        audit_log_insert(auth.get_user(request).id, auth.get_user(request).username, '黑名单个人查询',
                         '客户名称=[' + record_name + '] , 证件类型 = [' + id_type + '] , 证件号码 = [' + id_value + ']')

    return render(request, 'watchlist/record_query.html', {
        'record_list': record_list,
        'error_message': "You didn't select a record.",
    })


@login_required
def record_query(request):
    return render(request, 'watchlist/record_query.html')


@login_required
def record_detail(request, record_id):
    logger.info('[INFO] WATCHLIST LOG : User [' + auth.get_user(
        request).username + '] query person watchlist detail, record_id = [' + str(record_id) + ']')

    country_detail = DwDowjPersonCntryDtl.objects.filter(person_id=record_id)
    description_detail = DwDowjPersonDescDtl.objects.filter(person_id=record_id)
    date_detail = DwDowjPersonDateDtl.objects.filter(person_id=record_id)
    document_detail = DwDowjPersonDocumentDtl.objects.filter(person_id=record_id)
    name_detail = DwDowjPersonNameDtl.objects.filter(person_id=record_id)
    place_detail = DwDowjPersonPlaceDtl.objects.filter(person_id=record_id)
    profile_detail = DwDowjPersonProfileDtl.objects.filter(person_id=record_id)
    role_detail = DwDowjPersonRoleDtl.objects.filter(person_id=record_id)
    base_detail = DwDowjPersonDtl.objects.filter(person_id=record_id)
    image_detail = DwDowjPersonImageDtl.objects.filter(person_id=record_id)

    return render(request, 'watchlist/record_detail.html', {
        'country_detail': country_detail,
        'description_detail': description_detail,
        'date_detail': date_detail,
        'document_detail': document_detail,
        'name_detail': name_detail,
        'place_detail': place_detail,
        'profile_detail': profile_detail,
        'role_detail': role_detail,
        'base_detail': base_detail,
        'image_detail': image_detail,
    })


@login_required
def corp_result(request):
    record_name = request.POST['record_name']
    id_type = request.POST['id_type']
    id_value = request.POST['id_value']

    logger.info('[INFO] WATCHLIST LOG : User [' + auth.get_user(
        request).username + '] query entity watchlist, name = [' + record_name + '] id_type = [' + id_type + '] id_value = [' + id_value + ']')

    record_list = ''

    if record_name != '' or id_type != '' or id_value != '':

        record_filter = DwDowjRecordIndex.objects.all()

        if record_name != '':
            record_filter = record_filter.filter(record_name=record_name)

        if id_type != '':
            record_filter = record_filter.filter(id_type=id_type)

        if id_value != '':
            record_filter = record_filter.filter(id_value=id_value)

        record_list = record_filter

        audit_log_insert(auth.get_user(request).id, auth.get_user(request).username, '黑名单公司查询',
                         '客户名称=[' + record_name + '] , 证件类型 = [' + id_type + '] , 证件号码 = [' + id_value + ']')

    return render(request, 'watchlist/corp_query.html', {
        'record_list': record_list,
        'error_message': "You didn't select a record.",
    })


@login_required
def corp_query(request):
    return render(request, 'watchlist/corp_query.html')


@login_required
def corp_detail(request, record_id):
    logger.info('[INFO] WATCHLIST LOG : User [' + auth.get_user(
        request).username + '] query entity watchlist detail, record_id = [' + record_id + ']')

    base_detail = DwDowjEntityDtl.objects.filter(entity_id=record_id)
    company_detail = DwDowjEntityCompanyDtl.objects.filter(entity_id=record_id)
    country_detail = DwDowjEntityCountryDtl.objects.filter(entity_id=record_id)
    date_detail = DwDowjEntityDateDtl.objects.filter(entity_id=record_id)
    description_detail = DwDowjEntityDescDtl.objects.filter(entity_id=record_id)

    document_detail = DwDowjEntityDocumentDtl.objects.filter(entity_id=record_id)
    name_detail = DwDowjEntityNameDtl.objects.filter(entity_id=record_id)
    profile_detail = DwDowjEntityProfileDtl.objects.filter(entity_id=record_id)
    reference_detail = DwDowjEntityRefDtl.objects.filter(entity_id=record_id)
    source_detail = DwDowjEntitySourceDtl.objects.filter(entity_id=record_id)

    sr_detail = DwDowjEntitySrDtl.objects.filter(entity_id=record_id)

    return render(request, 'watchlist/corp_detail.html', {
        'base_detail': base_detail,
        'company_detail': company_detail,
        'country_detail': country_detail,
        'description_detail': description_detail,
        'date_detail': date_detail,
        'document_detail': document_detail,
        'name_detail': name_detail,
        'profile_detail': profile_detail,
        'reference_detail': reference_detail,
        'source_detail': source_detail,
        'sr_detail': sr_detail,
    })


@login_required
def corp_associate(request, record_id):
    return render(request, 'watchlist/corp_associate.html')


@login_required
def corp_associate_query(request):
    return render(request, 'watchlist/corp_associate.html')


# 审计日志查询
@login_required
def audit_log_query(request):
    return render(request, 'watchlist/audit_log.html')


@login_required
def audit_log_result(request):
    username = request.POST['username']
    oper_memo = request.POST['oper_memo']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    record_list = ''
    if username + oper_memo + start_date + end_date != '':

        result_filter = DwDowjAuditLog.objects.all()

        if username != '':
            result_filter = result_filter.filter(username=username)

        if oper_memo != '':
            result_filter = result_filter.filter(oper_memo__contains=oper_memo)

        if start_date != '':
            result_filter = result_filter.filter(
                oper_time__gte=datetime.date(int(start_date[:4]), int(start_date[5:7]), int(start_date[8:10])))

        if end_date != '':
            result_filter = result_filter.filter(
                oper_time__lte=datetime.date(int(end_date[:4]), int(end_date[5:7]), int(end_date[8:10])))

        record_list = result_filter

    return render(request, 'watchlist/audit_log.html', {
        'record_list': record_list
    })


class DowjIdentifyView(APIView):

    def get(self, request, format=None):
        # records = DwDowjRecordIndex.objects.all()[0:4]
        # serializer = WatchlistSerializer(records, many=True)
        return Response('', status.HTTP_405_METHOD_NOT_ALLOWED)

    # @silk_profile(name='DowjIdentifyView_post')  # name在Profiling页面区分不同请求名称
    def post(self, request, format=None):
        # 计算匹配结果，每一种匹配类型是一个占位符，
        # 0，不匹配
        # 1，完全匹配
        # 2，证件类型、证件号码匹配
        # 3，姓名、证件号码匹配
        # 4，姓名匹配
        # 5，证件号码匹配

        time.sleep(3)

        identify_json = {'return_code': '0', 'return_info': 'dowj jones black list identification successful!'}

        identify_dic = {'record_name': request.data.get('req_data').get('record_name', ''),
                        'id_value': request.data.get('req_data').get('id_value', ''),
                        'id_type': request.data.get('req_data').get('id_type', ''),
                        'result': 0}

        service_name = request.data.get('service_name')
        system_sign = request.data.get('system_sign')
        company_id = request.data.get('company_id')
        req_timestamp = request.data.get('req_timestamp')

        # logging
        logger.info(
            '[INFO] WATCHLIST LOG : Service_Name = [' + service_name + '] system_sign = [' + system_sign
            + '] company_id = [' + company_id + '] req_timestamp = [' + req_timestamp + '] record_name = [' +
            identify_dic['record_name'] + '] id_value = [' + identify_dic['id_value'] + '] id_type = [' + identify_dic[
                'id_type'] + ']')

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
        # print(identify_json)

        serializer = IdentifyResultSerializer(data=identify_json)

        if serializer.is_valid():
            # print(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
