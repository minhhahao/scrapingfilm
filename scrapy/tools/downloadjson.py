# -*- coding: utf-8 -*-
import re
import requests
import json
import sys
import time
import os
from multiprocessing.dummy import Pool as ThreadPool
from argparse import ArgumentParser

BASE_URL = "http://www.batdongsan.com.vn/HandlerWeb/APIAccountHandler.ashx?type=ProductDetail&productId=%s"
HTTP_PROXY = None
TIME_SLEEP = None
OUTPUT = None
PROXY_DICT = None
"""
Script download json file from url!
Library using: requests.
Install requests by pip: sudo pip install requests
Run script: python download.py -s <start_id> -e <end_id> -o <output_dir>
More option:
    -ps <number_process>
    -px <http_proxy>
    -t <time_sleep_seconds>
Example:
    python download.py -s 12 -e 24 -o output -ps 3 -px 124.120.127.19:8888 -t 2
We download for id 12 to id 24 with 3 cpu.
Using proxy: 124.120.127.19:8888, time sleep 2 second.
Final data save to output

Note: If url disable, it will save to log.txt on output directory
"""


# Function list all url can download
def get_list_url(id_start, id_end):
    return [BASE_URL % str(i) for i in range(int(id_start), int(id_end) + 1)]


# Function check url available
def check_url_use(input_url):
    try:
        check_var = requests.get(url=input_url, proxies=PROXY_DICT).status_code
        if check_var == 200:
            return True
        else:
            return False
    except Exception as err:
        print err
        print "Please check input_url again!"


# Function get data from url
def download(input_url):
    time.sleep(TIME_SLEEP)
    print "Starting download data from %s" % input_url
    try:
        req = requests.get(url=input_url, proxies=PROXY_DICT)
        resp = req.text
        data = json.loads(resp)
        return data
    except Exception as e:
        print e
        print "Invalid Json!"
        return


# Function write url fail to log
def write_to_log(data):
    log_file = "%s/log.txt" % OUTPUT
    with open(log_file, "a+") as lgf:
        lgf.write(data)
        lgf.write("\n")
        lgf.close()


# Function write data to output file
def write_to_file(input_url):
    data = download(input_url)
    if data is not None:
        product_id = re.search("\\d+", input_url).group()
        file_name = "%s/productId_%s.json" % (OUTPUT, product_id)
        print "Url %s downloaded at %s" % (input_url, file_name)
        with open(file_name, "w+") as fn:
            json.dump(data, fn)
            fn.close()
    else:
        print "Can't download url: %s" % input_url
        message_err = "Url: %s down" % input_url
        write_to_log(message_err)


# Function check output directory exist
def output_file(input_value):
    if input_value.endswith("/"):
        print "Please remove '/' characters in option output"
        return
    else:
        if not os.path.isdir(input_value):
            os.makedirs(input_value)
        return input_value


# Main
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--start",
                        default="1",
                        help="Start product ID [Required]")
    parser.add_argument("-e", "--end",
                        default="2000000",
                        help="End product ID [Required]")
    parser.add_argument("-ps", "--processes",
                        default="1",
                        help="Set processes .[Required]")
    parser.add_argument("-o", "--output",
                        default="output/",
                        help="Path to output json file [Required]")
    parser.add_argument("-t", "--timesleep",
                        default="0",
                        help="Set time sleep between with downloads [Required]")
    parser.add_argument("-px", "--proxy",
                        default=None,
                        help="Set http proxy [Required]")

    try:
        args = parser.parse_args()
    except Exception as e:
        print e
        parser.error("Invalid..")
        sys.exit(0)

    list_url = get_list_url(id_start=args.start, id_end=args.end)
    urls = []
    for url in list_url:
        if check_url_use(url):
            urls.append(url)
        else:
            message_err = "Url: %s down" % url
            write_to_log(message_err)
    if args.proxy:
        HTTP_PROXY = "http://%s" % args.proxy
        PROXY_DICT = {"http": HTTP_PROXY}

    TIME_SLEEP = int(args.timesleep)
    OUTPUT = output_file(input_value=args.output)
    processes = int(args.processes)
    pool = ThreadPool(processes=processes)
    result = pool.map(write_to_file, urls)
    pool.close()
    pool.join()
