#!/bin/bash
echo start
black .
if [ $1 ]
then
git add .
fi
git commit -m  $(ls days/ | sort -Vr | head -1)
git push