#!/bin/bash
set -u
min=0
max=2147483647
while [ $min -le $max ];
do
	mid=$((min+(max-min)/2))
	./prob1 $mid
	check=$?

	if [ $check -eq 2 ];then 
		min=$mid 
	elif [ $check -eq 1 ];then 
		max=$mid
	else 
		break
	fi
done
