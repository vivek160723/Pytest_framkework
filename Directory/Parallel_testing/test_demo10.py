import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestWebsiteLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        yield driver
        driver.quit()

    @pytest.mark.parametrize("email,password", [
        ("test@example.com", "password123"),
        ("admin@example.com", "wrongpass"),
        ("invalid@example.com", "user123"),
        ("guest@example.com", "guest123")
    ])
    def test_email_password(self, setup, email, password):
        driver = setup

        # Find the email and password input fields and login button
        email_field = driver.find_element(By.ID, "email")  # Update with actual ID or locator
        password_field = driver.find_element(By.ID, "passwd")  # The ID might be 'passwd' for password field
        login_button = driver.find_element(By.ID, "SubmitLogin")  # This is the usual ID for the submit button

        # Clear fields and input data
        email_field.clear()
        password_field.clear()
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()

        # Check for expected behavior (e.g., error message or redirection)
        try:
            # Check for redirect to the account page (successful login)
            if email == "test@example.com" and password == "password123":
                assert "My account" in driver.title  # After login, the title should contain "My account"
            else:
                # If invalid credentials, an error message should be shown
                error_message = driver.find_element(By.CSS_SELECTOR,
                                                    ".alert.alert-danger li").text  # CSS selector for error message
                assert "Invalid email address." in error_message or "Authentication failed." in error_message  # Error messages based on website
        except Exception as e:
            pytest.fail(f"Test failed due to {str(e)}")