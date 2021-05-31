from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


def screen_cut():
    driver = webdriver.Chrome()
    driver.get("https://mms.pinduoduo.com/orders/list")
    filename = "image.png"
    # 获取需要点击的元素
    element = driver.find_element(By.XPATH,
                                  '//*[@id="mf-mms-orders-container"]/div/div/div/div[5]/div[2]/div/div[1]/div['
                                  '2]/div[2]/div/a/span')
    element.click()
    # 截屏
    driver.save_screenshot(filename)
    # 获取元素上下左右的位置
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    # 打开刚才的截图
    im = Image.open(filename)
    # 截取对应位置
    im = im.crop((left, top, right, bottom))
    # 保存覆盖原有截图
    im.save(filename)

    driver.quit()


if __name__ == '__main__':
    screen_cut()
