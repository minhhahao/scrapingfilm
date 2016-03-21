import requests
import json


class hdviet:
    api_ep_url = "http://movies.hdviet.com/lay-danh-sach-tap-phim.html?id=%s"

    @classmethod
    def get_ep_avalible(cls, id_film):
        try:
            if len(id_film) > 0:
                slug = ''.join(id_film)
                url_full = hdviet.api_ep_url % slug
                try:
                    req = requests.get(url=url_full)
                    res_text = req.text
                    data = json.loads(res_text)
                    avalible_ep = data.get('Sequence')
                    total_ep = data.get("Episode")
                    if '0' in total_ep:
                        return
                    else:
                        result = "%s/%s" % (avalible_ep, total_ep)
                        return result
                except Exception as e:
                    print e
                    return
            else:
                return
        except Exception as e:
            print e
