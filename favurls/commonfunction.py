# -*-coding:utf-8-*-
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.serializers import serialize
from django.db import connection


def queryset_to_json(result):
    """ 将queryset转换为json格式的数据 """
    result_encode = list(result)
    # 判断查询结果是否为list，如果是list即表示数据查询时使用了valuse()，否则使用的是all()
    if isinstance(result_encode, list):
        data = json.dumps(result_encode, cls=DjangoJSONEncoder, ensure_ascii=False)
    else:
        temp = serialize('python', result)
        data = json.dumps(list(temp), cls=DjangoJSONEncoder, ensure_ascii=False)
    return data


def fetch2dic(cursor, rawdata):
    """
    将自定义的查询结果转换成字典组
    :param cursor:
    :param rawdata:
    :return:
    """
    col_names = [desc[0] for desc in cursor.description]
    print(col_names)
    result = []
    for row in rawdata:
        odjDict = {}
        for index, value in enumerate(row):
            odjDict[col_names[index]] = value
        result.append(odjDict)
    return result


def customquery2(sql, param):
    """自定义的sql查询方法，sql传字符串，param传元祖，如：(emp_id, level_sn, award_sn, userid)"""
    cursor = connection.cursor()
    cursor.execute(sql, param)
    rawdata = cursor.fetchall()
    return fetch2dic(cursor, rawdata)
    # with connection.cursor() as cursor:
    #     cursor.execute(sql, param)
    #     rawdata = cursor.fetchall()
    #     return fetch2dic(cursor, rawdata)


def customquery(sql):
    """自定义的sql查询方法，sql传字符串，param传元祖，如：(emp_id, level_sn, award_sn, userid)"""
    cursor = connection.cursor()
    cursor.execute(sql)
    rawdata = cursor.fetchall()
    return fetch2dic(cursor, rawdata)


def custominsert(sql):
    # with connection.cursor() as cc:
    #     cc.cursor.execute(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    return True

