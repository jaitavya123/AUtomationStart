from selenium import webdriver

print(" automation start PYTHON + GIT + JENKINS")

holdChrome = webdriver.ChromeOptions()
holdChrome.add_experimental_option("detach", True)   #Restrict auto close of chrome
e = webdriver.Chrome(holdChrome)
e.get("https://keepr.inoidsolutions.in/")