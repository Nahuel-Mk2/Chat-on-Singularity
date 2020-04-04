# -*- coding: utf-8 -*-
import subprocess
# 以下自作関数
import my_julius

if __name__ == '__main__':
    print("##########################")
    print("!!! ALSA init !!!")
    alsactl_init = ['alsactl','init']
    w = subprocess.Popen(alsactl_init) # alsaサウンドカードドライバを初期化している(Singularity上での音声再生を有効にするため)
    w.wait()
    print("##########################")
    print("Start!")
    print("please speak")
    my_julius.julius_function()
