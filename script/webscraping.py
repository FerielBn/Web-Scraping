from selenium import webdriver

url = 'https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ'
browser = webdriver.Chrome()
browser().get(url)

