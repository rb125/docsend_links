import getpass, csv, time, argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from progress.bar import ShadyBar

#Get csv file as input
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()
csv_file_path = args.file
num_accounts = 0
with open (csv_file_path, "r") as f:
    num_accounts = len(f.readlines())

# Define the DocSend website URL
docsend_url = 'https://www.docsend.com/'

# Define the email address and password for the DocSend account
docsend_email = input("Enter your docsend username:")
docsend_password = getpass.getpass("Enter your docsend password:")
default_link = input("Enter link to your docsend document:")

# Set up the Chrome driver options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://docsend.com/login")
driver.find_element(By.ID, "login_user_email").send_keys(docsend_email)
driver.find_element(By.ID, "login_user_password").send_keys(docsend_password)
driver.find_element(By.ID, "sign-in-button").submit()
time.sleep(1)



#Function to create docsend link
def create_docsend_link(account):
    driver.get(default_link)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.js-create-link-button").click()
    time.sleep(2)
    driver.find_element(By.NAME, "link_form[name]").send_keys(account)
    driver.find_element(By.NAME, "commit").submit()
    time.sleep(2)
    docsend_link = driver.find_element(By.CSS_SELECTOR, "div.link-url").text
    return docsend_link


def create_links():
    bar = ShadyBar('Creating Links:', max = num_accounts)
    list_of_links = []
    with open(csv_file_path, newline='') as csvfile:
        list_reader = csv.reader(csvfile, delimiter=",")
        for row in list_reader:
            account = row[0]
            docsend_link = create_docsend_link(account)
            bar.next()

            list_of_links.append([account, docsend_link])
    bar.finish()
    return list_of_links

def write_output():
    links = create_links()
    timestamp = time.time()
    output_file = "docsend_list_"+str(timestamp)+".csv"
    fields = ["account", "docsend_link"]
    with open(output_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(links)

write_output()
