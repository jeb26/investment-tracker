#!/bin/bash

#website to scrape
URL="http://markets.usatoday.com/custom/usatoday-com/html-mktscreener.asp"

#tokens for the filename
year=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f1`
month=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f2`
day=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f3`
hour=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f4`
minutes=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f5`
secondss=`date "+%Y_%m_%d_%l_%M_%S" | cut -d'_' -f6`

#echo "year:$year month:$month day:$day hour:$hour minutes:$minutes seconds:$secs"

#counters and constants
MINUTE=60
counter=0
while [ $counter -lt 2 ]
do
	wget -O usatoday_${year}__${month}_${day}_${hour}_${minutes}_${seconds}.html $URL
	sleep $MINUTE
	counter=$(($counter + 1))
done
