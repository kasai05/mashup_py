#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
import json
import struct
import sys
import uuid

# APIアクセスキー
gnavi_keyid = "2841a8e7e9c397c3fb2d97a5fb516816"
google_api_key = "AIzaSyBSzIn2MoyrCo-B4wBGEIvFAT2UKFDR5dM"

# エンドポイントURL
gnavi_uri = "https://api.gnavi.co.jp/RestSearchAPI/20150630/"

# 変数の型が文字列かどうかチェック
def is_str(data=None):
    if isinstance(data, str) or isinstance(data, unicode):
        return True
    else:
        return False

def http_get(url):
    try:
        return urllib.urlopen(url).read()
    except ValueError:
        print u"APIアクセスに失敗しました。"
        sys.exit()

def getlocation(address):
    geocode_uri = "https://maps.googleapis.com/maps/api/geocode/json"
    geocode_uri += "?address=" + address + "&language=ja"

    # 取得した結果を解析
    data = json.loads(http_get(geocode_uri))
    return data['results'][0]

print ('住所を入力してください >> ')
address = raw_input()

#緯度・経度の取得
location = getlocation(address)

latitude = location['geometry']['location']['lat']
longitude = location['geometry']['location']['lng']

# URLに続けて入れるパラメータを組立
query = [
    ("format",    "json"),
    ("keyid",     gnavi_keyid),
    ("latitude",  latitude),
    ("longitude", longitude),
    ("range",     1)
]

# URL生成
gnavi_uri += "?{0}".format(urllib.urlencode(query))

# API実行
result = http_get(gnavi_uri)

# 取得した結果を解析
data = json.loads(result)

# エラーの場合
if "error" in data:
    if "message" in data:
        print u"{0}".format(data["message"])
    else:
        print u"データ取得に失敗しました。"
    sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data:
    total_hit_count = data["total_hit_count"]

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0:
    print u"指定した内容ではヒットしませんでした。"
    sys.exit()

# レストランデータがなかったら終了
if not "rest" in data:
    print u"レストランデータが見つからなかったため終了します。"
    sys.exit()

# ヒット件数表示
print "{0}件ヒットしました。".format(total_hit_count)
print "店舗名  |  連絡先  |  最寄の路線  |  最寄の駅  |  最寄駅から店までの時間 "

# 出力件数
disp_count = 0

# レストランデータ取得
for rest in data["rest"]:
    line = []
    id = ""
    name = ""
    access_line = ""
    access_station = ""
    access_walk = ""
    code_category_name_s = []

    # 店舗名
    if "name" in rest and is_str(rest["name"]):
        name = u"{0}".format(rest["name"]).replace(u" ","")
        line.append(name)

    # 連絡先
    if "tel" in rest and is_str(rest["tel"]):
        tel = u"{0}".format(rest["tel"]).replace(u" ","")
        line.append(tel)

    if "access" in rest:
        access = rest["access"]
        # 最寄の路線
        if "line" in access and is_str(access["line"]):
            access_line = u"{0}".format(access["line"]).replace(u" ","")
        # 最寄の駅
        if "station" in access and is_str(access["station"]):
            access_station = u"{0}".format(access["station"]).replace(u" ","")
        # 最寄駅から店までの時間
        if "walk" in access and is_str(access["walk"]):
            access_walk = u"{0}分".format(access["walk"]).replace(u" ","")

        line.extend([access_line, access_station, access_walk])

    if len(line) == 0:
        print "データが正しく表示されませんでした。"
        sys.exit()

    print " | ".join(line)
    disp_count += 1

# 出力件数を表示して終了
print "----"
print u"{0}件出力しました。".format(disp_count)
sys.exit()
