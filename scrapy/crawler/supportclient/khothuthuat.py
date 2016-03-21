from crawler.utils.moduleimport import *


class khothuthuat:
    @classmethod
    def description(cls, value):
        if isinstance(value, list):
            # filter 'adsbygoogle = window.adsbygoogle || []).push({});\r' from value list
            # value = filter(lambda x: x != u'adsbygoogle = window.adsbygoogle || []).push({});\r', value)

            # get result
            data = ' '.join(value)
            try:
                import pdb
                pdb.set_trace()
                result = re.search(u"(.*)<strong>T\xecm ki\u1ebfm ph\u1ed5 bi\u1ebfn", data).group(1)
                return result
            except Exception as e:
                print e
                return data
