from urlparse import urlparse


def url_scheme_checker(url, header=None):
    par = urlparse(url)
    new_url = url
    if not par.scheme:
        if not header:
            url_replaced = par._replace(scheme='http')
        else:
            url_replaced = par._replace(scheme=header)
        new_url = url_replaced.geturl()
        if '///' in new_url:
            new_url = new_url.replace('///', '//')
    return new_url


if __name__ == '__main__':
    url = '//img.alicdn.com/imgextra/i1/203036173/TB2uR6qfAyWBuNjy0FpXXassXXa_!!203036173.jpg'
    new_url = url_scheme_checker(url)
    print(new_url)
