import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def main(mail, number):
    s = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    email = mail[number]
    driver.maximize_window()
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdhcaTv_p0LjqRJxrCorKiyUG_H_pe6J9JWfjpZXFyv5UC8fA/viewform')
    time.sleep(3)
    email_input = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    email_input.clear()
    email_input.send_keys(f"{email}")
    captcha_input = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    captcha_input.clear()
    captcha_input.send_keys('19')
    submit_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    number += 1
    time.sleep(3)
    driver.close()
    with open('result.txt', 'a') as f:
        f.write(f"{email}\n")
    main(mail, number)


def get_data_mail():
    f = open('mails.txt', 'r')
    i = 0
    for line in f:
        i
        i += 1
    with open("mails.txt", "r") as f:
        mail = f.read().split('\n')
        number = 0
        main(mail, number)


if __name__ == '__main__':
    get_data_mail()