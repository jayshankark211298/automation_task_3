import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DragAndDropDemo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://jqueryui.com/droppable/"

    def navigate_to_page(self):
        self.driver.get(self.url)

    def switch_to_iframe(self):
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "demo-frame"))
        )
        self.driver.switch_to.frame(iframe)

    def perform_drag_and_drop(self):
        # Locate draggable and droppable elements
        draggable_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "draggable"))
        )
        droppable_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "droppable"))
        )

        # Scroll the draggable element into view
        self.driver.execute_script("arguments[0].scrollIntoView();", draggable_element)

        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Perform drag and drop
        actions.drag_and_drop(draggable_element, droppable_element).perform()
        time.sleep(5)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close_driver(self):
        self.driver.quit()

    def run(self):
        self.navigate_to_page()
        self.switch_to_iframe()
        self.perform_drag_and_drop()
        self.switch_to_default_content()
        self.close_driver()


# Create an instance of the class and run the script
if __name__ == "__main__":
    demo = DragAndDropDemo()
    demo.run()
