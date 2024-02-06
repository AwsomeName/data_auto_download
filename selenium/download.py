from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time


if __name__ == '__main__':
    
    # 加载谷歌浏览器驱动
    chrome_options = Options()
    
    # linux下运行记得加上这些参数 ----------------------------
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--enable_downloads=True')

    chrome_options.add_argument('--proxy-server=http://192.168.31.101:10792')
    chrome_options.add_argument('--download.default_directory=./')
    chrome_options.add_argument('--download.downloadPath=./')
    # chrome_options.add_argument('--downloadPath=./')
    
    chrome_options.add_argument('--download.prompt_for_download=False')
    # chrome_options.add_argument('--download.directory_upgrade=False')
    chrome_options.add_argument('--safebrowsing.enabled=False')

    
	# 加载chromedriver -------------------------------------------------
	# windows 下的 chromedriver 默认加载路径是当前路径下的 chromedriver.exe
	# linux 下的 chromedriver 默认加载路径是 /usr/bin/chromedriver
	# 当然也可以通过 executable_path 自定义
    driver = webdriver.Chrome(options=chrome_options)
    # -----------------------------------------------------------------
    
    # 打开页
    # url = "https://www.kaggle.com/datasets/Cornell-University/arxiv?resource=download"
    # url = "https://www.kaggle.com/datasets/Cornell-University/arxiv/download?datasetVersionNumber=165"
    url = "https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2Fdatasets%2FCornell-University%2Farxiv%2Fversions%2F165%3Fresource%3Ddownload"
    driver.get(url)
    driver.implicitly_wait(6)
    # driver.switch_to.frame(0)
    driver.find_element(By.NAME, "email").send_keys("46406@qq.com")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "password").send_keys("your word")
    buttons = driver.find_elements(By.TAG_NAME, "button");
    print("wb: ", buttons)
    for bt in buttons:
        if bt.get_attribute("type") == "submit":
            bt.click()

    print("sign in click!")
    # down_url = "https://www.kaggle.com/datasets/Cornell-University/arxiv/download?datasetVersionNumber=165"
    driver.implicitly_wait(16)

    button = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a/button")
    print(button.get_attribute("class"))
    # button.click()
    durl = driver.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a')
    print("durl:, ", durl.get_attribute("href"))

    down_url = durl.get_attribute("href")
    version = down_url[-3:]
    print("version: ", version)
    if version == "165":
        print("download click....")
        button.click()
        # pass
    
    # driver.implicitly_wait(16)
    time.sleep(6000)
    # driver.close()
    

    
    
