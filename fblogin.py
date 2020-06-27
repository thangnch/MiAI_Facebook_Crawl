from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai bao bien browser
browser  = webdriver.Chrome(executable_path="./chromedriver")

# 2. Mở thử một trang web
browser.get("http://facebook.com")

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("thangnch") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("passwordfake")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(5)

# 4. Đóng trình duyệt
browser.close()