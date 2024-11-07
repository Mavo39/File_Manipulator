# File_Manipulator
File Manipulatorは、ファイルを操作するためのPythonプログラムです。
このプログラムはRecursionCSのプログラムの1つです。
指定されたファイルの内容を反転、コピー、複製、または文字列を置き換える操作が可能です。
コマンドラインから実行し、ファイルに対してさまざまな変更を加えることができます。

## 機能
このプログラムは、以下のコマンドをサポートしています。
・reverse: ファイルの内容を反転して新しいファイルに保存します。
・copy: ファイルの内容をコピーして新しいファイルに保存します。
・duplicate-contents: ファイルの内容を指定した回数複製します。
・replace-string: ファイルの内容を、指定された文字列から別の文字列へ置き換えます。

## 前提条件
Python3.xがインストールされている必要があります。

## インストール
1. このリポジトリをクローンします。
　bash: git clone https://github.com/username/repository_name.git
2. クローンしたディレクトリに移動します。
　bash: cd repository_name

## 使用方法
このプログラムはコマンドラインから実行します。以下は、各コマンドです。

# コマンド一覧
1. ファイルの内容を反転
　bash: python3 file_manipulator.py reverse <inputpath> <outputpath>
・inputpath: 操作するファイルのパス
・outputpath: 出力結果を保存するファイルのパス

2. ファイルの内容をコピー
　bash: python3 file_manipulator.py copy <inputpath> <outputpath>
・inputpath: コピー元のファイルのパス
・outputpath: コピー結果を保存するファイルのパス

3. ファイルの内容を複製
　bash: python3 file_manipulator.py duplicate-contents <inputpath> <n>
・inputpath: 操作するファイルのパス
・n: ファイルの内容を複製する回数（整数）

4. 文字列の置換
　bash: python3 file_manipulator.py replace-string <inputpath> <needle> <newstring>
・inputpath: 操作するファイルのパス
・needle: 置換対象の文字列
・newstring: 新しい文字列

## エラーハンドリング
プログラムは、以下のエラーに対応しております。
・入力ファイルが存在しない場合
・無効な引数が渡された場合
・置換用の文字列や複製回数が適切でない場合
各エラーについては、適切なメッセージが表示され、プログラムが停止します。
