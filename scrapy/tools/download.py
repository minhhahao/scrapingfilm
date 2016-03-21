# -*- coding: utf-8 -*-
import re
import requests
import json
import urllib
import sys
from multiprocessing.dummy import Pool as ThreadPool
from argparse import ArgumentParser

base_url = "http://www.batdongsan.com.vn/HandlerWeb/APIAccountHandler.ashx?type=ProductDetail&productId=%s"

list_url = []
dir_save = None


def get_list_url(id_start, id_end):
    return [base_url % str(i) for i in range(int(id_start), int(id_end) + 1)]


def check_url_use(input_url):
    check_var = urllib.urlopen(input_url).getcode()
    if check_var == 200:
        return True
    else:
        return False


def download(input_url):
    print "Start download data"
    req = requests.get(url=input_url)
    resp = req.text
    data = json.loads(resp)
    return data


def write_to_file(input_url):
    data = download(input_url)
    product_id = re.search("\\d+", input_url).group()
    file_name = "%s/productId_%s.json" % (dir_save, product_id)

    print "Start write to File"
    with open(file_name, "w") as fn:
        json.dump(data, fn)
        fn.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--start",
                        default="1",
                        help="Start product ID ")
    parser.add_argument("-e", "--end",
                        default="2000000",
                        help="End product ID ")
    parser.add_argument("-p", "--processes",
                        default="2000000",
                        help="End product ID ")
    parser.add_argument("-o", "--output",
                        default="output/",
                        help="path to output json file. [Required]")

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
            print "URL Down"

    dir_save = args.output
    processes = int(args.processes)
    pool = ThreadPool(processes=processes)
    result = pool.map(write_to_file, urls)
    pool.close()
    pool.join()
