import json
import csv
import sys
import os
from multiprocessing import Pool
from argparse import ArgumentParser

INPUT_FILE = None
OUTPUT_DIR = None

ALLOW_FIELDS = ["country", "description", "director", "film_genre", "film_star",
                "film_status", "film_type", "image_poster", "ishd", "name_en",
                "name_vn", "product_name", "product_url", "sub", "tags", "year"]


def write_to_csv(input_json):
    try:
        with open(input_json) as jip:
            data_input = json.load(jip)
            if OUTPUT_DIR is None:
                data_output = "%s%s" % (OUTPUT_DIR, input_json.replace("json", "csv"))
            else:
                data_output = "%s" % (input_json.replace("json", "csv"))
            with open(data_output, "w+") as cop:
                f = csv.writer(cop)
                f.writerow(ALLOW_FIELDS)
                for data in data_input:
                    data_unicode = [data.get(i) for i in ALLOW_FIELDS]
                    data_str = []
                    for j in data_unicode:
                        if j is not None:
                            j = j.encode("utf-8")
                            data_str.append(j)
                        else:
                            data_str.append(j)
                    f.writerow(data_str)
    except Exception as e:
        print "Invalid json: %s" % input_json
        print e


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", default="output/",
                        help="Path to input json. [Required]")
    parser.add_argument("-o", "--output", default="output/",
                        help="Path to output csv. [Required]")
    parser.add_argument("-p", "--process", default="1",
                        help="Set process [Required]")

    try:
        args = parser.parse_args()
    except Exception as e:
        print e
        parser.error("Invalid json")
        sys.exit(0)

    # checking input file or folder
    if args.input.endswith(".json"):
        INPUT_FILE = args.input
    elif os.path.isdir(args.input):
        if not args.input.endswith("/"):
            args.input = "%s/" % args.input
        INPUT_FILE = filter(lambda x: x.endswith(".json"), [
                            "%s%s" % (args.input, json_file)
                            for json_file in os.listdir(args.input)])
    else:
        print "Please check input again!"
        print "Input file must is json file or file json on folder"

    # checking output file or folder
    if os.path.isdir(args.output):
        if not args.output.endswith("/"):
            OUTPUT_DIR = "%s/" % args.output
        OUTPUT_DIR = args.output
    else:
        os.makedirs(args.output)
        OUTPUT_DIR = args.output

    process = int(args.process)
    if isinstance(INPUT_FILE, str):
        write_to_csv(INPUT_FILE)
    elif isinstance(INPUT_FILE, list):
        pool = Pool(processes=process)
        pool.map(write_to_csv, INPUT_FILE)
