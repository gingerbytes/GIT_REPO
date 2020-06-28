
'''
TASK: Import any libraries you think you'll need to scrape a website.
'''
import requests
import bs4

'''
TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/
and get the HMTL text from the homepage.
'''

res = requests.get("http://quotes.toscrape.com/")
# print(res.text)

'''
TASK: Get the names of all the authors on the first page.
'''

soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.select(".author"))

authors = set()  # get unique names only by using set()
for name in soup.select(".author"):
    authors.add(name.text)
# print(authors)

'''
TASK: Create a list of all the quotes on the first page.
'''
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

# print(quotes)

'''
TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests
text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).

HINT: Keep in mind there are also tags underneath each quote, try to find a class only
present in the top right tags, perhaps check the span.
'''
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.tag-item')
for item in soup.select(".tag-item"):
    # print(item.text)
    pass

'''
TASK: Notice how there is more than one page, and subsequent pages look like this 
http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation
to loop through all the pages and get all the unique authors on the website. Keep in mind
there are many ways to achieve this, also note that you will need to somehow figure out
how to check that your loop is on the last page with quotes. For debugging purposes, I will
let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/,
but try to create a loop that is robust enough that it wouldn't matter to know the amount
of pages beforehand, perhaps use try/except for this, its up to you!

'''

url = 'http://quotes.toscrape.com/page/'
for page in range(1, 10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)  # this is defined on top as a set()

'''
Possible Solution #2 ( Unknown Number of Pages, but knowledge of last page)

Let's check what the last invalid page looks like:
'''

# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text, 'lxml')

# This solution requires that the string "No quotes found!" only occurs on the last page.
# If for some reason this string was on the other pages, we would need to be more detailed.
"No quotes found!" in res.text

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to Next Page
    page += 1

print(authors)

'''
There are lots of other potential solutions that are even more robust and flexible,
the main idea is the same though, use a while loop to cycle through potential pages and have
a break condition based on the invalid page.
'''
