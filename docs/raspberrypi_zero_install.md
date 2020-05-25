Install DietPi on raspberry pi zero

1. Download img from https://dietpi.com/
2. Install to sd card with balenaEtcher
3. Edit dietpi.txt
```
##### Networking Options #####
AUTO_SETUP_NET_ETHERNET_ENABLED=0
AUTO_SETUP_NET_WIFI_ENABLED=1
```
4. Edit dietpi-wifi.txt
```
# - Entry 0
aWIFI_SSID[0]='xxx'
aWIFI_KEY[0]='xxx'
```

 Boot raspberry pi

 1. switch ssh to OpenSSH
 2. Enable I2C (Advanced Options)
 3. Set editor vim (programs)
 4.. Add pi user 
 ```
 adduser pi
 ```
 4. usermod -aG sudo username
 5. add to visudo
 ```
 pi  ALL=(ALL) NOPASSWD:ALL
 ```
 5. install git 
 ```
 sudo apt install git
 ```
 6. generate ssh key
 ```
 ssh-keygen
 ```
 7. copy keys to github/bitbucket

8. create ~/repos folder
9. git clone git@bitbucket.org:hummel22/smart_home.git
9 sudo apt instal pipenv


It may be necessary to set the following values to ley pipenv install work
```
export PIPENV_TIMEOUT=9999
export  PIPENV_INSTALL_TIMEOUT=9999
```

10. sudo apt-get install libgpiod2
