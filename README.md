# BouYearFestival
## 忘年会をするよ〜
これは忘年会用の謎解きアプリだよ～

### 公開版リポジトリ

2019年の会社の忘年会でやりました。3人で作りました～。  
忘年会版からheroku公開版にするにあたって、マイナーチェンジを行いました。  
当たり前ですがソースコードを見ると答えがわかるので、見ないようにしてください。

＜変更点＞

* 忘年会でやったコント　→　Googleドキュメントで台本を掲載
* 忘年会で配ったしおり　→　新ページを作って代用
* 謎の答え　→　個人情報をほぼ削除

### 作った人

一応紹介します。[YuichiSemura](https://github.com/YuichiSemura)、[thtitech](https://github.com/thtitech)、[tofuchic](https://github.com/tofuchic)  

## 開発環境

開発時のREADME.mdの内容↓

### 導入方法
1. まず[ここ](https://qiita.com/1000ch/items/93841f76ea52551b6a97)を参考にpyenvを導入する。Macの場合、 `brew install pyenv` でもいける気がする。
**pythonの導入はまだしないこと。**
また、windowsにはpyenvを導入できないので、その場合はanaconda3-4.1.0を自力でインストールする。

2. pyenvからanaconda3-4.1.0をinstallする。
```
$ pyenv install --list | grep anaconda3-4 # 確認コマンド
$ pyenv install anaconda3-4.1.0
```

3. 作業ディレクトリに移動してanacondaで仮想環境を作成、有効化する
```
$ cd /your/work/dir
$ pyenv versions # 確認コマンド
$ pyenv local anaconda3-4.1.0
$ pyenv versions # pythonがanacondaになっていることの確認
$ conda create -n py36 python=3.6 anaconda # anaconda仮想環境の作成
$ source $PYENV_ROOT/versions/anaconda3-4.1.0/bin/activate py36
```
このときpyenvのactivateコマンドとanacondaのactivateコマンドが衝突しているのでフルパスで指定する（もしくはaliasを設定する）。
プロンプトに仮想環境名が表示されたら成功。

4. Flaskのバージョン確認
```
$ python
$ >> import flask
$ >> flask.__version__ # 1.1.1になっていることを確認
```

5. 必要ライブラリのインストール
```
$ pip install Flask-WTF
```

### 設定ファイルの記述
`app.conf` の内容を自分の環境にそって書き換える。
```
port=8080
debug_path=logs/debug.log
error_path=logs/error.log
auth_dir=data/
sec_name=sec.pem
pub_name=pub.pem
```

### サーバの起動
```
$ python server.py
```

`app.conf` で指定したポート番号で起動する。
ブラウザで `localhost:8080/start` とかにアクセスすれば謎解き開始。


Apacheサーバとの連携は[ここ](https://qiita.com/arc279/items/df28bd100cc2f72fad3c)や[ここ](https://conta.hatenablog.com/entry/2012/01/16/005312)を参考にwsgiを導入する必要あり。
`server.wsgi` はサーバ導入時に追記予定。

## URL
以下のようにマッピングしている（GETリクエストのみ記載）
```
/start: 謎解き開始
/restart: なにかエラーが起きたり、どうしようもなくなったときに初めからできる
```
