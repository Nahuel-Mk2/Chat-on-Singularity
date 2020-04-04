# -*- coding: utf-8 -*-
import pya3rt

def api_function(message):
	apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX' # ここにAPIキーを入力する
	client = pya3rt.TalkClient(apikey)
	reply_json = client.talk(message)
	# 以下の形式でjsonが返ってくるので、replyの部分をとりだす
	# {'status': 0, 'message': 'ok', 'results': [{'perplexity': 1.2802554542585969, 'reply': 'そうですか'}]}
	if reply_json['message'] == 'ok':
		reply = reply_json['results'][0]['reply']
	else:
		reply = "reply取得に失敗しました."
	
	print("user:"+message)
	print("agent:"+reply)
	return reply


if __name__ == '__main__':
	message = "こんにちは"
	api_function(message)
