from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


def request_upass(driver):
    """
    Requests the U-Pass using the given Selenium driver.
    :param driver: the Selenium driver
    :return: None
    """
    url = "https://upassbc.translink.ca/"
    driver.get(url)

    process_school(driver)
    print("process_school(driver) returned.")

    process_login(driver)
    print("process_login(driver) returned.")

    process_request(driver)
    print("process_request(driver) returned.")


def process_school(driver):
    """
    Selects "University of British Columbia" as the school from the dropdown,
    and continues to the CWL login page.
    Precondition: driver is pointing to the U-Pass BC home page (with the
    "Select your school" dropdown.)
    Postcondition: driver is pointing to the CWL login page.
    :param driver: the Selenium driver
    :return: None
    """
    school_dropdown = driver.find_element_by_id("PsiId")
    select = Select(school_dropdown)

    select.select_by_value("ubc")

    go_button = driver.find_element_by_id("goButton")
    go_button.click()


def process_login(driver):
    """
    Enters the username and password into the corresponding text input fields,
    and logs into CWL.
    Precondition: driver is pointing to the CWL login page.
    Postcondition: driver is pointing to the "My U-Pass BC" page (with the
    "Request your U-Pass BC" table.)
    :param driver: the Selenium driver
    :return: None
    :raises: ValueError   if the username or password is invalid
    """
    login_name_input = driver.find_element_by_id("j_username")
    with open("../account/username.txt", "r") as file:
        username = file.read()
        login_name_input.send_keys(username)

    password_input = driver.find_element_by_id("password")
    with open("../account/password.txt", "r") as file:
        password = file.read()
        password_input.send_keys(password)

    continue_button = driver.find_element_by_name("action")
    continue_button.click()

    url = "https://shibboleth2.id.ubc.ca/idp/Authn/UserPassword"
    if driver.current_url == url:
        raise ValueError("Incorrect CWL credentials.")


def process_request(driver):
    """
    Checks if there is a U-Pass to request, and requests it if so.
    Precondition: driver is pointing to the "My U-Pass BC" page (with the
    "Request your U-Pass BC" table.)
    :param driver: the Selenium driver
    :return: None
    """
    try:
        request_checkbox_input = driver.find_element_by_id("chk_1")
        request_checkbox_input.click()

        print("Found U-Pass pending. Requesting...")
    except NoSuchElementException:
        print("No U-Pass pending.")
        return

    request_button = driver.find_element_by_id("requestButton")
    request_button.click()

    print("U-Pass requested.")