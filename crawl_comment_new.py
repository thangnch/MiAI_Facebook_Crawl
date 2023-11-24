from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 1. Khai báo browser
browser = webdriver.Chrome()

# 2. Mở URL của post
browser.get("file:///Users/thangnch/Desktop/index.html")

# sleep(5)

ul = browser.find_element(by=By.TAG_NAME, value="ul")
print(ul)

li  = ul.find_elements(by=By.TAG_NAME, value="li")
filecontent = ""
for lii in li:
    if lii.text[0]  not in "0123456789":
        ot = lii.text.replace("\n","")
        ot = ot.replace("\n","")
        print(ot)
        filecontent += ot + "\n"
    # name = lii.find_element(by=By.CLASS_NAME, value="x1y1aw1k.xn6708d.xwib8y2.x1ye3gou")
    # print(name.text)

f = open("demofile2.txt", "a")
f.write(filecontent)
f.close()
#
# # 3. Lấy link hiện comment
# showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
# showcomment_link.click()
# sleep(5)
#
# # 4. Lấy comment
# showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")
# showmore_link.click()
# sleep(random.randint(5,10))
#
# showmore_link.click()
# sleep(5)
#
# # 5. Tìm tất cả các comment và ghi ra màn hình (hoặc file)
# # -> lấy all thẻ div có thuộc tính aria-label='Bình luận'
#
# comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
#
# # Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
# for comment in comment_list:
#     # hiển thị tên người và nội dung, cách nhau bởi dấu :
#     poster = comment.find_element_by_class_name("_6qw4")
#     content = comment.find_element_by_class_name("_3l3x")
#     print("*", poster.text,":", content.text)
#
#
# sleep(5)
#
# # 6. Đóng browser
# browser.close()