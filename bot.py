from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

class Bot():
	def __init__(self):
		print("normal,advanced")
		global choose
		choose = input()
		if choose == "normal":
			driver.get("https://10fastfingers.com/typing-test/english")
		elif choose == "advanced":
			driver.get("https://10fastfingers.com/advanced-typing-test/english")
		self.i = 0
		print("How much wpm do you want")
		self.test = input()
		self.test = int(self.test)
		self.wpm = 60/self.test - 0.054
	def AcceptCookies(self):
		WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialog"]')))
		time.sleep(1)
		cookie_accept = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
	def TypeWords(self):
		keyboard = driver.find_element_by_xpath('//*[@id="inputfield"]')
		while self.i <= 400:
			time.sleep(self.wpm)
			self.i += 1
			self.x = driver.find_element_by_xpath(f'//*[@id="row1"]/span[{self.i}]')
			if random.randint(11,100) <= 10:
				keyboard.send_keys("d ")
				print("Typed special wrong " + self.x.text)
			else:
				keyboard.send_keys(self.x.text + " ")
				print("Typed " + self.x.text)
main = Bot()
if choose == "normal" or "advanced":
	main.AcceptCookies()
	main.TypeWords()

