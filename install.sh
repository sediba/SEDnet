#!/bin/bash
clear

echo "Checking if you have a version of SEDnet installed...";
if [ -d "/usr/share/doc/SEDnet" ] ;
then
echo "SEDnet already has a directory. Replace it? (recommended) y/n > " ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/SEDnet"
else
 exit
fi
fi

 echo "Installing SEDnet";
 echo "";
 echo "";
 sudo git clone https://github.com/sediba/SEDnet.git /usr/share/doc/SEDnet;
 echo "#!/bin/bash 
 python3 /usr/share/doc/SEDnet/SEDnet.py" '${1+"$@"}' > sednet;
 chmod +x sednet;
 sudo cp sednet /usr/bin/;
 rm sednet;


if [ -d "/usr/share/doc/SEDnet" ] ;
then
echo "";
echo "SEDnet was successfully installed.";
echo "";
  echo "<<<====================================================================>>>";
  echo "<<<        Access the tools by typing <sednet> on the terminal         >>>"; 
  echo "<<<====================================================================>>>";
  echo "";
else
  echo "There was a problem when installing SEDnet";
  exit
fi
