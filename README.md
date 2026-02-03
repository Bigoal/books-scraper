**Books Scraper 📚✨**

Simple, friendly, and reliable scraper for http://books.toscrape.com/.
Scrapes title, price, rating, availability and the book page link — then saves everything to a CSV so you can analyze or share the data.

---

**Quick highlights**
- Tiny single-file scraper (scraper.py) — easy to run.
- Output: data/books_data.csv
- Great for learning web scraping, data cleaning, or building demos.

---

**Run it (3 steps)**
python -m venv .venv
# activate .venv (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python scraper.py --start 1 --end 3 --output data/books_data.csv

---

**Example excerpt from the scraped CSV**

Below is a small sample (5 rows) showing the kind of table the scraper produces:

| title | price_£ | rating | stock | book_link |
| ----- | -------:| ------:| ------| --------- |
| A Light in the Attic | 51.77 | 3 | In stock | http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html |
| Tipping the Velvet | 53.74 | 1 | In stock | http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html |
| Soumission | 50.10 | 1 | In stock | http://books.toscrape.com/catalogue/soumission_998/index.html |
| Sharp Objects | 47.82 | 4 | In stock | http://books.toscrape.com/catalogue/sharp-objects_997/index.html |
| Sapiens: A Brief History of Humankind | 54.23 | 5 | In stock | http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html |

Tip: to copy more rows from your CSV, run:
head -n 6 data/books_data.csv
Then paste the output into this table.

---

**What's inside this repo**
- scraper.py — the scraping script (simple & well-commented)
- requirements.txt — libraries used
- data/books_data.csv — scraped output (sample or your real data)
- .gitignore — ignores virtualenv and other generated files

---

**Want to improve it?**
- Add --delay between requests to be extra polite.
- Save JSON or parquet for faster data loading.
- Add a small test to ensure parsing keeps working when the site changes.

---

**License**
MIT — free to use, tweak and share.
