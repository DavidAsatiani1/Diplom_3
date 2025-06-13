import pytest
from selenium import webdriver

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        driver = webdriver.Chrome()
    elif 'firefox' in request.param:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def user():
    created_user = create_user()
    yield created_user
    delete_user(created_user)

@pytest.fixture(scope='function')
def order(user):
    created_order = create_order(user)
    yield created_order
    delete_order(created_order)