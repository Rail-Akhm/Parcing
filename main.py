import requests
import json

def get_data():
    pass
    import requests

    cookies = {
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityDE_17326',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20953839895',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '1100000700000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '102',
        'MVID_REGION_SHOP': 'S964',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '3',
        'SMSError': '',
        'authError': '',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_ym_uid': '1656341328425402922',
        '_ym_d': '1656341328',
        'tmr_lvidTS': '1656341327834',
        'tmr_lvid': 'c8039c6d453b074f907e2709a13504e0',
        'flocktory-uuid': 'e6665b06-a6f8-4c9f-895d-7a6270c00a69-7',
        'BIGipServeratg-ps-prod_tcp80': '2466569226.20480.0000',
        'bIPs': '-314595793',
        'afUserId': '271eb940-f151-451a-b5a8-7f61ae61942f-p',
        'uxs_uid': '4203e900-f628-11ec-8763-6d3b2d8e9f7d',
        '__ttl__widget__ui': '1656341468657-55f252b0d511',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2466569226.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        '__lhash_': 'd2a3cf994160eb5d3e6ad12c682f2c1e',
        'JSESSIONID': 'fXPYvSpMpp2BL0c2GypqpJvY7VJ9HLpXvfkTJ1JHLtTJLJT1YwLn!1659720574',
        'MVID_CART_AVAILABILITY': '1',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_SUPER_FILTERS': 'false',
        '_gid': 'GA1.2.448330780.1657982342',
        '_ym_isad': '2',
        'advcake_track_id': '80596a6f-9225-8c5d-e49a-7e8ffd401a32',
        'advcake_session_id': '090e9c6b-ca44-23a1-f2c1-9deb87ce2415',
        'AF_SYNC': '1657982345659',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfYw1GLWohPAsdTxNBGUR5CmwXSEt1C2p0IUNEfTknbydVfnlnej8xLUMXPWshL1xmEBE5GjxrImhOWx9IXFFqJh8WfnQrWAwMYURIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDBEbR9iTlwjSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=Ev8syw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfYw1GLWohPAsdTxNBGUR5CmwXSEt1C2p0IUNEfTknbydVfnlnej8xLUMXPWshL1xmEBE5GjxrImhOWx9IXFFqJh8WfnQrWAwMYURIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDBEbR9iTlwjSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=Ev8syw==',
        'cfidsgib-w-mvideo': 'lZdSj6EHQn8jokpCLeuW0stGp9XceOEOE84196gHnYAz68EEnqhWQcZN6O/zY6OHSS78mZFEooySTiW/ggGjQaWixiob0iSl4N4uzeyI7cI1+xBaAINyfvZjyxS6aSTYWrZluS0GO9tEXzI7ABHTTm2ZHInKOYfjdsfP',
        'cfidsgib-w-mvideo': 'lZdSj6EHQn8jokpCLeuW0stGp9XceOEOE84196gHnYAz68EEnqhWQcZN6O/zY6OHSS78mZFEooySTiW/ggGjQaWixiob0iSl4N4uzeyI7cI1+xBaAINyfvZjyxS6aSTYWrZluS0GO9tEXzI7ABHTTm2ZHInKOYfjdsfP',
        'gsscgib-w-mvideo': 'azUxCJd2k/bOJuJW37PL+/QEPrzRtxiKTS9aHnLRfS2G5dtCwTjyTIXPD77MphDHneihPFL4tUdiwFuSNIPYq0M7vXHq9NCv7wTVXOKY0oQsZ4NjM2XuZMY/x1jUcznulLH6h9foj6275frrLkArGoa5E1NcVOa2NXsWCoyMsIKMGqTkXd2yXaIixLLoRQyzJwHBiw/4eQddgclKDY9yi5dg80nuCX/ODHJ9VyqDwKqr6erCd7TBZ2ooiXtTrA==',
        'gsscgib-w-mvideo': 'azUxCJd2k/bOJuJW37PL+/QEPrzRtxiKTS9aHnLRfS2G5dtCwTjyTIXPD77MphDHneihPFL4tUdiwFuSNIPYq0M7vXHq9NCv7wTVXOKY0oQsZ4NjM2XuZMY/x1jUcznulLH6h9foj6275frrLkArGoa5E1NcVOa2NXsWCoyMsIKMGqTkXd2yXaIixLLoRQyzJwHBiw/4eQddgclKDY9yi5dg80nuCX/ODHJ9VyqDwKqr6erCd7TBZ2ooiXtTrA==',
        'fgsscgib-w-mvideo': 'KQu2a52f4fc395e25487cad9a9badfa53718a699',
        'fgsscgib-w-mvideo': 'KQu2a52f4fc395e25487cad9a9badfa53718a699',
        'cfidsgib-w-mvideo': 'lDpxZgsC1VDUPMYtWqFthESnFXrngPMdPzgtbn7enrmuVe3bHpt8IpoHzP4Cd6JCsPVIQvQiMwjDxH7VAIvj6RhuKVB0WGXUp/57yhiNS48GY5VCil/XDax9YNUJRMEN8gcg5hXcM70pBqViYfbEe+SgHBvJ65icMnvX',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': '5683bc04-1432-440b-92ff-49fa22ce6917',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225683bc04-1432-440b-92ff-49fa22ce6917%22%7D',
        '_ga': 'GA1.2.194096916.1656341327',
        'tmr_detect': '1%7C1657982389229',
        'MVID_ENVCLOUD': 'prod2',
        'tmr_reqNum': '110',
        '_ga_CFMZTSS5FM': 'GS1.1.1657982341.2.1.1657982621.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1657982341.2.1.1657982621.60',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityDE_17326; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20953839895; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=1100000700000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=102; MVID_REGION_SHOP=S964; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; SMSError=; authError=; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_uid=1656341328425402922; _ym_d=1656341328; tmr_lvidTS=1656341327834; tmr_lvid=c8039c6d453b074f907e2709a13504e0; flocktory-uuid=e6665b06-a6f8-4c9f-895d-7a6270c00a69-7; BIGipServeratg-ps-prod_tcp80=2466569226.20480.0000; bIPs=-314595793; afUserId=271eb940-f151-451a-b5a8-7f61ae61942f-p; uxs_uid=4203e900-f628-11ec-8763-6d3b2d8e9f7d; __ttl__widget__ui=1656341468657-55f252b0d511; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2466569226.20480.0000; MVID_GTM_BROWSER_THEME=1; __lhash_=d2a3cf994160eb5d3e6ad12c682f2c1e; JSESSIONID=fXPYvSpMpp2BL0c2GypqpJvY7VJ9HLpXvfkTJ1JHLtTJLJT1YwLn!1659720574; MVID_CART_AVAILABILITY=1; MVID_CREDIT_AVAILABILITY=true; MVID_GTM_DELAY=true; MVID_MCLICK=true; MVID_MOBILE_FILTERS=true; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=false; _gid=GA1.2.448330780.1657982342; _ym_isad=2; advcake_track_id=80596a6f-9225-8c5d-e49a-7e8ffd401a32; advcake_session_id=090e9c6b-ca44-23a1-f2c1-9deb87ce2415; AF_SYNC=1657982345659; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfYw1GLWohPAsdTxNBGUR5CmwXSEt1C2p0IUNEfTknbydVfnlnej8xLUMXPWshL1xmEBE5GjxrImhOWx9IXFFqJh8WfnQrWAwMYURIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDBEbR9iTlwjSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=Ev8syw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfYw1GLWohPAsdTxNBGUR5CmwXSEt1C2p0IUNEfTknbydVfnlnej8xLUMXPWshL1xmEBE5GjxrImhOWx9IXFFqJh8WfnQrWAwMYURIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDBEbR9iTlwjSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=Ev8syw==; cfidsgib-w-mvideo=lZdSj6EHQn8jokpCLeuW0stGp9XceOEOE84196gHnYAz68EEnqhWQcZN6O/zY6OHSS78mZFEooySTiW/ggGjQaWixiob0iSl4N4uzeyI7cI1+xBaAINyfvZjyxS6aSTYWrZluS0GO9tEXzI7ABHTTm2ZHInKOYfjdsfP; cfidsgib-w-mvideo=lZdSj6EHQn8jokpCLeuW0stGp9XceOEOE84196gHnYAz68EEnqhWQcZN6O/zY6OHSS78mZFEooySTiW/ggGjQaWixiob0iSl4N4uzeyI7cI1+xBaAINyfvZjyxS6aSTYWrZluS0GO9tEXzI7ABHTTm2ZHInKOYfjdsfP; gsscgib-w-mvideo=azUxCJd2k/bOJuJW37PL+/QEPrzRtxiKTS9aHnLRfS2G5dtCwTjyTIXPD77MphDHneihPFL4tUdiwFuSNIPYq0M7vXHq9NCv7wTVXOKY0oQsZ4NjM2XuZMY/x1jUcznulLH6h9foj6275frrLkArGoa5E1NcVOa2NXsWCoyMsIKMGqTkXd2yXaIixLLoRQyzJwHBiw/4eQddgclKDY9yi5dg80nuCX/ODHJ9VyqDwKqr6erCd7TBZ2ooiXtTrA==; gsscgib-w-mvideo=azUxCJd2k/bOJuJW37PL+/QEPrzRtxiKTS9aHnLRfS2G5dtCwTjyTIXPD77MphDHneihPFL4tUdiwFuSNIPYq0M7vXHq9NCv7wTVXOKY0oQsZ4NjM2XuZMY/x1jUcznulLH6h9foj6275frrLkArGoa5E1NcVOa2NXsWCoyMsIKMGqTkXd2yXaIixLLoRQyzJwHBiw/4eQddgclKDY9yi5dg80nuCX/ODHJ9VyqDwKqr6erCd7TBZ2ooiXtTrA==; fgsscgib-w-mvideo=KQu2a52f4fc395e25487cad9a9badfa53718a699; fgsscgib-w-mvideo=KQu2a52f4fc395e25487cad9a9badfa53718a699; cfidsgib-w-mvideo=lDpxZgsC1VDUPMYtWqFthESnFXrngPMdPzgtbn7enrmuVe3bHpt8IpoHzP4Cd6JCsPVIQvQiMwjDxH7VAIvj6RhuKVB0WGXUp/57yhiNS48GY5VCil/XDax9YNUJRMEN8gcg5hXcM70pBqViYfbEe+SgHBvJ65icMnvX; CACHE_INDICATOR=false; mindboxDeviceUUID=5683bc04-1432-440b-92ff-49fa22ce6917; directCrm-session=%7B%22deviceGuid%22%3A%225683bc04-1432-440b-92ff-49fa22ce6917%22%7D; _ga=GA1.2.194096916.1656341327; tmr_detect=1%7C1657982389229; MVID_ENVCLOUD=prod2; tmr_reqNum=110; _ga_CFMZTSS5FM=GS1.1.1657982341.2.1.1657982621.0; _ga_BNX5WPP3YK=GS1.1.1657982341.2.1.1657982621.60',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': 'f80f0f0c-ba4a-480d-a0b9-7f001a5ea22c',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()


    products_ids = response.get('body').get('products')
    with open('1_product_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    #print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    #print(len(response.get('body').get('products')))


    products_ids_str = ','.join(products_ids)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_price = response.get('body').get('materialPrices')
    for item in material_price:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id]={
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')
    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()
