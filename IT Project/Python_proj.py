#General Imports and Scraping
import sys
import requests
from bs4 import BeautifulSoup
# Import for NLP
from textblob import TextBlob
# Import for ploting Library


WEB_PAGE_TO_SCRAPE_URL = "http://techcrunch.com/"

#requests.get('http://www.google.com')
response = requests.get(WEB_PAGE_TO_SCRAPE_URL)

#response_text = response.txt

fetched_html = response.text
fetched_html[:500]

fetched_html = ''
with open('techcrunch.html','r') as f:
    fetched_html = f.read()
fetched_html[:500]

#BeatautifulSoup(YOUR_RAW_HTML_TEXT,'html.parser')

souped_page = BeautifulSoup(fetched_html,'html.parser')
souped_page.find('title').getText()

souped_page.find('ul')
#Finite Searching
element_search = souped_page.find('ul',{'class':'river'})
#Matches Attributues
element_search.attrs

article_listings = souped_page.find_all('li',{'class':'river-block'})

print('Number of Article :',len(article_listings))
print('printing article titles \n')

for a in article_listings:
    if 'data-sharetitle' in a.attrs:
        print(a['data-sharetitle'])

## Test ##
backup_article = ''
with open('techcrunch_article.html','r') as f:
    backup_article = f.read()
ARTICLE_URL = 'https://techcrunch.com/2018/02/25/gobee-bike-throws-in-the-towel-on-france/'

article_response = requests.get(ARTICLE_URL)
article_soup = BeautifulSoup(article_response.text, 'html.parser')
article_body = article_soup.find('div',{'class':['article-entry']})
article_body

article_text = article_body.getText().replace('\n',' ')
article_text

print (article_body)

########################################
## NLP
## Test
my_text_blob_object = TextBlob('this is some test text')
my_text_blob_object.sentiment

processed_text = TextBlob(article_text)

print(processed_text.sentiment)

# split up text into sentences
sentences = article_text.split('.')
# loop for each sentence
for sentence in sentences:

    # get sentiment score for sentence
    sentence_sentiment = TextBlob(sentence).sentiment

    # if the subjectivity(opinionated) score is greater than 0.5 then 
    # print out the sentence with the score    
    if  sentence_sentiment.subjectivity > 0.5:
        print(sentence, sentence_sentiment.subjectivity)

##############################################
## Plotting
# draw plot in notebook
%matplotlib inline

# get all word indevidually by splitting on every space
words = article_text.split(' ')

# big it a big plot
plt.figure(figsize=(12,7))

# for each word draw the text on teh char using the sentiment score as the x and y coordinates
for word in words:
    word_sentiment = TextBlob(word).sentiment
    plt.text(word_sentiment.polarity, # x coordinate
             word_sentiment.subjectivity, # y coordinate
             word) # the text to draw

# set axis ranges 
plt.xlim(-1, 1)
plt.ylim(0, 1)

# draw line in middle
plt.axvline(0, color='red', linestyle='dashed')

# label axis
plt.title('Sentiment analysis of words')
plt.xlabel('Polarity (positive(love) or negative(hate))')
plt.ylabel('Subjectivity (0 - purly objective, 1 - purly subjective)')

# display
plt.show()

