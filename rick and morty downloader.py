from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    try:
        with DownloadProgressBar(unit='B', unit_scale=True,
                                 miniters=1, desc=url.split('/')[-1]) as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)
    except:
        print("Net too slow!")
        browser.close()
        quit()


def wait_till_page_loaded(xpath):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print("Loading took too much time!")
        browser.close()
        quit()


options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

season_number = input("Enter Season Number: ")
browser.get("http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S0"+season_number+"/480P/")
wait_till_page_loaded('/html/body/pre/a[2]')
episodeList = browser.find_elements_by_tag_name("a")
flag = False
idx = 0
for episode in episodeList:
    if flag:
        print(str(idx) + ". " + episode.text)
    flag = True
    idx = idx + 1
episodeNumber = int(input("Enter Episode Number: "))
url = "http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S0"+season_number+"/480P/" + str(episodeList[episodeNumber].text)
download_url(url, "")
browser.close()
