## データ収集の準備

### エブリセンスの用語について
* オーダー：  
レストランオーナーがセンサー情報収集するために指定した条件定義。求められるデータの条件や期間、報酬などを記載したもの。今回のハンズオンでは
**「JDMCデータ収集」**
という名称のオーダーを登録しています。
* ファーム：  
ひとつ以上のハードウェアデバイスにより構成される仮想的なデータ提供群。
例えば、EveyrPost(iPhone)とEveryStmapを組み合わせた状態を指します。
（一つまたは複数のデバイス(センサが搭載されたハードウェア)からなる
ファームオーナーが定義するデータ提供元です。）
* デバイス：  
ひとつ以上のセンサーを持つ、データ提供のためのハードウェア。
例えば、EveyrPost(iPhone)、Everystampそのものを指します
* センサー：  
センサーを搭載した機器（iPhone/Android Phone/EveryStamp）。
センサーデータを収集する機器。
個々のデータを計測するセンサを指します。

### アプリケーションのインストール
データ収集に当たり、エブリセンス社のデータ収集アプリケーション（EveryPost）を利用します。
Android、iPhoneそれぞれについてインストール方法は下記を参照してください。

* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#sec1-install
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#sec1-1
### オーナー情報の登録
インストール後、オーナー登録のキーワード欄に「JDMCカンファレンス」と設定してください。
※下記マニュアル項番16「指定されたキーワードがあれば、入力します」を参照。
* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#16-%E6%8C%87%E5%AE%9A%E3%81%95%E3%82%8C%E3%81%9F%E3%82%AD%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%89%E5%85%A5%E5%8A%9B%E3%81%8C%E3%81%82%E3%82%8C%E3%81%B0%E5%85%A5%E5%8A%9B%E3%81%97%E3%81%BE%E3%81%99
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#16-%E6%8C%87%E5%AE%9A%E3%81%95%E3%82%8C%E3%81%9F%E3%82%AD%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%89%E5%85%A5%E5%8A%9B%E3%81%8C%E3%81%82%E3%82%8C%E3%81%B0%E5%85%A5%E5%8A%9B%E3%81%97%E3%81%BE%E3%81%99

　**キーワード：JDMCカンファレンス**
　を必ず入力してください。

### ファーム情報の変更
アプリケーションのインストールが完了すると
**デバイス**
と
**ファーム**
が１つずつ登録済の状態となっています。このうち、ファームについて下記のマニュアルに従って、スマートフォンからデータを送るセンサーの内容を変更します。

以下の「高度な設定」の「3.ファーム情報変更」を参照し、「送信情報」欄からセンサーとして「位置」のみを残し、その他センサーを削除してください。  
※誤って「位置」を削除した場合はプルダウンメニューから追加することで再設定が可能です。  
* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E9%AB%98%E5%BA%A6%E3%81%AA%E8%A8%AD%E5%AE%9A
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E9%AB%98%E5%BA%A6%E3%81%AA%E8%A8%AD%E5%AE%9A

### オーダーの選択と稼働状態への変更 ###
ここまでの設定が完了すると、オーダーとして「JDMCデータ収集」が参照できる状態となっています。下記のマニュアルに従って、「オーダー一覧」から「JDMCデータ収集」を見つけ、詳細画面で稼働状態に変更してください。

* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%81%AE%E8%A9%B3%E7%B4%B0
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%81%AE%E8%A9%B3%E7%B4%B0%E7%94%BB%E9%9D%A2

### データ提供を停止する場合 ###
オーダーが稼働状態にある場合、アプリケーションを起動させておくと継続してデータを送信します。データを送信したくない場合は、下記のマニュアルに従って、オーダーを停止してください。  
※停止したオーダーは再度「稼働」状態にすることでデータ送信を再開できます。

* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%81%AE%E5%81%9C%E6%AD%A2
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%81%AE%E5%81%9C%E6%AD%A2

### 音声ガイダンスについて
データを送信する際、音声ガイダンスの設定を「データを送るときにセンサーメッセージを出します」をチェックしていると、データ送信の度に音声ガイダンスが流れます。音声ガイダンスが不要な場合は、このチェックを外してください。

* Android版（ESpost2）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost2)-Android%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#sec3-voice
* iPhone版（ESpost）  
https://github.com/every-sense/UserDocument/wiki/EveryPost(ESpost)iPhone%E7%89%88%E5%8F%96%E3%82%8A%E6%89%B1%E3%81%84%E8%AA%AC%E6%98%8E%E6%9B%B8#voice


### 注意事項
今回は、カンファレンス期間に限定して収集されるデータであり、ハンズオン以外の用途では使用致しません。
また、ポイントの付与もございませんので、あらかじめご了承の上データ提供頂ければと思います。

**オーダー一覧に「JDMCデータ収集」が表示されない場合**  
「オーダー一覧」に「JDMCデータ収集」が表示されない場合、以下の内容を再度ご確認ください。  
※本手順を再度ご確認頂き、漏れがないか確認してください。
* アカウント設定の「キーワード」に「JDMCカンファレンス」が設定されていること
* ファーム一覧画面で表示されたファーム名をタップし、「ファーム情報変更」画面の「デバイス」に表示されているセンサー情報を、「位置」のみ残して、その他デバイスを「ゴミ箱」アイコンをタップして削除し、「更新」をタップする。