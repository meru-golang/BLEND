# 健康報告
BLENDの健康報告の通信(体温と日付のみ)

# Method
~~~
POST
https://blend.school/api/student/health_report/regist_answer
~~~

# Header
~~~
Host: blend.school
Content-Type: application/json
Content-Length: 48
Accept-Encoding: gzip
User-Agent: okhttp/3.12.0
Authorization: Token Here
~~~
* Authorization以外記入不要

# Body
~~~
{
  "answer_180": "体温",
  "report_date": "日付(2021-04-01)"
}
~~~
* 日付は実行した日付では無いと送信できない

体温を修正するのであれば別の通信が必要(後日記載)

# Response
~~~
{
  "status": 200
  "id": 229814 #ここはランダム?
}
~~~
* 正常に送信できればstatusが200

IDはランダム生成で体温の修正に使える
