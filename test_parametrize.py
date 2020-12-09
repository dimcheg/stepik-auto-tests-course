import pytest

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_stepik_parametrization(browser, link):
    browser.get(link)

    time.sleep(5)

    result = str(math.log(int(time.time())))

    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(result)

    button_submit = browser.find_element_by_class_name("submit-submission")
    button_submit.click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "pre.smart-hints__hint"), "Correct!"))