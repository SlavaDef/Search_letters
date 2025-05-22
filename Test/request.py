import requests
import pprint


# створили кортедж
urls = ('http://www.baidu.com', 'http://www.sina.com.cn', 'https://www.radio-ua.com/')

# тут генератор списків
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content),'->',resp.status_code,'->',resp.url)

# а це вираз генератор
for resp in (requests.get(url) for url in urls):
    print(len(resp.content),'->',resp.status_code,'->',resp.url)

print('------')

def generator_request(some_url: tuple) -> tuple:
    for respon in (requests.get(url) for url in some_url):
        yield len(respon.content), respon.status_code, respon.url

for resp_len, status, url, in generator_request(urls):
 print(resp_len, '->', status, '->', url)

# make dictionary
url_res = {url: size for size, _, url in generator_request(urls)} # _ тут означає що цей параметер ігнориться
pprint.pprint(url_res)




#generator_request(urls)