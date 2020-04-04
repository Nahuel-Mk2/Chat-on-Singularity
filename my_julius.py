# -*- coding: utf-8 -*-
import socket
# 以下自作関数
import my_a3rt
import my_openJTalk

def julius_function():
	host = '127.0.0.1'   # IPアドレス
	port = 10500         # Juliusとの通信用ポート番号
	# Juliusにソケット通信で接続
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))
	data = ""

	try:
		data = ""
		while True:
			if '</RECOGOUT>\n.' in data:
				# 出力結果から認識した単語を取り出す
				recog_text = ""
				for line in data.split('\n'):
					index = line.find('WORD="')
					if index != -1:
						line = line[index+6:line.find('"', index+6)]
						recog_text = recog_text + line
				reply = my_a3rt.api_function(recog_text) # ここで音声認識結果をa3rtに送り、返り値をreplyに代入
				my_openJTalk.openjtalk_function(reply) # replyに代入された文字列をopenJTalkに送る
				data =""
			else:
				data += str(client.recv(1024).decode('utf-8')) # utf-8だとエラーになったので、shift-jisで回避

	except KeyboardInterrupt:
	    print('finished')
	    client.send("DIE".encode('utf-8'))
	    client.close()

if __name__ == '__main__':
	julius_function()