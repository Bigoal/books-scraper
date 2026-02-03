from scrapy.selector import Selector
import requests
import csv
import re

url = "http://books.toscrape.com/"

def extract_page_data(book_element):
    sel = Selector(text=book_element.text)
    # Price extracting and cleaning
    Prices = []
    Prices_String = sel.css(".price_color::text").getall()
    Prices= [   float(re.sub(r"[^\d.]", "", p))
                for p in Prices_String
                if p and re.sub(r"[^\d.]", "", p)]
    # Links extracting and adding the pre url 
    Links=[]
    Links_Directory = sel.css(".image_container a::attr(href)").getall()
    for item in Links_Directory:
        link = url
        if not item.startswith("catalogue/"):
            link += "catalogue/"
        link+= item
        Links.append(link)
    # Titles extracting
    Titles = sel.css("h3 a::attr(title)").getall()
    # Ratings extracting and converting it to numbers
    Ratings_string= sel.css(".image_container + p::attr(class)").getall()
    Ratings= []
    for rating in Ratings_string:
        if "One" in rating: 
            Ratings.append(1)
        if "Two" in rating: 
            Ratings.append(2)
        if "Three" in rating: 
            Ratings.append(3)    
        if "Four" in rating: 
            Ratings.append(4)
        if "Five" in rating: 
            Ratings.append(5)
    # Availability extracting
    Availability= sel.css(".instock.availability::text").getall()
    Availability=[s.strip() for s in Availability
                if s and s.strip()]

    Page_data= [
    {
        "Title": t,
        "Price_£": p,
        "Rating": r,
        "Availability":a,
        "Book_link": l
    }
    for t, p, r, a, l in zip(Titles, Prices, Ratings,Availability,Links)]
    return Page_data
def save_to_csv(books_data, filename="books_data.csv"):
    if not books_data:
        print("No data to save!")
        return
    
    # Define fieldnames
    fieldnames = ["title", "price_£", "rating", "stock", "book_link"]
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        # Write clean data
        for book in books_data:
            clean_book = {
                "title": book["Title"],
                "price_£": book["Price_£"],
                "rating": book["Rating"],
                "stock": book["Availability"],
                "book_link": book["Book_link"]
            }
            writer.writerow(clean_book)
    
    print(f"Data saved to {filename}")


Final_Data= []
for i in range(1,51):
    Current_url= url + "catalogue/page-"+ str(i) +".html"
    response = requests.get(Current_url)
    Final_Data= Final_Data + (extract_page_data(response))
save_to_csv(Final_Data)
