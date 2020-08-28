import requests
from bs4 import BeautifulSoup
import sys


def show_progress_bar(current_size, total_size):
    percentage = (current_size / total_size) * 100
    progress_bar_length = 50
    current_progress = int((current_size / total_size) * 50)
    current_size = int(current_size / 1024)
    progress_bar = "[" + "#" * current_progress + " " * (progress_bar_length - current_progress) + "]" \
                   + " Current Downloaded(KB): " + str(current_size)

    sys.stdout.write("\r{}".format(progress_bar))
    sys.stdout.flush()


def download(download_url, fileName):
    r2 = requests.get(download_url, stream=True)
    total_size = int(r2.headers['content-length'])
    print("Total Size Of The File(in KB): "+str(total_size/1024))
    current_size = 0
    file = open(fileName, 'wb')
    try:
        for data in r2.iter_content(chunk_size=1024):
            current_size = current_size + 1024
            file.write(data)
            show_progress_bar(current_size, total_size)
    finally:
        file.close()


season_number = input("Enter Season Number: ")

try:
    r = requests.get("http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S0" + season_number + "/480P/")
except requests.exceptions.ConnectionError:
    print("Connection Error")
    quit()

soup = BeautifulSoup(r.content, "html.parser")
episodeList = soup.find_all('a')
for idx in range(1, len(episodeList)):
    print(str(idx) + ". " + episodeList[idx].text)

episodeNumber = int(input("Enter Episode Number: "))
url = "http://dl9.rmdlsv.com/tv-series/Rick-And-Morty/S0" + season_number + "/480P/" + episodeList[episodeNumber].text

file_name = episodeList[episodeNumber].text
download(url, file_name)
