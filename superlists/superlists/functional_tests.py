'''
Created on Aug 29, 2014

@author: krobinson
'''
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title