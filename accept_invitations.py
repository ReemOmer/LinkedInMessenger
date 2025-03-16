import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
myemail = os.getenv("EMAIL")
mypassword = os.getenv("PASSWORD")

##################################### Web Driver #####################################

# Create a new instance of the Chrome WebDriver
service = Service(executable_path=r'C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

##################################### Login #####################################

driver.maximize_window()
url = "https://www.linkedin.com/login"

driver.get(url)

# Locate the username and password fields and the login button

driver.implicitly_wait(5)  

username_field = driver.find_element(By.ID,'username')
password_field = driver.find_element(By.ID,'password')
login_button = driver.find_element(By.CLASS_NAME,  "btn__primary--large.from__button--floating")

# Enter your username and password
username_field.send_keys(myemail)
time.sleep(5)

password_field.send_keys(mypassword)
time.sleep(5)

# Click the login button to submit the form
login_button.click()
time.sleep(30)

##################################### CONTENT #####################################

# After logging in, you can perform further actions on the webpage as needed
# we could actually automate this step as well by clicking on connections >> people

# Create a list of YouTube links to select one randomly to add it to the message
Youtube_links = [
                'https://www.youtube.com/watch?v=kpnNItRw3Fc&', 
                'https://www.youtube.com/watch?v=u04ThDjshh0&', 
                'https://www.youtube.com/watch?v=tlwxM_FJZEs&', 
                'https://www.youtube.com/watch?v=LTeZ-2OOPC8&', 
                'https://www.youtube.com/watch?v=eFN1gs8Dve8&', 
                'https://www.youtube.com/watch?v=T0VoaHCA8j0&', 
                'https://www.youtube.com/watch?v=zz5V_7NOmWo&', 
                'https://www.youtube.com/watch?v=R8iNMD_yHlE&', 
                'https://www.youtube.com/watch?v=HlyYJq5H74k&', 
                'https://www.youtube.com/watch?v=QvXRkGpZKR0&'
                ]


# Split the message into paragraphs to that it is easy to add names and YouTube links later
phrase_ar1 = "السلام عليكم يا "
phrase_ar2 = """

شكراً ليك على طلب الإضافة! جزاك الله خير.

أنا اسمي ريم، بشتغل في مجال علوم البيانات وعندي 6 سنين خبرة في المجال ده.

قبل فترة بدأت قناة في يوتيوب عشان أشارك فيها محتوى تفصيلي عن علوم البيانات، التحليل، التصوير البياني، وكل حاجة بتتعلق بالبيانات. حيكون شرف لي لو انضمّيت لي القناة!

"""
phrase_ar3 = """

حابّة جداً أسمع رأيك في الفيديو الفوق!

تحياتي،

--------------------

"""

phrase_en1 = "Salaam "
phrase_en2 = """

Thank you for the connection request! I appreciate your gesture.

My name is Reem, and I work as a data scientist with 6 years of experience in the field.

I have started this YouTube channel to share detailed content about data science, analysis, visualization, and everything related to data. I would be delighted if you joined me there as well!

"""
phrase_en3 = """

I would love to hear your feedback on the video above!

Cheers,
"""

##################################### MAIN #####################################

# Create a string object for the link of the connections page
invitation_page_base = 'https://www.linkedin.com/mynetwork/invitation-manager/?invitationType=CONNECTION'


# I have 3 pages in my case, we could also use the pagination to identify the numbe
for i in range(2):

    invitation_page = invitation_page_base + '&page=' + str(i + 1)

    driver.get(invitation_page)

    # scroll the page down to get the full list of invited connections
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

    # Locate the <ul> element 
    ul_element = driver.find_element(By.CLASS_NAME, "artdeco-list.mn-invitation-list")

    # Find all <li> elements with the class 'invitation-card'
    li_elements = driver.find_elements(By.CLASS_NAME, "invitation-card.artdeco-list__item") 
    print(len(li_elements))

    # Iterate through each <li> elements (list of connection requests; pagess + invitations)
    for li in li_elements:
        
        try:
            
            time.sleep(5)

            accept_button = li.find_element(By.XPATH, ".//div[1]/div[2]/button[2]")
            accept_button.click()
            time.sleep(3)

            message_button = li.find_element(By.XPATH, ".//div/div[1]/div/div[2]/button")
            message_button.click()
            time.sleep(3)

            name_element = driver.find_element(By.XPATH, "//a[contains(@class, 'profile-card-one-to-one__profile-link')]//span[@class='truncate']")
            person_name = name_element.text

            # Wait for the message container to open
            message_container = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.msg-overlay-conversation-bubble")))

            message_container = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.msg-overlay-conversation-bubble")))
            

            # Write the message in the text area
            message_box = message_container.find_element(By.CSS_SELECTOR, "div.msg-form__contenteditable")
            message_box.send_keys(Keys.CONTROL, 'a')  # Select all existing text
            message_box.send_keys(Keys.DELETE)        # Delete it

            Youtube_link = random.choice(Youtube_links)
            full_message = phrase_ar1 + person_name + phrase_ar2 + Youtube_link + phrase_ar3 + phrase_en1 + person_name + phrase_en2 + Youtube_link + phrase_en3

            message_box.send_keys(full_message)
            time.sleep(3)

            # Send the message to the new connection
            send_button = message_container.find_element(By.CSS_SELECTOR, "button.msg-form__send-button")
            send_button.click()
            time.sleep(3)

            # Close the message window
            header = WebDriverWait(driver, 5).until(
                                            EC.presence_of_element_located((By.CSS_SELECTOR, "header.msg-overlay-conversation-bubble-header")))
            buttons = header.find_elements(By.TAG_NAME, "button")
            buttons[-1].click()
            time.sleep(3)
            
        except Exception as e:
            print(f"Error processing 'Withdraw' action in li element: {e}")
            break
    break
driver.close()