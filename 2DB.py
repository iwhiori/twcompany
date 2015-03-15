#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

def find_twcom(per_file):
    fp = open(per_file, "r")
    while 1:
        line = fp.readline()
        if not line:
            break
        UN = line[0:8]
        firm_status = ""
        firm_name = ""
        paid_in_capital = 0
        name = ""
        address = ""
        setup_year = ""
        setup_month = ""
        setup_day = ""
        update_year = ""
        update_month = ""
        update_day = ""
        career_infomation = ""
        for item in json.loads(line[9:]).items():
            if item[0] == u'公司狀況':
                firm_status = item[1]
            if item[0] == u'公司名稱':
                firm_name = item[1]
            if item[0] == u'資本總額(元)':
                continue
                authorised_capital = item[1]
            if item[0] == u'實收資本額(元)':
                if len(item[1].strip()) == 0:
                    break
                paid_in_capital = int(item[1].replace(',',''))
                if paid_in_capital < 500000000:
                    break
            if item[0] == u'代表人姓名':
                name = item[1]
            if item[0] == u'公司所在地':
                address = item[1]
                continue
            if item[0] == u'登記機關':
                continue
                print item[1]
            if item[0] == u'核准設立日期':
                if not item[1]:
                    continue
                setup_year = item[1]['year']
                setup_month = item[1]['month']
                setup_day = item[1]['day']
            if item[0] == u'最後核准變更日期':
                if not item[1]:
                    continue
                update_year = item[1]['year']
                update_month = item[1]['month']
                update_day = item[1]['day']
            if item[0] == u'所營事業資料':
                continue
                for i in item[1]:
                    career_infomation = i[1],
            if item[0] == u'董監事名單':
                continue
                for ppl_list in item[1]:
                    print u'序號'+ppl_list[u'序號'],
                    print u'職稱'+ppl_list[u'職稱'],
                    print u'姓名'+ppl_list[u'姓名'],
#print u'所代表法人'+", ".join(ppl_list[u'所代表法人']),
                    print u'出資額'+ppl_list[u'出資額'],
            if item[0] == u'經理人名單':
                continue
                for ppl_list in item[1]:
                    print u'序號'+ppl_list[u'序號'],
                    print u'姓名'+ppl_list[u'姓名'],
        if paid_in_capital < 500000000:
            continue
#print u'到職日期',ppl_list[u'到職日期'],
        foo = u'%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (UN, firm_status, firm_name, paid_in_capital, update_year, update_month, update_day, setup_year, setup_month, setup_day, address)
        csv.write(foo.encode('utf8'))
    fp.close()

files = [\
        "10000000.json",\
        "20000000.json",\
        "30000000.json",\
        "40000000.json",\
        "50000000.json",\
        "60000000.json",\
        "70000000.json",\
        "80000000.json",\
        "90000000.json",\
        ]

csv = open("x0000000.csv", "w")
csv.write('統一編號,公司狀況,公司名稱,實收資本額(元),最後核准變更日期年,月,日,核准設立日期年,月,日,Address' + os.linesep)

for per_file in files:
    find_twcom(per_file)

csv.close()
