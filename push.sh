#!/bin/bash
echo start
black .
if [ $1 ]
then
git add .
fi
git commit -m  $(ls days/ | sort -nr | head -1)
git push