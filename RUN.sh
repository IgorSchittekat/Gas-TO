#! /bin/bash

echo "Welcome"
echo "~Which of the following scripts would you like to run?"
echo " (See README.txt for more info on input file location)"
echo " 1) Kinepolis"
echo " 2) Visualize ADT's"
echo " 3) Both"
read -p "~Select corresponding number:" ANSWER

if [ $ANSWER = 1 ];
then
  echo $'\n'
  cd Kinepolis
  python3 Kinepolis.py
elif [ $ANSWER = 2 ];
then
  echo $'\n'
  cd Kinepolis
  python3 VisualizeADTs.py
elif [ $ANSWER = 3 ];
then
  echo $'\n'
  cd Kinepolis
  python3 Kinepolis.py
  echo $'\n'
  python3 VisualizeADTs.py
else
  echo "Invalid input"
fi
