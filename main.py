import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
import os

username = input("Enter Login Credentials: \n    Phone number, username or email: ")
password = input("    Password: ")
insta_id = input("Enter Instagram Handle to be Scraped: ")
spt = input("Enter Scroll Pause Time (in secs): ") or 1
spt = int(spt)

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


# noinspection PyBroadException
def Login(user_id, user_password):
    URL = "https://www.instagram.com/"
    driver.get(URL)

    try:
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_element.clear()
        username_element.send_keys(user_id)

        password_element = driver.find_element_by_name("password")
        password_element.clear()
        password_element.send_keys(user_password)

        login = driver.find_elements_by_tag_name("button")[1]
        login.click()
        time.sleep(5)
    except:
        print("Oops! cannot Login...")


# noinspection PyBroadException
def scrape_data(target_id, user_id, user_password, spt):

    print("\nCreating Directory in C Drive....")
    destination_path = "D:/InstaScraper/" + target_id + " images"
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    print("\nLogging in...")
    Login(user_id, user_password)
    print("\nLogged in...")

    URL = "https://www.instagram.com/" + target_id
    driver.get(URL)

    SCROLL_PAUSE_TIME = spt

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    all_images = []
    i = 1

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        try:
            article = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "article"))
            )
            images = [image.get_attribute("src") for image in article.find_elements_by_tag_name("img") if image.get_attribute("src") not in all_images]
            for image in images:
                all_images.append(image)
                urllib.request.urlretrieve(image, destination_path + "/" + str(i) + ".png")
                i = i + 1

        except:
            print("\n\n :( Slow internet! some images missed, increase Scroll Time and try again if you want missing images...")

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("\nReached end of page!")
            break
        last_height = new_height

    print("\nImages Successfully saved in Instascraper Directory! \nOpening, wait a moment.....")
    driver.quit()
    path = os.path.realpath(destination_path)
    os.startfile(path)


scrape_data(insta_id, username, password, spt)
