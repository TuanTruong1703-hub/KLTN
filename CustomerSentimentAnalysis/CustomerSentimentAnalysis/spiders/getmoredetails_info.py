import scrapy
import requests
import pandas as pd
import numpy as np
import time
import json


class APIShopClass(object):
    def API_HEADERS(shopid):
        api = f"https://shopee.vn/api/v4/product/get_shop_info?shopid={shopid}"

        headers = {
            "Cookie": "_gcl_au=1.1.1998224720.1641870990; _med=refer; REC_T_ID=decf295d-728c-11ec-bcee-f20e94dc7543; SPC_F=zex0RMAuwcy2e4pD9GAYcpxqbHE25jOo; SPC_IA=-1; SPC_EC=-; SPC_U=-; _fbp=fb.1.1641870990232.950255945; _hjSessionUser_868286=eyJpZCI6IjEwNGNjMGVhLTQxNTYtNTczMS05MWQ1LTQ3YmZiMzNjYmY0ZiIsImNyZWF0ZWQiOjE2NDE4NzA5OTE2MTUsImV4aXN0aW5nIjp0cnVlfQ==; SPC_SI=bfftocsg9.rYjpeplVlwMZbvvBA4cyykiVkP6deVTF; csrftoken=empUnoIZUJy894lFjVLBlGAH5t9ZZfQh; _QPWSDCXHZQA=d80ce467-4a89-4d11-ba50-d3bccf475e70; _gid=GA1.2.302893168.1641963997; _hjSession_868286=eyJpZCI6ImJlZTFlNDVhLTY3ZmMtNDE5NC1hZTllLTVhZTliNjFlZjk3OSIsImNyZWF0ZWQiOjE2NDE5ODQ4Mzc0MzIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; cto_bundle=E2477l9ldlYzV3U2ckltRDBDSlhwdE8lMkIyaE1mcUE5ekRHV2ZDRURYb1NlNVMzcW1CU29Pb3N0VzBiZ25KcEE1T0RVQVl3cUE1UU9XblRUR3lmWlVkU1dWOGM0TDhvdWt3V29xcjROaTJsbFJaJTJGOXNLZDNGJTJCTnRnQmZ5NmJ6MWtDbiUyQll4JTJCWmhPYlglMkZpQjhWVDVmU0Z6WUxsQXclM0QlM0Q; shopee_webUnique_ccd=MONoBKVCCsA5IC8Te/Ik6w==|f8Y8Npti8vV89jtXqhxvlUL3J26LKtMH1UIflI3Enkzq38fKE23Ibx2uP+Xu4UT5JE91i3qYgSDa1f5LivfO|ylY1faD1+5jThlCo|04|3; AMP_TOKEN=$NOT_FOUND; _ga=GA1.2.1287493862.1641870991; _dc_gtm_UA-61914164-6=1; _ga_M32T05RVZT=GS1.1.1641984836.4.1.1641984858.38; SPC_T_IV="'Ia9RxpmYJecsCuxN0ZGRmA=='"; SPC_T_ID="'KZnpAQs8QINeinjnEiEJRnHiX+o3egySf3AT0tt+lOeCLDSGD33DXKO435JP79yk0y0v8ddM6pwULlhFkjQpcISAtc07M2budMG7tHRSMEU='"",
            "X-Api-Source": "pc",
        }
        return {
            "api": api,
            "headers": headers,
        }


