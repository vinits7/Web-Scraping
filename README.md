# Web-Scraping
Web Scraping Amazon Product Data

# Web Scraping an Amazon product's data (Electronics => Computers and Accessories => Monitors) [From amazon.com]

use python,
read index.html file and parse it with beautifulsoup.

find all div with class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"

for each div from above list,
try find img with class="s-image" then link=img.src
except links=''

try find span with class="a-size-base-plus a-color-base a-text-normal" then title=span.text
except title=''

try find span with class="a-icon-alt" then rating=span.text
except rating=''

try find span with class="a-price-whole" then price=span.text
except price=''

open data.json and write link, title, rating and price.
