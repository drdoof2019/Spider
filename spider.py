from general import *
from urllib.request import urlopen
from link_finder import LinkFinder

class Spider:
    # Class objesi tanımalama ( tüm örümcekler arasında paylaşılan ortak bilgi )
    proje_adi = ''
    base_url = ''  # ana_url
    domain_name = ''
    kuyruk_dosyasi = ''
    tamamlanan_dosyasi = ''
    kuyruk = set()
    tamamlanan = set()

    def __init__(self, proje_adi, base_url, domain_name):
        Spider.proje_adi = proje_adi
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.kuyruk_dosyasi = Spider.proje_adi + "/kuyruk.txt"
        Spider.tamamlanan_dosyasi = Spider.proje_adi + "/tamamlanan.txt"
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)


    @staticmethod
    def boot():
        dosya_dizini_olustur(Spider.proje_adi)
        veri_dosyaları_olustur(Spider.proje_adi, Spider.base_url)
        Spider.kuyruk = dosyadan_kumeye(Spider.kuyruk_dosyasi)
        Spider.tamamlanan = dosyadan_kumeye(Spider.tamamlanan_dosyasi)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.tamamlanan:
            print(thread_name + " now crawling " + page_url)
            print('Kuyrukta ', str(len(Spider.kuyruk)) + ' | Crawled ', str(len(Spider.tamamlanan)))
            try:
                Spider.add_links_to_kuyruk(Spider.gather_links(page_url))
                Spider.kuyruk.remove(page_url)
            except:
                Spider.kuyruk.remove(page_url)

            Spider.tamamlanan.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            # The condition in its IF-statement never returned TRUE because response.getheader("Content-Type") returns text/html; charset=utf-8.
            if 'text/html' in response.getheader('Content-Type'):  # if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            # print('Error: sayfayı crawl edemiyorum')
            # print("response.headers['Content-Type']: ", response.headers['Content-Type'])
            print(str(e))
            return set()
        return finder.page_link()

    @staticmethod
    def add_links_to_kuyruk(links):
        for link in links:
            if link in Spider.kuyruk:
                continue
            if link in Spider.tamamlanan:
                continue
            if Spider.domain_name not in link:
                continue

            Spider.kuyruk.add(link)

    @staticmethod
    def update_files():
        kumeden_dosyaya(Spider.kuyruk, Spider.kuyruk_dosyasi)
        kumeden_dosyaya(Spider.tamamlanan, Spider.tamamlanan_dosyasi)





