class ShopeeapiSpider(scrapy.Spider):
    name = "api_itemandshop_info"
    allowed_domains = ["shopee.vn"]
    start_urls = ["https://shopee.vn/"]

    def parse(self, response):
        # Mặc hàng điện tử
        url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=    &newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        # # Mặc hàng mỹ phẩm
        # url = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036279&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
        headers = {
            "cookie": "SPC_PC_HYBRID_ID=84; csrftoken=yfXVW13rQpK3DzcXrQVd7HxVy0CQiLby; SPC_IA=-1; SPC_EC=-; SPC_U=-; REC_T_ID=3908e25e-ca61-11eb-bda5-b49691a184d6; SPC_SI=mall.Bzx0PwZeSVAFgIHB9hbnMNkCj0tT058y; REC_T_ID=3907c5e8-ca61-11eb-8919-2cea7f90b8dd; SPC_F=5YYHYE2NhmeGDFsZy2bENJdo7uWXmG8G; _gcl_au=1.1.986783983.1623380447; _med=refer; welcomePkgShown=true; _fbp=fb.1.1623380447884.2089297794; _hjid=73079271-761f-45ec-8ec3-d29b2bfbff00; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1801455669.1623380448; _gid=GA1.2.1367985147.1623380449; _dc_gtm_UA-61914164-6=1; cto_bundle=H55KnF9yZTYxY0d0dnFLdE1RM2RwR0JEUHYlMkZkd3h3Z2dMTFJlTUxlWjhyMzRyazNyY3JRUlZzcG1sdUZHNFFiNFk0JTJGN3FQMkV5N3p4OEVOUDNhNlFhaFBrZFAySUtvcVBrTFZKd1gxVTBzV1NNWjMzWSUyRklpOTcyY1N4ZFpPTCUyQmdPNXls; _ga_M32T05RVZT=GS1.1.1623380448.1.1.1623380474.34; SPC_R_T_ID='9BWkgUMYI/LFWBSrJ7kZ6ZVO8q+dubLBe7ZYTZKFZHDajgfOT0KQgUcqBIPsqLafhHDj2EN0S8AKARyq1b6V/wuwmCuA0brj6NP9j1OOAnI='; SPC_T_IV='eu1JKxgz1uPp2DJ5FxaVMg=='; SPC_R_T_IV='eu1JKxgz1uPp2DJ5FxaVMg=='; SPC_T_ID='9BWkgUMYI/LFWBSrJ7kZ6ZVO8q+dubLBe7ZYTZKFZHDajgfOT0KQgUcqBIPsqLafhHDj2EN0S8AKARyq1b6V/wuwmCuA0brj6NP9j1OOAnI='"
        }
        respons = requests.request("GET", url, headers=headers).json()
        for item in respons["items"]:

            item_id = item["item_basic"]['itemid']
            shop_id = item["item_basic"]['shopid']
            item_name = item["item_basic"]['name']
            item_status = item["item_basic"]['item_status']
            category_id = item["item_basic"]['catid']
            price = item["item_basic"]['price']
            price_before_discount = item["item_basic"]['price_before_discount']
            price_max = item["item_basic"]['price_max']
            price_max_before_discount = item["item_basic"]['price_max_before_discount']
            price_min = item["item_basic"]['price_min']
            price_min_before_discount = item["item_basic"]['price_min_before_discount']
            raw_discount = item["item_basic"]['raw_discount']
            sold = item["item_basic"]['sold']
            stock = item["item_basic"]['stock']
            historical_sold = item["item_basic"]['historical_sold']
            url_api_shop = APIShopClass.API_HEADERS(shop_id)
            yield response.follow(
                url=url_api_shop["api"],
                callback=self.parse_products,
                headers=url_api_shop["headers"],
                meta={
                    "itemname": item_name,
                    "item_status": item_status,
                    "item_id": item_id,
                    "shop_id": shop_id,
                    "category_id": category_id,
                    "price": price,
                    "price_before_discount": price_before_discount,
                    "price_max": price_max,
                    "price_max_before_discount": price_max_before_discount,
                    "price_min": price_min,
                    "price_min_before_discount": price_min_before_discount,
                    "raw_discount": raw_discount,
                    "sold": sold,
                    "stock": stock,
                    "historical_sold": historical_sold,
                    "dem": 0},
            )

    def parse_products(self, response):
        itemid = response.request.meta["item_id"],
        shopid = response.request.meta["shop_id"],
        itemname = response.request.meta["itemname"],
        item_status = response.request.meta["item_status"],
        categoryid = response.request.meta["category_id"],
        price = response.request.meta["price"],
        price_before_discount = response.request.meta["price_before_discount"],
        price_max = response.request.meta["price_max"],
        price_max_before_discount = response.request.meta["price_max_before_discount"],
        price_min = response.request.meta["price_min"],
        price_min_before_discount = response.request.meta["price_min_before_discount"],
        raw_discount = response.request.meta["raw_discount"],
        sold = response.request.meta["sold"],
        historical_sold = response.request.meta["historical_sold"],
        stock = response.request.meta["stock"],
        dem = int(response.request.meta["dem"]) + 1

        resp = json.loads(response.body)
        yield {
            "id_shop": shopid,
            "id_product": itemid,
            "item_name": itemname,
            "item_status": item_status,
            "category_id": categoryid,
            "price": price,
            "price_before_discount": price_before_discount,
            "price_max": price_max,
            "price_max_before_discount": price_max_before_discount,
            "price_min": price_min,
            "price_min_before_discount": price_min_before_discount,
            "raw_discount": raw_discount,
            "sold": sold,
            "historical_sold": historical_sold,
            "stock": stock,
            'shop_name': resp['data']['name'],
            "Average rating score": resp["data"]["rating_star"],
            "Official Status": resp["data"]["is_official_shop"],
            'shop_location': resp['data']['shop_location'],
            "Response time": resp["data"]["response_time"],
            "Response rating": resp["data"]["response_rate"],
            "Follower": resp["data"]["follower_count"],

        }
