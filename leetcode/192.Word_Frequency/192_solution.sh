#!/bin/sh
#cat words.txt | xargs -n1 | sort | uniq -c | sort -nr |awk '{print $2 " " $1}'
cat words.txt | xargs -n2 #| sort | uniq -c | sort -nr |awk '{print $2 " " $1}'
