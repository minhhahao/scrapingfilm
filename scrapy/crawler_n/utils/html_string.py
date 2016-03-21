import re
import requests
from lxml.html import clean

'''
Function: remove custom attrs in hml
'''


def remove_tags(html):
    try:
        kill_tags = ['a', 'img', 'strong', 'em']
        allow_tags = ['p', 'span', 'br']
        cleaner = clean.Cleaner(safe_attrs_only=True,
                                safe_attrs=frozenset(),
                                whitelist_tags=set(allow_tags),
                                remove_tags=kill_tags)
        results = cleaner.clean_html(html)
        return results
    except Exception as e:

        print e


'''
Function: add base_url to url if short url and skip if url is full url
'''


def add_base_url_to_src(base_url, input_html):
    data_output = []
    data_input = re.findall("src=\"(/\\w+/[^\"]+)", input_html)
    for data in data_input:
        if data.startswith("http"):
            data_output.append(data)
        else:
            data_output.append(base_url + data)
    return data_output


'''
Function: check url exists
'''


def check_url_use(input_url):
    try:
        check_var = requests.get(url=input_url).status_code
        if check_var == 200:
            return True
        else:
            return False
    except Exception as err:
        print err
        print "Please check input_url again!"
