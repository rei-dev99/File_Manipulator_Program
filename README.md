# ⌘ File Manupulator Program
コマンドラインインターフェースを使って、コマンドと引数を渡してファイル操作を行うプログラム。

## 💻 環境
- Raspberry pi 4
- Ubuntu
- Python

## 👨‍💻 実行方法
4つのコマンドを実行できます。

コマンドを実行するにはまず下記コマンドを実行します。

```
python3 file_manipulator.py
```

その後、入力を求められるので下記に示すコマンドのように実行します。

### reverseコマンド
入力ファイル内の内容を反転して、出力ファイルに上書き保存します。

- 第一引数：コマンド名
- 第二引数：入力ファイル名
- 第三引数：出力ファイル名

実行例
```
reverse ./files/input.txt ./files/output.txt
```

### copyコマンド
入力ファイルの内容を出力ファイルにコピーします。

- 第一引数：コマンド名
- 第二引数：入力ファイル名
- 第三引数：出力ファイル名

実行例
```
copy ./files/input.txt ./files/output.txt
```

### duplicate-contentsコマンド
入力ファイルの内容を指定した回数文、入力ファイルに複製します。

- 第一引数：コマンド名
- 第二引数：入力ファイル名
- 第三引数：複製回数

実行例
```
duplicate-contents ./files/input.txt 3
```

### replace-stringコマンド
入力ファイルから任意の文字Aを任意の文字Bに変換します。

- 第一引数：コマンド名
- 第二引数：入力ファイル名
- 第三引数：入力ファイル内から探し出したい文字列
- 第四引数：置き換える文字列

実行例
```
replace-string ./files/input.txt needle newstring
```


