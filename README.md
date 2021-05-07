# BLENDとは何か
[BLEND](https://blend.school)

BLENDとは、モチベーションワークス株式会社によって運営されている校務支援システムである。

アプリ本体はバグが多く、アップデートを行っても再ログインするまでは修正されない。

また、サーバー側にも問題があり
* APIの呼び出し回数制限が無し(全てのエンドポイントにおいて制限が無いのでDoS攻撃が可能)



# 必要な物
* BLENDのアカウント(Googleログイン制の物は非対応)
* Python3が動作する環境(Windowsでもok)

# 使い方
まだない

# BLENDの通信
* [ログイン](https://github.com/meru-golang/BLEND/blob/main/Login.md)
* [健康報告](https://github.com/meru-golang/BLEND/blob/main/Report.md)
* [アンケート](https://github.com/meru-golang/BLEND/blob/main/Answer.md)


# 注意点
APIの制限が無いが、大量にリクエストを送るのはやめよう！

# Author
* [meru_golang](https://github.com/meru-golang)
