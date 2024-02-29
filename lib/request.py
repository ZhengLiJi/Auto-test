from selenium import webdriver
from PIL import Image
import pytesseract
import time
# 这一段就不需要了 直接接口拿 转jpeg 放到ocr中识别
def fetch_captcha_image(url):
    # 启动浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    # 等待页面加载完成
    time.sleep(5)

    # 设置验证码图片的位置和大小（假设已知）
    location = {'x': 1980, 'y': 805}  # 左上角坐标
    size = {'width': 175, 'height':80 }  # 宽度和高度

    # 截取验证码图片
    try:
        driver.save_screenshot('screenshot.png')
        captcha_image = Image.open('screenshot.png')
        captcha_image = captcha_image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))

        captcha_image.save('captcha_image.png')
        Image.open('captcha_image.png')
    except Exception as e:
        print('截取验证码图片失败:', e)
        driver.quit()
        return

    # 关闭浏览器

def recognize_captcha(image_path):
    # 使用Tesseract识别图片中的文字
    captcha_text = pytesseract.image_to_string(Image.open(image_path))
    return captcha_text.strip()

# 使用示例
if __name__ == "__main__":
    url = 'https://dashboardtest.tikipay.co/user/login'
    fetch_captcha_image(url)
    captcha_text = recognize_captcha('captcha_image.png')
    print('识别到的验证码：', captcha_text)
