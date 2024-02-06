import asyncio
from pyppeteer import launch
import time


width, height = 1366, 768

 
async def main():
    browser = await launch(
        headless=False,
        userDataDir='./userdata',
        executablePath="/home/lc/code/data_auto_download/chrome-linux64/chrome",
        args=[f'--window-size={width},{height}','--proxy-server=http://192.168.31.101:10792','--download-path=./'])
    page = await browser.newPage()
    # await page.goto('https://www.taobao.com')
    await page.setViewport({'width': width, 'height': height})
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    # 访问网页
    # await page.goto('https://www.baidu.com')
    print("loading ...")
    await page.goto('https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2Fdatasets%2FCornell-University%2Farxiv%2Fversions%2F165%3Fresource%3Ddownload')
    await asyncio.sleep(6)
    print("load done")

    # 提交用户名，登录
    print("inputing...")
    name_str = 'input[name="email"]'
    pswd_str = 'input[name="password"]'
    try:
        await page.type(name_str, "46406@qq.com")
        await page.type(pswd_str, "you passwd")
        await page.click('button[type="submit"]')
        await asyncio.sleep(10)
        print("click done")
    except:
        print("dont need login")

    await asyncio.sleep(4)
    
    # 下载
    print("try to download")
    # 验证版本
    element_attribute = await page.evaluate('''() => {
        const xpath = '//*[@id="site-content"]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a'; // 修改为你的 XPath 表达式
        const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        
        // 获取元素的属性
        const attribute = element ? element.getAttribute('href') : null;
        
        return attribute;
    }''')

    # print('元素属性值:', element_attribute)
    version = element_attribute[-3:]
    print("version: ", version)
    if version == "165":
        print("download click ...")
        down_btn_xpth = "/html/body/main/div[1]/div/div[5]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a/button"
        down_btn = await page.xpath(down_btn_xpth)
        print("downloading...")
        await down_btn[0].click()
        print("download done")
        
    await asyncio.sleep(10)
    # time.sleep(100)
 
# time.sleep(1000)
# asyncio.sleep(1000)
# await asyncio.sleep(10)
asyncio.get_event_loop().run_until_complete(asyncio.wait_for(main(), timeout=100000))