## buildozer init:

### buildozer install:


normal:
```sh
pip3 install --user --upgrade buildozer
```

forced (make this out off from a virtualenv):
```sh
## [deb] ##
sudo apt update

#Ubuntu
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential libstdc++6 aidl 

#Kali
sudo apt install -y git zip unzip default-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential libstdc++6 aidl 

#installing the cython
pip3 install Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

#installing the java-sdk on the kali linux
sudo apt install -y default-jdk -y

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/

#now, install the buildozer using the pip3
pip3 install --user --upgrade buildozer
```
<hr>
<br>

### creating buildozer.spec file from zero:
```sh
buildozer init
```

### create the buildozer file with your specifications, and start the android/debug build using (out off from venv):
```sh
buildozer -v android debug deploy run logcat

buildozer android deploy run logcat
```
save the logs with:
```sh
 > my_log.txt
```

