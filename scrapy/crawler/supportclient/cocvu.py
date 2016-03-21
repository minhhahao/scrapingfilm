from crawler.utils.moduleimport import *


class cocvu:
    @classmethod
    def description(cls, value):
        if isinstance(value, list):
            data = ' '.join(value)
            try:
                result = re.search(u"(.*)<h3>B\xecnh lu\u1eadn tr\xean Facebook", data).group(1)
                return result
            except Exception as e:
                print e
