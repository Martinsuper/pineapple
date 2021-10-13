from selenium import webdriver


def get_calendar():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.set_window_size(1080, 1024)
    driver.get('http://www.baidu.com/s?ie=UTF-8&wd=日历')
    img = driver.find_element_by_xpath('//*[@id="1"]/div/div[1]')
    img.screenshot('../img/calender.png')
    driver.quit()


def get_weather():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.set_window_size(1080, 1024)
    driver.get('http://www.baidu.com/s?ie=UTF-8&wd=上海天气')
    img = driver.find_element_by_xpath('//*[@id="1"]/div[1]/div[2]/div[1]')
    img.screenshot('../img/weather.png')
    driver.quit()


if __name__ == '__main__':
    get_calendar()
    get_weather()
