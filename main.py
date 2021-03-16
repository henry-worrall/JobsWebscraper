from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Monster's job website function by using the request in the URL bar to get Job descriptions.
The URLs have the structure: "https://www.monster.co.uk/jobs/search?q=" + job title searched + "&where=" + search location + "&page=" + page number.
The page number determines how many jobs are loaded up. We will want the maximum number.
Since there are 10 jobs per page, this is (the number of jobs / 10) rounded up.
Another querk is that the maximum number of results that will load for a result is 50.
Hence loading page 248 will not return the results of all the pages, but the results of the last 5.
Hence we need to loop apply the logic to pages 5, 10, 15,..., 248 etc.
The number of jobs is displayed on the page.
"""

"""
We want to load up all the jobs for our search.
For each job
    click the job
    Wait for the job description to load
    Get all of the relevant information
        Collect all text from the description
    Append the data to a python list
"""

######## PARAMETERS ###########
job = "junior developer"
location = "london"
###############################

#define where the webdriver is located
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


############ HELPER FUNCTIONS ###############
# define function for clicking, based off ID by default
def click_element(id, by=By.ID):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, str(id)))
            )
        element.click()
    except:
        print(f"Element {id} not found.")

# define function to send keystrokes to element
def send_text(id, text, by=By.ID):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, str(id)))
            )
        element.send_keys(text)
    except:
        print(f"Element {id} not found.")

# define function to gather text/data
def get_text(id, by=By.ID):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, str(id)))
            )
        return element.text
    except:
        print(f"Element {id} not found.")

# define a wait for element function
def element_wait(id, by=By.CLASS_NAME):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, str(id)))
            )
    except:
        print("Element {id} not found.")
#############################################


######## MAIN CODE #########
# navigate to desired website job search
driver.get(f"https://www.monster.co.uk/jobs/search?q={job}&where={location}&page=1")
print(driver.title)

# find and click cookies button
click_element("onetrust-accept-btn-handler")

# find the number of jobs
no_jobs = get_text("/html/body/div[1]/div[2]/div/div[1]/div[2]/h1/strong", by=By.XPATH)
no_pages = str((int(no_jobs)//10) + 1)

search_pages = [i for i in range(1,int(no_pages),5)]

r_list = []
# loop over all the relevant search pages
for page in search_pages:
    # navigate to url with all jobs
    driver.get(f"https://www.monster.co.uk/jobs/search?q={job}&where={location}&page={page}")

    element_wait("result-card")
    # find all results
    results = driver.find_elements_by_class_name("results-card")

    # loop over results
    for result in results:
        result.click()
        description = driver.find_element_by_class_name('job-description')
        r_list.append(description.text)

print(r_list)
print(len(r_list))
