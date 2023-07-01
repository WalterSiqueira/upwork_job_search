import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class u_scraper:
    def __init__(self):
        self.webdriver_path = '/path/to/chromedriver'  # Replace with the actual path
        self.service = Service(self.webdriver_path)
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
    
    def get_input(self):
        self.keyword = str(input("Enter the keyword you want to search: "))
        self.search()
    
    def search(self):
        self.target = f"https://www.upwork.com/nx/jobs/search/?from_recent_search=true&q={self.keyword}&sort=recency"
        self.driver.get(self.target)
        self.driver.implicitly_wait(10)
        self.parent_elements = self.driver.find_elements(By.CSS_SELECTOR, '.up-card')
        self.search_in_results()
    
    def search_in_results(self):
        self.texts = []
        self.links = []
        for parent_element in self.parent_elements:
            child_elements = parent_element.find_elements(By.CSS_SELECTOR, '.up-card-section')
            for child_element in child_elements:
                gran_elements = child_element.find_elements(By.XPATH, './/div/h3')
                gran_elements_links = child_element.find_elements(By.XPATH, './/div/h3/a')
                for gran_element in gran_elements:
                    text = gran_element.text
                    self.texts.append(text)
                for gran_link in gran_elements_links: 
                    href = gran_link.get_attribute('href')
                    self.links.append(href)
        self.show()
        self.close()
    def show(self):
        for i in range(len(self.texts)):
            print(self.texts[i])
            print(self.links[i])
    
    def close(self):
        self.driver.quit()

a = u_scraper()
a.get_input()

