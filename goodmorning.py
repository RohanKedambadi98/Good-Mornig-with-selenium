from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class morning():
    def test(self):

        #youtube
        YoutubeUrl = "https://www.youtube.com/watch?v=LbIkrZSIG9A#t=0m41s"
        driver = webdriver.Firefox()
        driver.get(YoutubeUrl)
        driver.implicitly_wait(3)

        time.sleep(3)
        # center play button
        driver.find_element(By.XPATH, "//button[@class='ytp-large-play-button ytp-button']").click()
        time.sleep(7)
        # skip ad
        driver.find_element(By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']").click()
        time.sleep(2)
        # no thanks
        driver.find_element_by_css_selector("paper-button.style-text").click()
        # full screen
        # driver.find_element(By.XPATH,"//button[@class='ytp-fullscreen-button ytp-button']").cli

        #set position and size
        driver.set_window_size(466,400)
        driver.set_window_position(450,10)

        #instagram
        InstaUrl = "https://www.instagram.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(InstaUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.NAME, "username").send_keys("username")
        driver.find_element(By.NAME, "password").send_keys("password")
        # driver.find_element(By.XPATH, "//button[text()='Show']").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Not Now']").click()

        time.sleep(3)
        driver.set_window_size(466,400)
        driver.set_window_position(3,10)




        #facebook
        FbUrl = "https://www.facebook.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(FbUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID,"email").send_keys("username")
        driver.find_element(By.ID,"pass").send_keys("password")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        if driver.current_url=="https://www.facebook.com/":
            pass
        else:
            driver.refresh()
            driver.find_element(By.XPATH, "//input[@id='email']").send_keys("username")
            driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("password")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()


        driver.set_window_size(466,400)
        driver.set_window_position(900,10)



        #what is today
        search_string = "what's today"

        # This is done to structure the string

        search_string = search_string.replace(' ', '+')


        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(0))

        driver.set_window_size(1000,320)
        driver.set_window_position(185,425)

        driver.execute_script("window.scrollBy(0,85);")









gg = morning()
gg.test()
