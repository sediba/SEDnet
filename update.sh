#
# ____  _____ ____             _                      _    _             
#/ ___|| ____|  _ \ _ __   ___| |___      _____  _ __| | _(_)_ __   __ _ 
#\___ \|  _| | | | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / | '_ \ / _` |
# ___) | |___| |_| | | | |  __/ |_ \ V  V / (_) | |  |   <| | | | | (_| |
#|____/|_____|____/|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\_|_| |_|\__, |
#                                                                  |___/ 
#

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/SEDnet/

clear

cd /etc/

clear

sudo rm -rf /etc/sediba

clear

mkdir sediba

clear

cd sediba

clear

git clone https://github.com/sediba/SEDnet.git

clear

cd SEDnet

clear

sudo chmod +x install.sh

clear

./install.sh

clear
