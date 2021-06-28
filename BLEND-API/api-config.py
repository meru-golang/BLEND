#BLENDの必要なURL
class config:
    #BLENDのURL
    host_url = "https://blend.school/api"

    #ログイン
    login = host_url + "/login"

    #報告
    report = host_url + "/student/health_report/regist_answer"

#ヘッダー関連
class headers:
    #Host
    host = "blend.school"

    #User-Agent
    UA = "okhttp/3.12.0"

    #Accept-Encoding
    Accept = "gzip"

    #Content-Type
    ContentType = "application/json; charset=UTF-8"

    #Content-Lengthログイン用
    length_login = "62"

    #Content-Length報告用
    length_report = "74"