import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
I_USER = os.getenv("INS_USER")
I_PASS = os.getenv("INS_PASS")
SIMILAR_ACCOUNT = "fluttertoplulugu"


class InstaFollower():
    def __init__(self):
        self.s = Service(executable_path=CHROME_DRIVER_PATH)
        self.browser = webdriver.Chrome(service=self.s)
        self.wait = WebDriverWait(self.browser, 30, 0.5, ElementClickInterceptedException)

    def login(self):
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div input")))
        user.send_keys(I_USER)
        passw = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
        passw.send_keys(I_PASS)
        loggin_but = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        loggin_but.click()
        time.sleep(5)
        notnow = self.browser.find_element(By.CSS_SELECTOR, '.HoLwm')
        notnow.click()
        time.sleep(2)

    def find_followers(self):
        search = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')))
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        s_account = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.yPP5B a')))
        s_account.click()
        time.sleep(2)
        followers_click = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.Y8-fY a')))
        followers_click.click()
        time.sleep(2)
        self.followers = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.PZuss li')))

    def follow(self):
        iterate = 0
        if iterate == len(self.followers):
            iterate = 0
            self.followers.send_keys(Keys.PAGE_DOWN)
            self.followers = self.wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.PZuss li')))
        for follower in self.followers:
            try:
                follow = follower.find_element(By.CSS_SELECTOR, '.sqdOP.L3NKy.y3zKF')
            except NoSuchElementException:
                pass
            else:
                time.sleep(3)
                follow.click()
            iterate += 1

    def quit_browser(self):
        self.browser.quit()