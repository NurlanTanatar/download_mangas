from selenium import webdriver

def get_links_from_website(website):
    file_name = "output"
    browser = webdriver.Firefox()
    browser.get(website)
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
