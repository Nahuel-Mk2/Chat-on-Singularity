# -*- coding: utf-8 -*-
import subprocess
from datetime import datetime

def openjtalk_function(message):
    open_jtalk=['open_jtalk']
    # 以下openJTalkのオプション
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    allpass=['-a','0.5']
    speed=['-r','1.0']
    halftone=['-fm','0.0']
    f0=['-jf','1.0']
    outwav=['-ow','open_jtalk.wav']

    cmd=open_jtalk+mech+htsvoice+allpass+speed+halftone+f0+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(message.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','-D','plughw:2,0','open_jtalk.wav'] # plughwについては[aplay -l]で再生デバイスのcard, deviceの番号を確認する
    subprocess.Popen(aplay) # ここで発話する

def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    openjtalk_function(text)

if __name__ == '__main__':
    say_datetime()

