import sys
import os

class FileManipulator:
	# 今後の拡張を見越して設定
	def __init__(self):
		pass

	# ファイルの内容を逆にして出力
	def reverse(self, inputpath, outputpath):
		# 通常の処理
		try:
			# ファイルの読み込み
			with open(inputpath, 'r') as file:
				content = file.read()
				# 読み込んだファイルを逆文字列にして変数に格納する
				reversed_content = content[::-1]

			# ファイルへ書き込み
			with open(outputpath, 'w') as file:
				file.write(reversed_content)

			print(f"'{inputpath}'の内容を反転し、'{outputpath}'に保存しました。")

		# エラー発生時の処理
		except FileNotFoundError:
			print(f"エラー: '{inputpath}'が見つかりません。")


	# ファイルの内容をコピーして新しいファイルに保存
	def copy(self, inputpath, outputpath):
		# 通常の処理
		try:
			# ファイルの読み込み
			with open(inputpath, 'r') as file:
				content = file.read()

			# ファイルへ書き込み
			with open(outputpath, 'w') as file:
				file.write(content)

			print(f"'{inputpath}'の内容をコピーし、'{outputpath}'に保存しました。")		

		# エラー発生時の処理
		except FileNotFoundError:
			print(f"エラー: '{inputpath}'が見つかりません。")


	# ファイルの内容を複製して上書き
	def duplicate_contents(self, inputpath, n):
		# 通常の処理
		try:
			n = int(n)

			# ファイルの読み込み
			with open(inputpath, 'r') as file:
				content = file.read()
				duplicated_content = content * n

			# ファイルへの上書き
			with open(inputpath, 'w') as file:
				file.write(duplicated_content)

			print(f"'{inputpath}'の内容を{n}回複製しました。")		

		# エラー発生時の処理
		except FileNotFoundError:
			print(f"エラー: '{inputpath}'が見つかりません。")
			
		except ValueError:
			print(f"エラー: nは整数である必要があります。")


	# ファイルの内容の指定文字列の置き換え
	def replace_string(self, inputpath, needle, newstring):
		# 通常の処理
		try:
			# ファイルの読み込み
			with open(inputpath, 'r') as file:
				content = file.read()
				updated_content = content.replace(needle, newstring)

			# ファイルへ上書き
			with open(inputpath, 'w') as file:
				file.write(updated_content)

			print(f"'{inputpath}'の内容を、'{needle}'から'{newstring}'に置き換えました。")		

		# エラー発生時の処理
		except FileNotFoundError:
			print(f"エラー: '{inputpath}'が見つかりません。")

	
# 引数のバリデーション
def validate_args(args):
	if len(args) < 2:
		print("エラー: コマンドが指定されていません。例:python3 file_manipulator.py <command> <arguments>")
		return False

	command = args[1]

	if command == "reverse" or command == "copy":
		# 引数が4つない場合
		if len(args) != 4:
			print(f"エラー: '{command}'コマンドには <inputpath> と <outputpath> が必要です。")
			return False

		# 指定したパスが存在しない場合
		elif not os.path.isfile(args[2]):
			print (f"エラー: 入力ファイル'{args[2]}'が存在しません。")
			return False

	elif command == "duplicate-contents":
		# 引数が4つない場合
		if len(args) != 4:
			print(f"エラー: 'duplicate-contents'コマンドには <inputpath> と <n> が必要です。")
			return False

		# 指定したパスが存在しない場合
		elif not os.path.isfile(args[2]):
			print(f"エラー: 入力ファイル'{args[2]}'が存在しません。")
			return False

		# 指定した引数が整数でない場合
		elif not args[3].isdigit():
			print(f"エラー: 'n'は正の整数である必要があります。")
			return False

	elif command == "replace-string":
		# 引数が5つない場合
		if len(args) != 5:
			print(f"エラー: 'replace-string'コマンドには <inputpath>, <needle>, <newstring> が必要です。")
			return False

		# 指定したパスが存在しない場合
		elif not os.path.isfile(args[2]):
			print(f"エラー: 入力ファイル'{args[2]}'が存在しません。")
			return False

	else:
		print(f"エラー: コマンド'{command}'はサポートされていません。")
		return False

	return True


# メイン処理
# __name__: Pythonの特殊変数で、スクリプトの実行内容に応じて異なる値を持つ
# スクリプトが直接実行された場合、__name__には__main__が入る
if __name__ == "__main__":
	args = sys.argv

	# 0:正常終了 1:異常終了
	# 引数が正しくない場合、プログラム終了
	if not validate_args(args):
		sys.exit(1)

	manipulator = FileManipulator()
	command = args[1]

	if command == "reverse":
		manipulator.reverse(args[2], args[3])
	
	elif command == "copy":
		manipulator.copy(args[2], args[3])

	elif command == "duplicate-contents":
		manipulator.duplicate_contents(args[2], args[3])

	elif command == "replace-string":
		manipulator.replace_string(args[2], args[3], args[4])