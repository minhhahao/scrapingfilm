# -*- coding: utf-8 -*-
import os
import sys
import re
import csv
import subprocess
import json
import smtplib
import mimetypes
from multiprocessing import Pool
from argparse import ArgumentParser
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage


short_command = "scrapy crawl film -a config_file=%s -o %s --logfile %s"
all_command = []

"""
    Set email account
"""
FROM = "haminh.itvn@gmail.com"
TO = None
USERNAME = "haminh.itvn"
PASSWORD = "hoangminh1001101"
RESULT_FILE = "output/results.csv"
html = """\
<html>
  <head></head>
  <body>
    <p>Dear An!<br>
        Scraping film is finished!
        Please check output.
    </p>
  </body>
</html>
"""


def get_command(dir_config, dir_output):
    file_name = os.listdir(dir_config)
    for i in file_name:
        config_file = dir_config + i
        slug_file = re.search("(.*)_config.json", i).group(1)
        output_file = '%s%s_output.json' % (dir_output, slug_file)
        log_file = "%slog/%s.log" % (dir_output, slug_file)
        full_command = short_command % (config_file, output_file, log_file)
        all_command.append(full_command)
    return


def run_crawl(command):
    site_name = re.search(
        "config_file=sources/.*/(.*)_config\\.json", command).group(1)
    print "Starting crawl library '%s'" % site_name
    print "running--------------------------------"
    subprocess.call('%s' % command, shell=True)


def send_mail():
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM
        msg['To'] = TO
        msg['Subject'] = "Crawling Finished!"

        ctype, encoding = mimetypes.guess_type(RESULT_FILE)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            fp = open(RESULT_FILE)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(RESULT_FILE, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(RESULT_FILE, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(RESULT_FILE, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)

        attachment.add_header("Content-Disposition",
                              "attachment", filename=RESULT_FILE)
        part_html = MIMEText(html, 'html')
        msg.attach(part_html)
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()

        print "Successfully sent email"
    except Exception as e:
        print e


if __name__ == "__main__":
    # Option input/output
    parser = ArgumentParser()
    parser.add_argument("-i", "--input",
                        default="sources/config",
                        help="path to input json file. [Required]")
    parser.add_argument("-o", "--output",
                        default="output/",
                        help="path to output json file. [Required]")
    parser.add_argument("-p", "--processes",
                        default="1",
                        help="path to output json file. [Required]")
    parser.add_argument("-e", "--email",
                        default="minhhahao@gmail.com",
                        help="Email. [Required]")

    try:
        args = parser.parse_args()
    except Exception as e:
        print e
        parser.error("Invalid..")
        sys.exit(0)

    threading = int(args.processes)
    pool = Pool(processes=threading)  # start 2 worker processes
    get_command(dir_config=args.input, dir_output=args.output)
    if not os.path.isdir("%slog/" % args.output):
        os.mkdir("%slog/" % args.output)
    pool.map(run_crawl, all_command)
    try:
        TO = args.email
        all_output_file = os.listdir(args.output)
        all_output_json = filter(lambda x: x.endswith(".json"), all_output_file)
        with open("%s" % RESULT_FILE, "w+") as fcsv:
            f = csv.writer(fcsv)
            f.writerow(['productId', 'numberFilm'])
            for output_json in all_output_json:
                data_json = json.load(open("%s%s" % (args.output, output_json)))
                productId = re.search("(.*)_output", output_json).group(1)
                numberFilm = len(data_json)
                f.writerow([productId, numberFilm])
        send_mail()
    except Exception as e:
        print e
