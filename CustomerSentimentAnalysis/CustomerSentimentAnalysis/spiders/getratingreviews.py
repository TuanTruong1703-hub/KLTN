import scrapy
import requests
import pandas as pd
import numpy as np
import time
import json


class APIProductClass(object):
    def API_HEADERS(itemid, shopid, dem):
        api = f"https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid={itemid}&limit=6&offset={dem*6}&shopid={shopid}&type=0"

        headers = {
            "Cookie": "_gcl_au=1.1.1889080692.1613720007; _fbp=fb.1.1613720010486.1130357992; csrftoken=HqRO6RzbYr8L8jat6o0snEkY10UBrf1r; REC_T_ID=c45ae345-7284-11eb-b342-3c15fb3af3aa; SPC_SI=bfftocvn.QqSLQfiOAkVrEjhIhWsTUlR03osZQ3Kb; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=x3z9IEfriOqKQ906EJw89rb0YCs6WUv3; welcomePkgShown=true; _hjid=f895f87b-39b8-46f6-80d8-492719434759; _hjFirstSeen=1; _gid=GA1.2.979129240.1613720026; _hjAbsoluteSessionInProgress=0; SPC_CT_eef172bc='1613720961.VF4ideeuX3ALuy2nIXO371VPX69ccm6e1s6DWgB1HJ8='; SPC_CT_0ad6b9e8='1613723130.1JX20izhVzQ+LA+7UZA2izfnSb8BTVjOE6DRvwRQKbQ='; AMP_TOKEN=%24NOT_FOUND; SPC_CT_0d862251='1613723993.OqCkRDr7NYMygA/beu+sBESEn9iDFU6hgnht2/jTv90='; _dc_gtm_UA-61914164-6=1; cto_bundle=vmg3hV9HQ3BpdnhRNmhneWlXeWpsbVl2cWZGREZFbE1zWDVlZW9LJTJCU2glMkJTdmNBenJoYmhpaFUlMkYwQ2ZRSDI1WUFpSUdOWW0zYUpiSnVVSU5ZcllMV09xWExTVkpsdSUyQkQ0WFhEWGFxeVZVY3poJTJGMTRwVWNxa2ZUNG9icnZVeFlSUTRNS25tNVRpRWowTWpENEglMkJkWnNuTGk4VHclM0QlM0Q; _ga=GA1.2.346080001.1613720023; _ga_M32T05RVZT=GS1.1.1613723132.2.1.1613724467.15; SPC_R_T_ID='Fid+AuVVtFMzMGPDsYoQayVEmkC/5ra19tMU0DzuAQMDC9RnPvnaX+wHVuMjWtQGY+jjW/CnQqv1A6DN1j5aeCJ8dC8GYfTB62FWh+MVU5o='; SPC_T_IV='mtf/NT8IUapw8Y+EcgRoNw=='; SPC_R_T_IV='mtf/NT8IUapw8Y+EcgRoNw=='; SPC_T_ID='Fid+AuVVtFMzMGPDsYoQayVEmkC/5ra19tMU0DzuAQMDC9RnPvnaX+wHVuMjWtQGY+jjW/CnQqv1A6DN1j5aeCJ8dC8GYfTB62FWh+MVU5o='",
            "X-Api-Source": "pc",
        }
        return {
            "api": api,
            "headers": headers,
        }


