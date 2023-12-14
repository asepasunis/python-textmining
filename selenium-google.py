import sys
import time
import selenium
import argparse
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', help='Masukan kriteria pencarian')
    parser.add_argument('-p', '--pages', default=1, help='1 page = 100 hasil')
    return parser.parse_args()


def start_browser():
    br = webdriver.Firefox()
    br.implicitly_wait(10)
    return br


def scrape_results(br):
    links = br.find_elements(By.XPATH, "/h3[@class='r']/a[@href]")
    print(links)
    results = []
    for link in links:
        title = link.text
        results.append(title)
    return results


def go_to_page(br, page_num, search_term):
    page_num = page_num - 1
    start_results = page_num * 100
    start_results = str(start_results)
    url = 'https://google.com/webhp?#num=100&start=' + start_results + '&q=' + search_term
    br.get(url)
    time.sleep(2)


def main():
    args = parse_args()
    br = start_browser()
    if not args.search:
        sys.exit('exit')
    search_term = args.search
    pages = args.pages
    all_result = []
    for page_num in range(int(pages)):
        page_num = page_num + 1  # start 0
        go_to_page(br, page_num, search_term)
        title_urls = scrape_results(br)
        for title in title_urls:
            all_result.append(title)

    for result in all_result:
        title = result[0]
        print('[+]', title, '---')


main()
