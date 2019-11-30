from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
form selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

import re

'''
TODO:
Yamaha: xj/85, fzs/99/02, xj/94/03,
BMW: K/93/87,
Kawasaki: ER/97/06, GPZ/97, ZR/00, Zephyr/92
Honda: CB/98
1. Create class
'''

class Searcher():
# https://www.otomoto.pl/motocykle-i-quady/{mark}/{model}/od-{year1}/?search%5Bfilter_float_price%3Ato%5D={price}&search%5Bfilter_float_year%3Ato%5D={year2}&search%5Bfilter_float_engine_capacity%3Afrom%5D={engine}&search%5Border%5D=created_at%3Adesc&search%5Bcountry%5D=

	def __init__(self, mark, model, year1, year2, engine, price):
		self.mark = mark
		self.model = model
		self.year1 = year1
		self.year2 = year2
		self.price = price
		self.engine = engine

		url = f"https://www.otomoto.pl/motocykle-i-quady/{self.mark}/{self.model}/od-{self.year1}/?search%5Bfilter_float_price%3Ato%5D={self.price}&search%5Bfilter_float_year%3Ato%5D={self.year2}&search%5Bfilter_float_engine_capacity%3Afrom%5D={self.engine}&search%5Border%5D=created_at%3Adesc&search%5Bcountry%5D="

	def down(url):
		options = webdriver.Chrome.Options()
		options.add_argument('--headless')
		options.add_argument('disable-gpu')
		driver = webdriver.Chrome()
		driver.get(url)
		content = driver.find_element_by_xpath('//*[@id="body-container"]/div[2]/div[1]/div/div[1]/div[4]/article[1]')

		# xpath of element on page #1
		# //*[@id="body-container"]/div[2]/div[1]/div/div[1]/div[4]/article[1]
		# xpath of element on page #2
		# //*[@id="body-container"]/div[2]/div[1]/div/div[1]/div[4]/article[2]
		# same for every page


oto = Searcher('BMW', 'K', 1995, 2011, 250, 10000)
oto.down
