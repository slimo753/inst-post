from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
import time
import pygame

# Приветстиве
print("######~##~~##~~####~~######~~####~~~~~~#####~~##~~##",
      "~~##~~~###~##~##~~~~~~~##~~~##~~##~~~~~##~~##~~####",
      "~~##~~~##~###~~####~~~~##~~~######~~~~~#####~~~~##",
      "~~##~~~##~~##~~~~~##~~~##~~~##~~##~~~~~##~~~~~~~##",
      "######~##~~##~~####~~~~##~~~##~~##~##~~##~~~~~~~##", sep="\n")

# Ввод
file_login = open("file_login.txt", "r")
login = file_login.read().split("\n")[0]
print("Login: ", str(login))
file_login = open("file_login.txt", "r")
password = file_login.read().split("\n")[1]
print("Password: ", str(password))

file_hashtag = open("file_hashtag.txt", "r")
hashtag = file_hashtag.read().split("\n")[0]
print("Hashtag: ", str(hashtag))

file_showing = open("file_showing.txt", "r")
showing = file_showing.read().split("\n")[0]
showing = int(showing)
print("Post view time: ", str(showing))

file_quantity_input = open("file_quantity_input.txt", "r")
quantity_input = file_quantity_input.read().split("\n")[0]
quantity_input = int(quantity_input)
print("Number of posts: ", str(quantity_input))

file_screen = open("file_screen.txt", "r")
quantity_screen = file_screen.read().split("\n")[0]
quantity_screen = int(quantity_screen)
print("Quantity of posts: ", str(quantity_screen))

def inst():

      chrome_options = webdriver.ChromeOptions()
      chrome_options.add_argument("--disable-background-networking")
      chrome_options.add_argument("start-maximized")
      chrome_options.add_argument("--disable-popup-blocking")
      chrome_options.add_argument("--disable-blink-features=AutomationControlled")
      chrome_options.add_argument("user-data-dir=C:/cookie/{}".format(login))
      driver = webdriver.Chrome(options=chrome_options)
      driver.get("https://www.instagram.com/?hl=en")

      time.sleep(2)
      driver.implicitly_wait(5)

      # Принятие Cookie
      try:
            print("Attempt to accept Cookie")
            driver.find_element_by_xpath("//*[@class='aOOlW  bIiDR  ']").click()

      except WDE:

            print("Cookie already accepted")

      # Авторизация
      try:
            print("Attempt to authorize")
            login_element = driver.find_element_by_xpath("//*[@name='username']")
            login_element.send_keys(login)
            password_element = driver.find_element_by_xpath("//*[@name='password']")
            password_element.send_keys(password)
            driver.find_element_by_xpath("//*[@class='sqdOP  L3NKy   y3zKF     ']").click()
            time.sleep(3)
            print("Authorization completed")

      except WDE:

            print("Authorization has already been completed")

      # Отказ от сохранения пароля
      try:
            driver.find_element_by_xpath("//*[@class='sqdOP yWX7d    y3zKF     ']").click()
            print("Refused to save password")

      except WDE:

            print("Refused to save password")

      # Отказ от уведомлений
      try:
            driver.find_element_by_xpath("//*[@class='aOOlW   HoLwm ']").click()
            print("Refused notifications")

      except WDE:

            print("Refused notifications")

      status = True

      while status:

          try:
                driver.implicitly_wait(10)
                driver.get("https://www.instagram.com/?hl=en")
                time.sleep(1)

                # Ввод в окно поиска
                window_search_element = driver.find_element_by_xpath("//*[@placeholder='Search']")
                window_search_element.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
                time.sleep(1)
                window_search_element.send_keys(hashtag)
                print("Introduce", str(hashtag), "to the search")
                time.sleep(1)

                # Клик в окне поиска
                result_search = driver.find_element_by_xpath("//*[@class='_7UhW9   xLCgt      MMzan   _0PwGv             fDxYl     '][1]")
                result_search.click()
                driver.refresh()

                # Количество постов
                quantity_post = 1

                column = 1

                line = 1

                screen_number = 1

                post = True

                while post:

                      if  quantity_post <= quantity_input:

                            if line < 4:

                                  # Кликаем на найденные элементы в поиске
                                  post_element = driver.find_element_by_xpath("//*[@class='KC1QD']/div[2]//*[@class='Nnq7C weEfm'][" + str(column) + "]//div[@class='v1Nh3 kIKUG  _bz0w'][" + str(line) + "]")
                                  post_element.click()
                                  print("-------------------------------------")
                                  print("Post display: ", str(showing), "seconds")
                                  time.sleep(showing)

                                  # Делаем скрин
                                  driver.save_screenshot("{}.png".format(screen_number))

                                  driver.find_element_by_xpath("//*[@aria-label='Close']").click()
                                  print("Shown ", str(quantity_post), "of ", str(quantity_input), "posts")
                                  quantity_post += 1
                                  line += 1

                                  screen_number += 1

                            else:

                                  line = 1
                                  column += 1

                      else:

                            post = False

                            shown_screen = 1

                            screens = 1

                            screen = True

                            while screen:

                                  if shown_screen <= quantity_screen:

                                        try:
                                              _PNG_IMAGE = '{}.png'.format(screens)

                                              pygame.display.init()
                                              img = pygame.image.load(_PNG_IMAGE)
                                              img = pygame.transform.scale(img, (1920, 1080))
                                              screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
                                              screen.blit(img, (0, 0))
                                              pygame.display.flip()
                                              time.sleep(showing)
                                              pygame.quit()

                                              screens += 1

                                              shown_screen += 1

                                        except FileNotFoundError:

                                              screens = 1

                                  else:

                                        screen = False

          except WDE:

              status = True
              print("Element search error")
              driver.get("https://www.instagram.com/?hl=en")

inst()
