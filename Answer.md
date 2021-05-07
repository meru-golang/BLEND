# アンケート
BLENDのアンケートの通信(送信)

# Method
~~~
POST
https://blend.school/api/student/scom/read_answer
~~~

# Header
~~~
Host: blend.school
content-type: application/json; charset=UTF-8
content-length: 324
accept-encoding: gzip
user-agent: okhttp/3.12.0
authorization: token here
~~~
* Headerは設定しなくても問題なく201が返ってくる

# Body
~~~
{
    "id":idplz,
    "q_answer": answer
    "q_id": idplz
}
~~~

# Response
~~~
{
"status":200
}
~~~
