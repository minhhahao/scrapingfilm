from crawler.utils.html_string import *


class FormatData:

    def __init__(self):
        pass

    '''
    Function: Format description field
    '''

    @staticmethod
    def description(self, input_value):

        html_desc = None
        html_desc_list = []
        if isinstance(input_value, list):
            for input_v in input_value:
                html_desc_list.append(remove_tags(input_v))
                html_desc = ' '.join(html_desc_list)
            return html_desc

        elif isinstance(input_value, unicode):
            return remove_tags(input_value)
        else:
            return

    '''
    Function: Format film_type field
    '''

    @staticmethod
    def film_type(self, input_value):
        if input_value is None:
            return "Phim le"
        if len(input_value) > 0:
            return "Phim bo"
        else:
            return "Phim le"

    '''
    Function: Format name_en, name_vn field
    '''

    @staticmethod
    def name(self, input_value):
        if isinstance(input_value, list):
            return ''.join(input_value)
        elif isinstance(input_value, str):
            return input_value
        elif isinstance(input_value, unicode):
            return input_value.encode("utf-8")
        else:
            return

    '''
    Function: Format country field
    '''

    @staticmethod
    def country(self, input_value):
        if len(input_value) > 0:
            return input_value[0]
        else:
            return

    '''
    Function: Format ishd field
    '''

    @staticmethod
    def ishd(self, input_value):
        if len(input_value) > 0:
            return "1"
        else:
            return

    '''
    Function: Format image_urls field
    '''

    @staticmethod
    def image_urls(self, input_value):

        results = []
        if len(input_value) > 0:
            for url in input_value:
                url = url.encode('utf-8', 'ignore')
                if url.startswith('http'):
                    # check url exist
                    if check_url_use(url):
                        results.append(url)
                else:
                    full_url = self.base_url + url
                    # check url exist
                    if check_url_use(input_url=full_url):
                        results.append(full_url)

            return '; '.join(results)
        else:
            return

    '''
    Function: Format film_status field
    '''

    @staticmethod
    def film_status(self, input_value):
        try:
            if len(input_value) > 0:
                input_value = ''.join(input_value)
                if 'p' in input_value:
                    return input_value
                else:
                    input_value = 'Tap %s' % input_value
                    return input_value
            else:
                return

        except Exception as e:
            print e
    '''
    Function: Format year field
    '''

    @staticmethod
    def year(self, input_value):
        if len(input_value) > 0:
            return input_value[0]
        else:
            return

    '''
    Function: Format sub field
    '''

    @staticmethod
    def sub(self, input_value):
        if len(input_value) > 0:
            return "1"
        else:
            return "0"

    '''
    Function: Format other field
    '''

    @staticmethod
    def other(self, input_value):
        if len(input_value) > 0:
            return '; '.join(input_value)
        else:
            return None
