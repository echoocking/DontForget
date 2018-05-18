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
    url = 'https://fun.fanli.com/goshop/go?go=http%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D564357535644&id=712&lc=taohuasuan_9kuai9&pid=564357535644&sign=e4e75898'
    new_url = url_unquote(url)
    print(new_url)
