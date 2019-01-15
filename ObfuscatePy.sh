#! /bin/bash
# =================================
VERSION="1.0"

# =================================

CURRENT_PATH=`pwd`
PROJECT_SRC_PATH=$1
ENTRY=$2

other_file(){
cd ..

for f in LICENSE logging.yml README.md requirements.txt
do
cp $PROJECT_SRC_PATH/$f sdist/dist/BattleShipGame
done
}

checkPyarmorInstall(){
if [ `pip list | grep pyarmor | wc -l` -eq 0 ] 
then
  pip install pyarmor
else 
  echo "Pyarmor already installed"
fi
}

obfuscate(){
pyarmor init --src=$PROJECT_SRC_PATH sdist
cd sdist
echo `pwd`
./pyarmor config --entry=$ENTRY --manifest="include *.py,recursive-include app *.py"
./pyarmor build

}

main(){
checkPyarmorInstall
obfuscate
other_file

cd $CURRENT_PATH
}

main
