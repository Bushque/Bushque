import selenium
import requests
import bs4
import pandas

# List of URLs for construction material categories on Lemanapro
CATEGORIES = {
    "keramogranit": "https://lemanapro.ru/catalogue/keramogranit/",
}

# Headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://lemanapro.ru/",
}

# Function to parse prices
def get_prices(url):
    """Parses prices for construction materials from the specified URL."""
    try:
        # Send a request to the website
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all product cards
        products = soup.find_all('div', class_='product-card')

        # Collect data
        data = []
        for product in products:
            name = product.find('span', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            price = float(price.replace('₽', '').replace(',', '.').strip())
            data.append({'name': name, 'price': price})

        return data

    except Exception as e:
        print(f"Error while parsing the website: {e}")
        return []

# Function to save data to CSV
def save_to_csv(data, file="material_prices.csv"):
    """Saves data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(file, index=False, encoding='utf-8')
    print(f"Data saved to file {file}")

# Function to find the cheapest material
def find_cheapest(data):
    """Finds the cheapest material in the data."""
    if not data:
        return None

    # Find the material with the minimum price
    cheapest = min(data, key=lambda x: x['price'])
    return cheapest

# Main function
def monitor_prices():
    """Main function for price monitoring."""
    all_data = []

    # Iterate through all categories
    for category, url in CATEGORIES.items():
        print(f"Parsing category: {category}...")
        data = get_prices(url)
        if data:
            # Add category to the data
            for product in data:
                product['category'] = category
            all_data.extend(data)
        else:
            print(f"Failed to retrieve data for category: {category}")

    if not all_data:
        print("No data for analysis.")
        return

    # Print data
    for product in all_data:
        print(f"Category: {product['category']}, Material: {product['name']}, Price: {product['price']} RUB")

    # Save data to CSV
    save_to_csv(all_data)

    # Find the cheapest material
    cheapest = find_cheapest(all_data)
    if cheapest:
        print("\nCheapest material:")
        print(f"Category: {cheapest['category']}, Material: {cheapest['name']}, Price: {cheapest['price']} RUB")
    else:
        print("Failed to find the cheapest material.")

# Run the monitoring
if __name__ == "__main__":
    monitor_prices()