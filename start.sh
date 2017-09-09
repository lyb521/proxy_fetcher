#!/bin/bash
cd `dirname $0`

scrapy crawl xici --logfile=log --loglevel=WARNING

scrapy crawl mimiip --logfile=log --loglevel=WARNING

scrapy crawl ipbus --logfile=log --loglevel=WARNING

scrapy crawl kdl --logfile=log --loglevel=WARNING

scrapy crawl goubanjia --logfile=log --loglevel=WARNING

scrapy crawl ip3366 --logfile=log --loglevel=WARNING
