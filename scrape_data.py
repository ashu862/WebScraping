import requests
from bs4 import BeautifulSoup
import csv

def get_amazon_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_element = soup.find("span", attrs={"class":'a-size-base a-color-base'}).text().strip()
    if title_element:
        title = title_element.get_text().strip()
    else:
        title = "Title Not Found"

    price_element = soup.find(id="priceblock_ourprice")
    if price_element:
        price = price_element.get_text().strip()
    else:
        price = "Price Not Found"

    rating_element = soup.find(class_="a-icon-alt")
    if rating_element:
        rating = rating_element.get_text().strip()
    else:
        rating = "Rating Not Found"

    num_reviews_element = soup.find(id="acrCustomerReviewText")
    if num_reviews_element:
        num_reviews = num_reviews_element.get_text().strip()
    else:
        num_reviews = "Number of Reviews Not Found"
    
    return title, price, rating, num_reviews


def main():
    url = 'https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031&dc&qid=1708139937&rnid=1389401031&ref=lp_1389401031_nr_n_3'
    title, price, rating, num_reviews = get_amazon_data(url)
    
    with open('amazon_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Rating', 'Number of Reviews'])
        writer.writerow([title, price, rating, num_reviews])

if __name__ == "__main__":
    main()
