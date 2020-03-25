import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)


browser.get("http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S04/480P/")
time.sleep(5)
episodeList = browser.find_elements_by_tag_name("a")
flag = False
idx = 0
for episode in episodeList:
    if flag:
        print(str(idx) + ". " + episode.text)
    flag = True
    idx = idx + 1
episodeNumber = int(input("Enter Episode Number: "))
time.sleep(5)
url = "http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S04/480P/" + str(episodeList[episodeNumber - 1].text)
download_url(url,"")


