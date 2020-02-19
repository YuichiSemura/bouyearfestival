# set constants
LOGIN_PAGE = "page1.html"
murase_PAGE = "page2.html"
tanaka_PAGE = "page3.html"
DUMMY_PAGE = "page4.html"

COOKIE_Q1 = "q1"
COOKIE_Q2 = "q2"
COOKIE_Q3 = "q3"
COOKIE_PARITY = "parity"

ANS1 = "muraseyuichi"
ANS2 = "1110"
ANS3 = "tanakayuichi"
YUICHI = "yuichi"

WRGANS11 = "muraseyuuichi"

ERR1 = "IDはフルネームです。 ex) yamadahanako"
ERR2 = "ユーザー名が違います"
ERR3 = "文字数が長すぎます"
ERR4 = "英数字以外の文字が含まれています"
ERR5 = "空文字列です"
ERR6 = "プロセスIDが違います"
ERR7 = "現在のユーザーでは権限が不足しています"
ERR8 = "数字以外の文字が含まれています"

############################
# post_p1
# q1 = 0
# shoki
MSG_s1 = """<h3>まずは、問題 1 と問題 2 を解いて</h3>
<h3>ユーザー名を特定してください！</h3>
<br>
<h3>問題 1 では<b style="color : #4ec6db ;">ボタン</b>を押してみてね！</h3>
<h3>問題 2 は<b style="color : #4ec6db ;">自然</b>に関係するわ...</h3>
<br>
<h3>ユーザー名はローマ字で入力するのよ！</h3>"""

# muraseyuuichi
MSG_w11 = """<h3>少し表記が違うみたいです！</h3>
<h3>u が 1 つ要らないみたい！</h3>
<h3>　</h3>""" + MSG_s1

# wrong
MSG_w19 = """<h3>もう一度考えてみましょう！</h3>
<h3>　</h3>""" + MSG_s1

############################
# q1 = 1
# shoki 
MSG_s2 = """<h3>さっきと変わっている場所はありませんか？</h3>
<h3>別のユーザー名を特定してください！</h3>
<h3>　</h3>
<h3>困ったらしおりを見ましょう！</h3>
<h3>何かヒントが隠れているかも！</h3>"""

# yuichi
MSG_w21 = """<h3>ユーザ名はフルネームです！</h3>
<h3>　</h3>
<h3>さっきと変わっている場所はありませんか？</h3>
<h3>別のユーザー名を特定してください！</h3>
<h3>　</h3>
<h3>困ったらしおりを見ましょう！</h3>
<h3>何かヒントが隠れているかも！</h3>"""

# たなかゆういち
# yuuichi
# tanakayuuichi
# はさすがに人間じゃないのでカット

# 間違い
MSG_w29 = """<h3>もう一度考えてみましょう！</h3>
<h3>　</h3>
<h3>さっきと変わっている場所はありませんか？</h3>
<h3>別のユーザー名を特定してください！</h3>
<h3>　</h3>
<h3>困ったらしおりを見ましょう！</h3>
<h3>何かヒントが隠れているかも！</h3>"""

############################

#post_p2
MSG_s3 = """<h3>無事ログインできたようですね！！</h3>
<h3>　</h3>
<h3>次は、問題 3 と問題 4 を解いて</h3>
<h3>数字 4 桁のプロセス ID を特定してください！</h3>
<h3>　</h3>
<h3>困ったらしおりを見ましょう！</h3>
<h3>何かヒントが隠れているかも！</h3>"""

MSG_s4 = """<h3>プロセス ID を特定したようです！</h3>
<h3>　</h3>
<h3>しかし、現在ログイン中のユーザーは</h3>
<h3>プロセスを停止するための</h3>
<h3>権限が不足しているようです！</h3>
<h3>　</h3>
<h3>とりあえず右上のリンクから</h3>
<h3>ログインページに戻りましょう！</h3>"""

MSG_w39 = """<h3>もう一度考えてみましょう！</h3>
<h3>　</h3>
<h3>問題 3 と問題 4 を解いて</h3>
<h3>数字 4 桁のプロセスIDを特定してください！</h3>
<h3>　</h3>
<h3>困ったらしおりを見ましょう！</h3>
<h3>何かヒントが隠れているかも！</h3>"""

############################

PERSONS_JSON = """
[
    {
        "imgurl": "/static/image/yuichi.png",
        "name": "村瀬 雄一",
        "attrlist": [
            {
                "key": "birthday",
                "value": "2/18"
            },
            {
                "key": "肩書",
                "value": "フルスタックエンジニア"
            },
            {
                "key": "趣味",
                "value": "Splatoon"
            },
            {
                "key": "嫌いな言葉",
                "value": "コスモワールド"
            }
        ]
    },
        {
        "imgurl": "/static/image/hakone.png",
        "name": "箱根 亜美",
        "attrlist": [
            {
                "key": "birthday",
                "value": "9/11"
            },
            {
                "key": "肩書",
                "value": "Web系（あみだけに（は？））"
            },
            {
                "key": "趣味",
                "value": "AirPodsを掃除する"
            },
            {
                "key": "嫌いな言葉",
                "value": "◯◯でミルクボーイ風漫才やってみた"
            }
        ]
    },
    {
        "imgurl": "/static/image/hasuko.png",
        "name": "長谷部 蓮子",
        "attrlist": [
            {
                "key": "birthday",
                "value": "11/10"
            },
            {
                "key": "肩書",
                "value": "牛角マニア"
            },
            {
                "key": "上司",
                "value": "田中優一"
            },
            {
                "key": "趣味",
                "value": "モンハン野良でゆうたにハチミツをあげる"
            }
        ]
    },
    {
        "imgurl": "/static/image/mido.png",
        "name": "水鏡 導",
        "attrlist": [
            {
                "key": "birthday",
                "value": "3/3"
            },
            {
                "key": "夢",
                "value": "リポビタンDの空き瓶を集めて船を作って太平洋を渡る"
            },
            {
                "key": "趣味",
                "value": "トイレでサボる"
            },
            {
                "key": "特技",
                "value": "カロリービックバン"
            }
        ]
    },
    {
        "imgurl": "/static/image/kaiga.png",
        "name": "絵画 樹花",
        "attrlist": [
            {
                "key": "birthday",
                "value": "7/7"
            },
            {
                "key": "特技",
                "value": "邪念を0にする"
            },
            {
                "key": "嫌いな人",
                "value": "たくさん"
            },
            {
                "key": "好きなゲーム",
                "value": "Dead by Daylight"
            }
        ]
    },
    {
        "imgurl": "",
        "name": "春日 塗",
        "attrlist": [
            {
                "key": "birthday",
                "value": "null"
            },
            {
                "key": "好きな言葉",
                "value": "none"
            },
            {
                "key": "好きなゲーム",
                "value": "undefined"
            },
            {
                "key": "嫌いな例外",
                "value": "nil"
            }
        ]
    }
]
"""
