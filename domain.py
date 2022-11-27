from urllib.parse import urlparse

# domaini tespit edelim (sivas.edu.tr)
def get_domain(url):
    try:
        result = get_sub_domain(url).split('.')
        return result[-3] + '.' + result[-2] + '.' + result[-1]   # ŞOKOMELLİ
    except:
        return ''


# Sub_domaini tespit edelim (muhendislik.sivas.edu.tr) (asdads.sivas.com)
def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

# print(get_domain("https://muhendislik.sivas.edu.tr/elektrik---elektronik-muhendisligi-bolumu"))