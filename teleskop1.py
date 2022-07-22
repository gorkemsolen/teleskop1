from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/admin/Downloads/chromedriver_win32/chromedriver.exe')

browser.get("https://www.nytimes.com/crosswords/game/mini")

path = browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/main/div/div/article/section[2]")

print(path.text)