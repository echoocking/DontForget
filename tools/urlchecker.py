from urlparse import urlparse
from urllib import quote, unquote

def url_scheme_checker(url, header='http'):
    par = urlparse(url)
    new_url = url
    if not par.scheme:
       
        url_replaced = par._replace(scheme=header)
        new_url = url_replaced.geturl()
        if '///' in new_url:
            new_url = new_url.replace('///', '//')
    return new_url


def url_unquote(url):
    return unquote(url)


if __name__ == '__main__':
    url = 'https://fun.fanli.com/goshop/go?id=712&lc=taohuasuan_9kuai9&go=https://uland.taobao.com/coupon/edetail?e=M%2Fix9%2Fwfdz%2BbhUsf2ayXDCkum0Md9jW28qz22AlK%2FM%2FS00l8O80VB7cZelJt%2Bzjy9nNa8V2%2FfgCU8bIiPhUhftzNwQTGaE3k14t9QUPD0GaTz0aCh2qIRzxNuKO33NBYKWk794GLk9290%2BcSgujO2Yu6FJABcKj4gPRfTgnhrZM%3D&af=1&pid=mm_32293866_3446435_59504417&itemId=534255178000&sign=0685a179'
    new_url = url_unquote(url)
    print(new_url)
