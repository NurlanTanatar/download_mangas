from selenium import webdriver
from get_files import download_files_from_report
from check_missing import check_for_missing_files
file_name = "output"
browser = webdriver.Firefox()
browser.get("https://manga-online.biz/reawaken_man_12.html")
more = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/button')
more.click()
links = browser.find_elements_by_css_selector('div.options.content > a')
arr = []
for i in links:
    arr.append(i.get_attribute('href'))
arr = arr[::-1]
arr = arr[0:5]
browser.quit()

#check for right amount of chapters
# with open("outputNum.txt", "w") as txt_file:
#     for line in range(len(arr)):
#         txt_file.write(f"{line} {arr[line]}\n")

with open(f"{file_name}.txt", "w") as txt_file:
    for line in range(len(arr)):
        txt_file.write(f"{arr[line]}\n")

print("downloading")
download_files_from_report(file_name)
print("checking")
check_for_missing_files(file_name)
