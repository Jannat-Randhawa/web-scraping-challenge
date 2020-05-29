#Dependencies 
import pandas as pd 
from bs4 import BeautifulSoup 
from splinter import Browser 
import requests 
import os
import time

#Site Navigation
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape(): 
    browser = init_browser()

    #NASA Mar News 
    news_url = "http://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find("div", class_='content_title').text
    news_p = soup.find("div", class_='article_teaser_body').text
    print(f"News Title: {news_title}")
    print(f"News Paragraph: {news_p}")

    #JPL Mars Space Images - Featured Image
    main_url = "https://www.jpl.nasa.gov"
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image_results = soup.find("ul", class_="articles")
    image_href = image_results.find("a", class_='fancybox')['data-fancybox-href']
    featured_image_url = main_url + image_href
    featured_image_url

    #Mar Weather 
    twitter_url = "https://twitter.com/marswxreport?lang=en"

    browser.visit(twitter_url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    spans=soup.find_all('span')
    for span in spans:
        if 'InSight sol ' in span.text:
            print(span.text)
            mars_weather = span.text
            break
    mars_weather

    #Mars Facts 
    table_facts = pd.read_html("https://space-facts.com/mars/")
    mars_df = table_facts[0]
    mars_df_new.columns = ["Category", "Measurements"]
    mars_facts = mars_df_new.set_index("Category")
    mars_facts

    #Mar Hemisphere 
    import time
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    time.sleep(3)
    hemispheres_main_url = 'https://astrogeology.usgs.gov'
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    div_items = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    hemispheres_main_url = 'https://astrogeology.usgs.gov'
    for item in div_items: 
        title = item.find('h3').text
        end_points = item.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_main_url + end_points)
        image_html = browser.html
        soup = BeautifulSoup( image_html, 'html.parser')
        image_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"Title": title, "Image_URL": image_url})

    hemisphere_image_urls

    mars_dict = {"news_title": news_title, "news_text": news_p, "featured_image": featured_image_url,
    "mars_weather": mars_weather, "mars_facts":mars_facts, "hemispheres_images": hemisphere_image_urls}
    return mars_dict

    browser.quit()