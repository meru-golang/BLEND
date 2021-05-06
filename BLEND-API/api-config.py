#BLENDの必要なURL
class config:
    #BLENDのURL
    host_url = "https://blend.school/api"

    #ログイン
    login = "/login"

    #報告
    report = "/student/health_report/regist_answer"

#ヘッダー関連
class headers:
    #Host
    host = "blend.school"

    #User-Agent
    user = "okhttp/3.12.0"

    #Accept-Encoding
    Accept-Encoding = "gzip"

    #Content-Type
    Content-Type = "application/json; charset=UTF-8"

    #Content-Lengthログイン用
    length-login = "62"

    #Content-Length報告用
    length-report = "74"