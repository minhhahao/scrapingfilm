from scrapy import Selector


class xemphimso:

    @classmethod
    def country(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            country = Selector(text=input_value).xpath(
                "//span[@class='country']//a//text()").extract()
            return country
        else:
            return

    @classmethod
    def description(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            description = Selector(text=input_value).xpath(
                "//div[@id='movie_description']//*").extract()
            return description
        else:
            return

    @classmethod
    def director(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            director = Selector(text=input_value).xpath(
                "//a[contains(./@href,'dao-dien')]//text()").extract()
            return director
        else:
            return

    @classmethod
    def film_genre(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            film_genre = Selector(text=input_value).xpath(
                "//p[@class='info_stt']/span[@class='status']//a/text()").extract()
            return film_genre
        else:
            return

    @classmethod
    def film_star(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            film_star = Selector(text=input_value).xpath(
                "//div[@class='actor-name']//text()").extract()
            return film_star
        else:
            return

    @classmethod
    def film_status(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            film_status = Selector(text=input_value).xpath(
                "//p[@class='info_stt']/span[@class='status-update']//text()").extract()
            return film_status
        else:
            return

    @classmethod
    def film_type(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            film_type = Selector(text=input_value).xpath(
                "//p[@class='info_stt']/span[@class='status-update']//text()").re("\\d+")
            return film_type
        else:
            return

    @classmethod
    def image_poster(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            image_poster = Selector(text=input_value).xpath(
                "//div[@class='cover']/div/a/img/@src").extract()
            return image_poster
        else:
            return

    @classmethod
    def name_en(cls, input_value):
        try:
            if isinstance(input_value, list):
                input_value = ''.join(input_value)
                name = Selector(text=input_value).xpath(
                    "//h1//text()")
                if len(name.re("-.*-(.*)")) > 0:
                    try:
                        name_en = str(''.join(name.re("-.*-(.*)")))
                        return name_en
                    except UnicodeEncodeError:
                        return
                elif len(name.re("-(.*)")) > 0:
                    name_en = name.re("-(.*)")
                    return name_en
                else:
                    name = name.extract()
                    if isinstance(name, list):
                        name = ''.join(name)
                        try:
                            name = str(name)
                            return name
                        except UnicodeEncodeError:
                            return
            else:
                return
        except Exception as e:
            print e

    @classmethod
    def name_vn(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            name_1 = Selector(text=input_value).xpath("//span[@itemprop='title']//text()").extract()
            try:
                name_1 = str(''.join(name_1))
                name = Selector(text=input_value).xpath(
                    "//h1//text()")
                if len(name.re("(.*-.*-.*)")) > 0:
                    try:
                        name_en = str(''.join(name.re("(.*-.*-.*)")))
                        return
                    except UnicodeEncodeError:
                        return ''.join(name.re("(.*-.*-.*)"))
                elif len(name.re("(.*)-")) > 0:
                    name_vn = name.re("(.*)-")
                    return name_vn
                else:
                    name = name.extract()
                    if isinstance(name, list):
                        name = ''.join(name)
                        try:
                            name = str(name)
                            return
                        except UnicodeEncodeError:
                            return name
            except UnicodeEncodeError:
                return ''.join(name_1)
        else:
            return

    @classmethod
    def tags(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            tags = Selector(text=input_value).xpath(
                "//div[@class='info-tag']//h3/a//text()").extract()
            return tags
        else:
            return

    @classmethod
    def year(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            year_sel = Selector(text=input_value)
            year = year_sel.xpath(
                "//span/text()").re("\\d{4}")
            return year
        else:
            return

    @classmethod
    def ishd(cls, input_value):
        if isinstance(input_value, list):
            input_value = ''.join(input_value)
            ishd = Selector(text=input_value).xpath(
                "//span[@class='status-update']//text()[contains(.,'HD')]").extract()
            return ishd
        else:
            return
