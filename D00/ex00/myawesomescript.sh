#!/bin/sh
if [ ! -z $1 ] ; then 
	curl --silent bit.ly/1O72s3U | grep 'href' | cut -d '"' -f 2
fi
