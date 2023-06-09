import argparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TempMail import TempMail
import time
import re
import random
import string
from tqdm import tqdm

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", action="store_true", help="Use a random proxy from the site!")
    return parser.parse_args()

# Function to generate a random password
def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

# Function to get a list of working HTTP/HTTPS proxies
def get_proxies():
    url = "https://www.sslproxies.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    proxy_table = soup.find("table", class_="table table-striped table-bordered")
    if proxy_table:
        rows = proxy_table.find_all("tr")
        proxies = []
        for row in rows[1:]:
            columns = row.find_all("td")
            if len(columns) >= 2:
                ip = columns[0].text
                port = columns[1].text
                proxy = f"{ip}:{port}"
                proxies.append(proxy)
        return proxies
    else:
        return []

args = parse_arguments()

# Create a new TempMail object
print("Creating a new TempMail object...")
tmp = TempMail()

# Generate an inbox
print("Generating an inbox...")
inb = TempMail.generateInbox(tmp)

# Define the URL of the sign-up page
signup_url = "https://beta.elevenlabs.io/sign-up"

# Define the path to your chromedriver (change it according to your path)
driver_path = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"

# Set the proxy options for the Chrome driver
chrome_options = webdriver.ChromeOptions()

if args.proxy:
    # Get a list of working HTTP/HTTPS proxies
    proxies = get_proxies()
    print("Total Proxies:", len(proxies))

    # Select a random proxy from the list
    if proxies:
        proxy = random.choice(proxies)
        print("Selected Proxy:", proxy)
        chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    else:
        print("No working proxies found.")

# Create a new instance of the Chrome driver with proxy options
print("Creating a new instance of the Chrome driver...")
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Go to the sign-up page
print("Navigating to the sign-up page...")
driver.get(signup_url)

# Wait for the page to load
wait = WebDriverWait(driver, 30)

# Generate a random password
password = generate_password(10)

# Find the email input field and enter the temporary email
print("Entering the temporary email...")
email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]')))
email_field.send_keys(inb.address)  # Use the address property of the Inbox object

# Find the password input field and enter the password
print("Entering the password...")
password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password_field.send_keys(password)

# Find the terms checkbox and click it
print("Checking the terms checkbox...")
terms_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="terms"]')))
terms_checkbox.click()

# Find the sign-up button and click it
print("Clicking the sign-up button...")
sign_up_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
sign_up_button.click()

# Wait for the confirmation email
print("Waiting for the confirmation email...")
for i in tqdm(range(30)):
    time.sleep(1)

# Check for emails
print("Checking for emails...")
emails = TempMail.getEmails(tmp, inbox=inb)

# If there is a confirmation email
if emails:
    # Get the confirmation link
    print("Getting the confirmation link...")
    confirmation_link = re.search("(?P<url>https?://[^\s]+)", emails[0].body).group("url")

    # Visit the confirmation link
    print("Visiting the confirmation link...")
    driver.get(confirmation_link)

    # Wait for 10 seconds
    print("Waiting for 30 seconds...")
    for i in tqdm(range(30)):
        time.sleep(1)

    # Save the email and password to a file
    print("Saving the email and password to a file...")
    with open("accounts.txt", "a") as file:
        file.write("-------------------------------------\n")
        file.write(f"Email: {inb.address}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Confirmation Link: {confirmation_link}\n")

# Close the driver
print("Closing the driver...")
driver.quit()

print("Done!")
