# ログイン
BLENDのログインの通信

# Method
~~~
POST
https://blend.school/api/login
~~~

# Header
~~~
Host: blend.school
Content-Type: application/json
Content-Length: 62
Accept-Encoding: gzip
User-Agent: okhttp/3.12.0
~~~
* Headerは設定しなくても問題なく201が返ってくる

# Body
~~~
{
"login_id":"mail",
"password":"pass"
}
~~~

# Response
~~~
{
"account_type":"student",
"token":"Token",
"link":""
}
~~~
* linkは何も入ってない
* トークンは失効しないと思われる、何回もログインしても同じ物が返ってくる

トークンは別の通信に必要なので毎回ログインするのが嫌なのであれば、txtなどに保存する事を推奨

