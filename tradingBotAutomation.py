from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import undetected_chromedriver as uc
import random

def start_trading(username, password):

    driver = uc.Chrome()


    driver.get("https://qxbroker.com/en")


    login_button = driver.find_element(By.XPATH, "//*[@id='top']/div/div[1]/a[2]")
    login_button.click()
    sleep(3)


    username_input = driver.find_element(By.XPATH, "//*[@id='tab-1']/form/div[1]/input")
    password_input = driver.find_element(By.XPATH, "//*[@id='tab-1']/form/div[2]/input")

    username_input.send_keys(username)
    password_input.send_keys(password)
    sleep(3)

    submit_button = driver.find_element(By.XPATH, "//*[@id='tab-1']/form/button/div")
    submit_button.click()
    sleep(6)

    manu_btn = driver.find_element (By.XPATH, "//div[@class='usermenu__info-wrapper']")
    manu_btn.click()
    sleep (3)
    myID = "34146912"

    web_page_id_element = driver.find_element (By.XPATH, "//span[@class='usermenu__number']")
    web_page_id_text = web_page_id_element.text

    # Extract numeric part from the text
    web_page_id_str = web_page_id_text.split (":")[1].strip ()

    # Check if your ID is equal to the web page ID
    try:
        if myID == web_page_id_str:
            # Click the demoAccountBtn
            demo_account_btn = driver.find_element (By.XPATH,
                                                    "//*[@id='root']/div/div[1]/header/div[8]/div[2]/div[2]/ul[1]/li[3]/a")
            demo_account_btn.click ()
            print(f"Your ID is {myID} has match with Bot ID {web_page_id_text} ")

    except NoSuchElementException:
        print ("Invalid ID")

    sleep (5)

    user_amount = 5

    while user_amount <= 10000:

        amount_send = driver.find_element (By.XPATH, "//input[@type='text' and @class='input-control__input']")
        amount_send.clear ()  # Clear the input before sending keys
        sleep(1)
        amount_send.send_keys (user_amount)




        up_button = "/html/body/div[1]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[1]/button"
        down_button = "/html/body/div[1]/div/div[1]/main/div[2]/div[1]/div/div[6]/div[4]/button"



        up_button = WebDriverWait (driver, 10).until (
            EC.visibility_of_element_located ((By.XPATH, up_button))
        )

        down_button = WebDriverWait (driver, 10).until (
            EC.element_to_be_clickable ((By.XPATH, down_button))
        )

        # # Handling Element Location Errors
        try:
            clickBtn = random.choice([up_button, down_button])
            clickBtn.click()
        except TimeoutException:
            print ("Error: Unable to locate or click the button")


        current_time = datetime.datetime.now ().strftime ("%H:%M:%S")
        current_seconds = int (current_time.split (":")[2])

        if current_seconds == 0:
            if random.choice ([True, False]):
                up_button.click ()
            else:
                down_button.click ()

            break

        # Use WebDriverWait to wait for a specific condition (e.g seconds becoming 00)
        try:
            WebDriverWait (driver, 0.1).until (
                EC.text_to_be_present_in_element ((By.XPATH, "//div[@class='server-time online']"), "00"))


            if random.choice ([True]):
                up_button.click ()
            else:
                down_button.click ()
            break
        except TimeoutException:
            pass

        # Wait for the profit/loss message popup
        time.sleep (60)


        profit_loss_message = driver.find_element (By.XPATH,
                                                   '/html/body/div[1]/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[4]')

        message_text = profit_loss_message.text

        if '+' in message_text:

            print (f"You have profit {message_text}")


        else:
            user_amount *= 2

            sleep(1)
            print (f"You have Loss {message_text}")

        # Continue with the current amount on profit

    # Quit the WebDriver once the user_amount reaches 10000
    driver.quit ()


start_trading ('madihaatta59@gmail.com', 'madiha.atta@2005')



