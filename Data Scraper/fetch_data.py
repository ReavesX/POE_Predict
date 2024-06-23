from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def fetch_data(league,scraped_data):
    """
    Fetches  data from Path of Exile's poe.ninja for a specified league using Selenium and BeautifulSoup.

    Args:
    - league (str): The league name for which currency data is to be fetched.
    - scraped_data (list): The array for which the scraped data is appended to

    """



    # Initialize the WebDriver and provide the url
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"https://poe.ninja/economy/{league}/currency")

    # Wait for the page to load completely, then extract the page source once it is completely loaded
    driver.implicitly_wait(10)
    page_source = driver.page_source


    soup = BeautifulSoup(page_source, 'html.parser') # Parse the page source

    # For every row in the parsed site find all cells which contain 'td'
    # Then, provided there is text in the cell, get the text value in the cell, which contains the item name and item value 
    # finally append to the placeholder list


    for row in soup.select('table tbody tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            name = cells[0].get_text(strip=True)
            buy_price = cells[1].get_text(strip=True)
            sell_price = cells[2].get_text(strip=True)
            scraped_data.append({'name': name, 'Buy value': buy_price, 'Sell Value': sell_price })

    # Last, close the driver and return the list
    driver.quit()
    return scraped_data

print(fetch_data('necropolis',scraped_data = []))