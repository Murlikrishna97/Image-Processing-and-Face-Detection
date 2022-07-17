from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import threading
import os
import shutil


def search_google(search_term, root_dir):

    # Chrome
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # service = Service("D:\CDAC\Lecture Notes\Linux & Cloud Computing\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(service=service,options=options)
    # driver.get(url)

    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(2)
    try:
        cookie_consent = driver.find_element(by=By.ID, value='L2AGLb')
        cookie_consent.click()
    except: 
        pass
    time.sleep(1)
    search_box = driver.find_element(by=By.NAME, value='q')
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    i = 0
    for i in range(10):
        time.sleep(5)
        driver.execute_script(f"window.scrollTo({200000 * i}, {200000 * (i+1)});")

    time.sleep(5)
    driver.execute_script(f"window.scrollTo({200000 * (i + 1)}, 0);")


    image_search_block = driver.find_element(by=By.CLASS_NAME, value='islrc')
    images = image_search_block.find_elements(by=By.CLASS_NAME, value='rg_i')
    i = 0
    dirpath = root_dir + '/' + '_'.join(search_term.split())
    os.mkdir(dirpath)
    for image in images:
        if i == 150:
            break
        image.click()
        time.sleep(10)
        original_urls = driver.find_elements(by=By.CLASS_NAME, value='n3VNCb')
        for urls in original_urls:
            original_url = urls.get_attribute('src')
            if 'http' in original_url and 'gstatic' not in original_url:
                try:
                    data = requests.get(original_url)
                    file = open(dirpath + '/' + '_'.join(search_term.split(' ')) + '_' + str(i) + '.jpg', 'wb')
                    file.write(data.content)
                    file.close()
                    print()
                    print(f"Saved : {i} : {dirpath + '/' + '_'.join(search_term.split(' ')) + '_' + str(i) + '.jpg'}")
                    print(f"Link : {original_url}")
                    i += 1
                    break
                except:
                    pass
    driver.close()


if __name__ == '__main__':
    root_dir = 'Images_HD_150'
    if os.path.isdir(root_dir):
        shutil.rmtree(root_dir)
    os.mkdir(root_dir)
    url = "https://www.google.com/imghp"
    search_terms = ['Sanna Marin', 'Narendra Modi', 'Vladimir Putin', 'Tsai Ing-wen', 'Iván Duque Márquez', 'Alberto Fernández', 'Joe Bidden', 'Felix Tshisekedi', 'Jacinda Ardern', 'Carlos Alvarado Quesada']
        #              [Finland         India             Russia              Taiwan          Columbia              Argentina           USA             DRC                 NZ              Cost rica

    threads = []
    for search_term in search_terms:
        # search_google(search_term, root_dir)
        # threading.Thread(target=search_google, args=(search_term, root_dir)).start()
        threads.append(threading.Thread(target=search_google, args=(search_term, root_dir)))

    for idx, thread in enumerate(threads):
        thread.start()

        if (idx + 1) % 5 == 0:
            thread.join()

