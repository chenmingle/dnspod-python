#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'chenmingle'

import urllib2
import urllib
import json
import time
import socket


public_dic={}
public_dic["login_token"]=("%s,%s" % ('Token_ID','Token_key'))
public_dic["format"]="json"
headers={}
headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"


###获取dmanin的id###
def getDomainID(domain):
    url="https://dnsapi.cn/Domain.INFO"
    params=public_dic.copy()
    params["domain"]=domain
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    formatJson=json.load(resp)
#    print formatJson["domain"]['id']
#    print formatJson["domain"]
    if formatJson["status"]["code"]!="1":
        return 0
    else:
        return formatJson["domain"]["id"]
    pass


###获取某个domain的域名解析列表###
def getRecordList(domain_id):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
#    print myJson
    for i in myJson['records']:
	print i['id'],i['type'],i['name'],i['line'],i['line_id'],i['value'],i['ttl'],i['enabled']


###获取某条域名解析id###
def getRecordID(domain_id,record,line_id):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    params["sub_domain"]=record
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
#    print myJson
    for i in myJson['records']:
	if i['line_id'] == line_id:
        	print i['id'],i['type'],i['name'],i['line'],i['value'],i['ttl'],i['status']


###创建域名解析###
def createRecord(domain_id,sub_domain,record_type,record_line_id,value):
    url="https://dnsapi.cn/Record.Create"
    params=public_dic.copy()
    params['domain_id']=domain_id
    params['sub_domain']=sub_domain
    params['record_type']=record_type
    params['record_line_id']=record_line_id
    params['value']=value
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    print myJson


###更新域名解析###
#def updateRecord(domain_id,sub_domain,record_type,record_line_id,value):
#    url="https://dnsapi.cn/Record.List"
#    params=public_dic.copy()
#    params["domain_id"]=domain_id
#    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
#    resp=urllib2.urlopen(req)
#    myJson=json.load(resp)
#    for i in myJson['records']:
#	if i['name'] == sub_domain and i['line_id'] == record_line_id:
#		record_id=i['id']
#		print record_id
#    url="https://dnsapi.cn/Record.Modify"
#    params=public_dic.copy()
#    params['domain_id']=domain_id
#    params['record_id']=record_id
#    params['sub_domain']=sub_domain
#    params['record_type']=record_type
#    params['record_line_id']=record_line_id
#    params['value']=value
#    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
#    resp=urllib2.urlopen(req)
#    myJson=json.load(resp)
#    print myJson


###更新域名解析配置###
def updateRecordLine(domain_id,sub_domain,record_type,line_id,record_line_id,value):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    for i in myJson['records']:
        if i['name'] == sub_domain and i['line_id'] == line_id:
                record_id=i['id']
                print record_id
    url="https://dnsapi.cn/Record.Modify"
    params=public_dic.copy()
    params['domain_id']=domain_id
    params['record_id']=record_id
    params['sub_domain']=sub_domain
    params['record_type']=record_type
    params['record_line_id']=record_line_id
    params['value']=value
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    print myJson


###修改域名解析状态###
def statusRecord(domain_id,sub_domain,record_line_id,status):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    for i in myJson['records']:
        if i['name'] == sub_domain and i['line_id'] == record_line_id:
                record_id=i['id']
    url="https://dnsapi.cn/Record.Status"
    params=public_dic.copy()
    params['domain_id']=domain_id
    params['record_id']=record_id
    params['status']=status
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    print myJson


###删除域名解析###
def deleteRecord(domain_id,sub_domain,record_line_id):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    for i in myJson['records']:
        if i['name'] == sub_domain and i['line_id'] == record_line_id:
                record_id=i['id']
    url="https://dnsapi.cn/Record.Remove"
    params=public_dic.copy()
    params['domain_id']=domain_id
    params['record_id']=record_id
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    print myJson


id = getDomainID('dnspod.com')
getRecordList(id)
#getRecordID(id,'cml','10=1')
#createRecord(id,'cml','A','0','126.40.109.48')
#updateRecordLine(id,'cml','A','10=1','10=1','126.40.109.48')
#statusRecord(id,'cml','10=1','enabled')
#deleteRecord(id,'cml','10=1')