class ShopeeapiSpider(scrapy.Spider):
    name = "api_comment"
    allowed_domains = ["shopee.vn"]
    start_urls = ["https://shopee.vn/"]

    def parse(self, response):
        # # 1. Comment mặc hàng điện tử
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036132&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"

        # #    2. Comment mặc hàng mỹ phẩm
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036279&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"

        # # 3. Comment mặc hàng về sức khỏe
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036345&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"

        # # 4.  Comment mặc hàng nhà cửa và đời sống
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036670&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"

        # # 5. Comment mặc hàng mẹ và bé
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036194&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 6. Thời trang nam
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035567&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 7. Thời trang nữ
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035639&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # 8. Giày dép nữ
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035825&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 9. Giày dép nam
        url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035801&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 10. Máy tính laptop
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035954&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 11.Điện thoại phụ kiện
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036030&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 12.Túi ví nữ
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035761&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 13.Phụ kiện trang sức nữ
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035853&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 14.Đồng hồ
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035788&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 15.Thể thao du lịch
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11035478&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 16. Bách hóa online
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036525&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 17. Nhà sách online
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036863&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # 18. Ô tô xe máy xe đạp
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036793&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        headers = {
            "cookie": "SPC_PC_HYBRID_ID=84; csrftoken=yfXVW13rQpK3DzcXrQVd7HxVy0CQiLby; SPC_IA=-1; SPC_EC=-; SPC_U=-; REC_T_ID=3908e25e-ca61-11eb-bda5-b49691a184d6; SPC_SI=mall.Bzx0PwZeSVAFgIHB9hbnMNkCj0tT058y; REC_T_ID=3907c5e8-ca61-11eb-8919-2cea7f90b8dd; SPC_F=5YYHYE2NhmeGDFsZy2bENJdo7uWXmG8G; _gcl_au=1.1.986783983.1623380447; _med=refer; welcomePkgShown=true; _fbp=fb.1.1623380447884.2089297794; _hjid=73079271-761f-45ec-8ec3-d29b2bfbff00; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1801455669.1623380448; _gid=GA1.2.1367985147.1623380449; _dc_gtm_UA-61914164-6=1; cto_bundle=H55KnF9yZTYxY0d0dnFLdE1RM2RwR0JEUHYlMkZkd3h3Z2dMTFJlTUxlWjhyMzRyazNyY3JRUlZzcG1sdUZHNFFiNFk0JTJGN3FQMkV5N3p4OEVOUDNhNlFhaFBrZFAySUtvcVBrTFZKd1gxVTBzV1NNWjMzWSUyRklpOTcyY1N4ZFpPTCUyQmdPNXls; _ga_M32T05RVZT=GS1.1.1623380448.1.1.1623380474.34; SPC_R_T_ID='9BWkgUMYI/LFWBSrJ7kZ6ZVO8q+dubLBe7ZYTZKFZHDajgfOT0KQgUcqBIPsqLafhHDj2EN0S8AKARyq1b6V/wuwmCuA0brj6NP9j1OOAnI='; SPC_T_IV='eu1JKxgz1uPp2DJ5FxaVMg=='; SPC_R_T_IV='eu1JKxgz1uPp2DJ5FxaVMg=='; SPC_T_ID='9BWkgUMYI/LFWBSrJ7kZ6ZVO8q+dubLBe7ZYTZKFZHDajgfOT0KQgUcqBIPsqLafhHDj2EN0S8AKARyq1b6V/wuwmCuA0brj6NP9j1OOAnI='"
        }
        respons = requests.request("GET", url, headers=headers).json()
        for item in respons["items"]:
            itemid = item["itemid"]
            shopid = item["shopid"]

            url_api = APIProductClass.API_HEADERS(itemid, shopid, 0)
            yield response.follow(
                url=url_api["api"],
                callback=self.parse_comment,
                headers=url_api["headers"],
                meta={"itemid": itemid, "shopid": shopid, "dem": 0},
            )

    def parse_comment(self, response):
        itemid = response.request.meta["itemid"]
        shopid = response.request.meta["shopid"]
        dem = int(response.request.meta["dem"]) + 1

        resp = json.loads(response.body)
        for item in resp["data"]["ratings"]:
            yield {
                "Time": time.ctime(int(item["ctime"])),
                "reviews_id": item["cmtid"],
                "Reviews": item["comment"],
                "id_user": item["userid"],
                "user name": item["author_username"],
                "order_id": item["orderid"],
                "items_id": itemid,
                "shop_id": item["shopid"],
                "rating status": item["rating"],
                "scores": item["rating_star"],
                "shipping": item["sip_info"]["origin_region"],
            }

        if (dem <= 10000):
            url_api = APIProductClass.API_HEADERS(itemid, shopid, dem)
            yield response.follow(
                url=url_api["api"],
                callback=self.parse_comment,
                headers=url_api["headers"],
                meta={"itemid": itemid, "shopid": shopid, "dem": dem},
            )
