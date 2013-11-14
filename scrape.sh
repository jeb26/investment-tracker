#!/bin/bash

#counters and constants
TIME_TO_SLEEP=5
TIMES_TO_SCRAPE=2
counter=0

#website to scrape
URL="http://markets.usatoday.com/custom/usatoday-com/html-mktscreener.asp"

#date command to be run multiple times
GET_DATE="date "+%Y_%m_%d_%l_%M_%S""
GET_FIELD="cut -d'_' "

#echo "year:$year month:$month day:$day hour:$hour minutes:$minutes seconds:$secs"

while [ ${counter} -lt ${TIMES_TO_SCRAPE} ]
do
	#time tokens
	year=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f1`
	month=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f2`
	day=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f3`
	hour=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f4`
	minutes=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f5`
	secs=`date "+%Y_%m_%e_%I_%M_%S" | cut -d'_' -f6`
	
	#begin webpage download with filename containing time tokens
	wget -O pages/usatoday_${year}_${month}_${day}_${hour}_${minutes}_${secs}.html $URL
	#echo ${day}${hour}
	#echo "${year}_${month}_${day}_${hour}_${minutes}_${secs}.html"

	sleep ${TIME_TO_SLEEP}
	counter=$(($counter + 1))
done
