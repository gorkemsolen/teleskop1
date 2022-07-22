from selenium import webdriver
import json

#selenium ve chrome driver ile gereken bağlantıyı sağlayarak verilerin elementine erişim ve ekranda yazdırma

browser = webdriver.Chrome(executable_path='C:/Users/admin/Downloads/chromedriver_win32/chromedriver.exe')

browser.get("https://www.nytimes.com/crosswords/game/mini")

path = browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/main/div/div/article/section[2]")

print(path.text)

#json dosyasının temelini oluşturma

clues = {
    "clues":[{
    'group': ' ',
    'number': ' ',
    'string':' '
  }]}

#json dosyasını oluşturma

with open('crossword.json', 'w') as json_file:
  json.dump(clues, json_file)

#json'a yeni veriler ekleme mantığı

def write_json(new_data, filename='crossword.json'):
    with open(filename,'r+') as file:

        file_data = json.load(file)
        file_data["clues"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#gereken verilere erişim ve ekleme

for j in range(2):
  j+=1
  groupNo=str(j)
  for i in range(5):
    i+=1
    rowNo=str(i)
    newClue = {
    'group': browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/main/div/div/article/section[2]/div["+groupNo+"]/h3").text,
    'number': browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/main/div/div/article/section[2]/div["+groupNo+"]/ol/li["+rowNo+"]/span[1]").text,
    'string':browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/main/div/div/article/section[2]/div["+groupNo+"]/ol/li["+rowNo+"]/span[2]").text
    }
     
    write_json(newClue)

browser.quit()
