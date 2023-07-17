from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta
import pandas as pd

# Set up ChromeDriver service
# s = Service("./chromedriver.exe")
# browser = webdriver.Chrome(service=s)
# browser = webdriver.Chrome(executable_path="./chromedriver.exe")

service = Service("./chromedriver.exe")
browser = webdriver.Chrome(service=service)

# Set initial date and data list
current_date = datetime(2023,7,13)
data = []

# Read URL
idx = 0
while True:
    # print("Process 300 days from {}-{}-{}".format(current_date.day, current_date.month, current_date.year))
    print("Process 300 days from {}-{}-{}".format(current_date.day, current_date.month, current_date.year))

    url = 'https://www.thantai1.net/so-ket-qua'
    browser.get(url)

    # Set date
    end = browser.find_element(By.ID, "end")
    end.clear()
    # end.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year))
    end.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year))

    btn = browser.find_element(By.XPATH, "/html/body/div[3]/main/div/form/div[2]/div/button[9]")
    btn.click()
# div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0, div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0.border-left, div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0.border-left
    # result = browser.find_elements(By.CSS_SELECTOR, ".font-weight-bold.col-12.d-block.p-1.m-0, .font-weight-bold.col-6.d-block.p-1.m-0, .font-weight-bold.col-6.d-block.p-1.m-0.border-left")
    # result = browser.find_elements(By.CSS_SELECTOR, 'div[l="4"].font-weight-bold.col-3.d-block.p-1.m-0, div[l="4"].font-weight-bold.col-3.d-block.p-1.m-0.border-left, div[l="4"].font-weight-bold.col-3.d-block.p-1.m-0.border-left, div[l="4"].font-weight-bold.col-3.d-block.p-1.m-0.border-left, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0.border-bottom, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0.border-left.border-bottom, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0.border-left.border-bottom, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0.border-left, div[l="4"].font-weight-bold.col-4.d-block.p-1.m-0.border-left')
    result = browser.find_elements(By.CSS_SELECTOR, 'div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0, div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0.border-left, div[l="2"].font-weight-bold.col-3.d-block.p-1.m-0.border-left')

    # result = browser.find_elements(By.CSS_SELECTOR, 'div[l="3"].font-weight-bold.col-4.d-block.p-1.m-0, div[l="3"].font-weight-bold.col-4.d-block.p-1.m-0.border-left, div[l="3"].font-weight-bold.col-4.d-block.p-1.m-0.border-left')
    for row in result:
        idx += 1
        data.append(row.text)

    current_date -= timedelta(days=300)
    if idx > 75 * 365: # số năm là 17 năm 
        break

# Save data to CSV file
df = pd.DataFrame(data)
df.to_csv("Giai_7.csv", index=False)

# Close the browser
browser.close()
#  hoàn thành xong giải 7