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
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--proxy-server=http://192.168.31.101:10792')
    # chrome_options.add_argument('--proxy-server=http://192.168.31.101:10792')

    # -----------------------------------------------------
    
	# 加载chromedriver -------------------------------------------------
	# windows 下的 chromedriver 默认加载路径是当前路径下的 chromedriver.exe
	# linux 下的 chromedriver 默认加载路径是 /usr/bin/chromedriver
	# 当然也可以通过 executable_path 自定义
    driver = webdriver.Chrome(options=chrome_options)
    # -----------------------------------------------------------------
    
    # 打开百度首页
    url = "https://www.kaggle.com/datasets/Cornell-University/arxiv?resource=download"
    # driver.get('https://www.baidu.com/')
    driver.get(url)
    # print("init...")
    # button = driver.find_element(By.CLASS_NAME, "sc-iEYVpv dLIycx")
    # print("button:", button)
    # driver.find_element(By.Class, "sc-iEYVpv dLIycx").click()
    print("click!")
    
    # time.sleep(100)
    
    raw_cookies = driver.get_cookies()
    print("raw cookie:")
    print(raw_cookies)
    print("------------\n")
    
    # print("save now!")
    # jsoncookies = json.dumps(mycookies)
    # with open("mycookie.json",'w') as f:
    #     f.write(jsoncookies)
    # # time.sleep(100)
    # driver.close()
    # exit()
    
    cookie_file = "mycookie.json"
    with open(cookie_file, "r") as fp:
        cookies = json.load(fp)

    for rc in raw_cookies:
        raw_name = rc['name']
        for nc in cookies:
            if nc['name'] == raw_name:
                if nc != rc:
                    print("diff:")
                    print("raw:", rc)
                    print("cc:", nc)
                    print("\n")
                    # if nc['name'] in ["__Host-KAGGLEID", "XSRF-TOKEN"]:
                    # if nc['name'] in ["__Host-KAGGLEID", "CSRF-TOKEN"]:
                    if nc['name'] in ["__Host-KAGGLEID", "CLIENT-TOKEN"]:
                        rc['value'] = nc['value']

    print("------------==============\n\n")

    driver.delete_all_cookies()
    for cookie in raw_cookies:
        print("cookie:", cookie)
        # if cookie['name'] == "__Host-KAGGLEID":
        #     print("---pass")
        #     continue
        driver.add_cookie(cookie)
    # driver.add_cookie(cookies)

    time.sleep(2)
    print("update cookis done")
    # driver.get(url)
    driver.refresh()
    print("refreshing ! ...")
    time.sleep(60)
    
    # mycookies = driver.get_cookies()
    # jsoncookies = json.dumps(mycookies)
    # with open("mycookie.json",'w') as f:
    #     f.write(jsoncookies)
# driver.quit()
    
    # 获取百度导航栏中的文本
    # xp = '//*[@id="s-top-left"]/a'
    # nav_list = [elm.get_attribute('text') for elm in driver.find_elements(by=By.XPATH, value=xp)]
    # print(nav_list)
    # ['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘']
