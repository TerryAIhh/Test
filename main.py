from time import sleep

from PIL import Image
from selenium import webdriver
import random
import pytesseract


def login():
    account = '皇族狼蛛7号'
    pwd = 'Qq13861808088'
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.get('https://mms.pinduoduo.com/login')
    driver.maximize_window()
    sleep(random.uniform(1, 3))
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/main/div/section[2]/div/div/div/div[1]/div/div[2]').click()
    # 输入账号
    sleep(random.uniform(0, 2))
    elemAccount = driver.find_element_by_xpath('//*[@id="usernameId"]')
    elemAccount.send_keys(account[:3])
    sleep(random.uniform(0, 2))
    elemAccount.send_keys(account[3:7])
    sleep(random.uniform(0, 2))
    elemAccount.send_keys(account[7:])
    # 输入密码
    sleep(random.uniform(1, 3))
    elemPwd = driver.find_element_by_xpath('//*[@id="passwordId"]')
    elemPwd.send_keys(pwd[:3])
    sleep(random.uniform(0, 2))
    elemPwd.send_keys(pwd[3:7])
    sleep(random.uniform(0, 2))
    elemPwd.send_keys(pwd[7:])
    # 点击登录
    sleep(random.uniform(1, 3))
    elemLogin = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/main/div/section[2]/div/div/div/div['
                                             '2]/section/div/div[2]/button')
    elemLogin.click()
    # # 点击事件
    # sleep(random.uniform(1, 3))
    # driver.find_element_by_xpath('//*[@id="block1190"]/div[2]/div/div[2]/div/div[1]/div[2]/a').click()
    # sleep(random.uniform(0, 2))
    # driver.find_element_by_xpath('//*[@id="tasktable"]/tbody/tr/td[4]/a').click()
    # sleep(random.uniform(1, 3))
    # tabs = driver.find_element_by_xpath('//*[@id="legendBasic"]/table/tbody/tr[4]/td')
    # tabs.screenshot('tabs.png')
    # text = pytesseract.image_to_string(Image.open('tabs.png'))
    # print(text)

    # # 切入网页框架
    # sleep(random.unifrom(1, 3))
    # driver.switch_to.frame(driver.find_element_by_xpath(r'//*[@id="J_login_container"]/div/iframe'))
    # # 切入 # 点击账号登录
    # driver.find_element_by_xpath(r"/html/body/div/div[2]/div[5]/span").click()
    # # print(driver.page_source)
    # #  输入验证码
    # sleep(random.uniform(1, 3))
    # driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[:3])
    # sleep(random.uniform(0, 2))
    # driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[3:7])
    # sleep(random.uniform(0, 2))
    # driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[7:])
    # # 点击获取验证码,等待输入
    # sleep(random.uniform(1, 3))
    # driver.find_element_by_xpath(r'//*[@id="send-number-button"]').click()
    # key = input('请输入验证码:')
    # driver.find_element_by_xpath(r'//*[@id="number-textbox"]').send_keys(key)
    # # 点击登陆
    # sleep(random.uniform(0, 1))
    # driver.find_element_by_xpath(r'//*[@id="login-button-mobile"]').click()
    # driver.switch_to.default_content()
    # # 切出框架
    # sleep(random.uniform(1, 5))
    # # 处理cookie
    # print(request)
    # cookie = driver.get_cookies()
    # print(cookie)
    # result = {}
    # for each in cookie:
    #     result[each['name']] = each['value']
    #     return result


if __name__ == '__main__':
    login()
