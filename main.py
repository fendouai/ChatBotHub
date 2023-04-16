import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chat_content = "你好，开放猫"

# 设置Chrome浏览器启动参数，让多个窗口并排显示
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-position=0,0")
chrome_options.add_argument("--window-size=800,600")
chrome_options.add_argument("--disable-extensions")

# 创建Chrome浏览器实例
driver = webdriver.Chrome(chrome_options=chrome_options)

# 打开多个网页
driver.get("https://openmao.panchuang.net/#/chat/")
driver.execute_script("window.open('https://zlv7o.aichatos.com/#/chat/');")
driver.execute_script("window.open('https://free.anzz.top/#/chat/');")

wait = WebDriverWait(driver, 20)  # 显式等待10秒
# 切换到每个窗口，以便进行后续操作
windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    # 找到textarea元素并输入内容
    textarea = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    textarea.send_keys(chat_content)
    # 使用ActionChains库模拟鼠标操作，以便在多个窗口之间移动
    time.sleep(3)
    textarea.send_keys(Keys.RETURN)
    time.sleep(3)

# 如果需要长时间停留，可以增加数值。
time.sleep(30)
# 关闭浏览器 移出代码注释 可以自动关闭所有网页
#driver.quit()
