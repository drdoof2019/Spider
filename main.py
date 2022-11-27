import threading
from queue import Queue
from spider import Spider
from domain import get_domain
from general import *


PROJE_ADI = 'sivasgovtr'
ANASAYFA = 'https://www.sivas.edu.tr/'
DOMAIN_ADI = get_domain(ANASAYFA)
KUYRUK_DOSYASI = PROJE_ADI + '/kuyruk.txt'
TAMAMLANAN_DOSYASI = PROJE_ADI + '/tamamlanan.txt'
NUMBER_OF_THREADS = 20
queue = Queue()
Spider(PROJE_ADI, ANASAYFA, DOMAIN_ADI)


# Örümcek oluşturma f'n
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Örümceklerimiz için iş oluşturalım
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# her item için yeni bir iş oluşturucaz
def create_jobs():
    for link in dosyadan_kumeye(KUYRUK_DOSYASI):
        queue.put(link)
    queue.join()
    crawl()


# kuyrukta item var mı kontrol ettiğimiz f'n
def crawl():
    kuyruktaki_linkler = dosyadan_kumeye(KUYRUK_DOSYASI)
    if len(kuyruktaki_linkler) > 0:
        print(str(len(kuyruktaki_linkler)) + ' kuyruktaki link sayısı')
        create_jobs()

create_spiders()
crawl()