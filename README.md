ロボットシステム学2018課題1
====
マイコン:raspberry pi 3
OS:ubuntu 16.04 + ROS

## 目録
> 機能 <br>
> ディバイスドライバ説明 <br>

### 機能
* モールス信号をLEDで再現する
* morse.pyを実行して、アルファベット文字や数値を入力すると自動的にモールス信号を変換する

### ディバイスドライバ説明
* ledはraspberry piのGPIO番号を指定する(default:GPIO25)

### インストール
> 1. `sudo make`
> 2. `sudo insmod myled.ko`
> 3. `sudo chmod 666 /dev/myled0`

### アンインストール
> 1. `sudo rmmod myled`
> 2. `sudo make clean`

### 使用
* LEDをonする: `echo 1 > /dev/myled0`
* LEDをoffする: `echo 0 > /dev/myled0`
