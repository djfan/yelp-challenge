library(quanteda)
library(tidytext)
library(topicmodels)
library(ldatuning)
library(stringi)
load('Documents/Spring2017/DSGA_3001_Text/HW/HW3/custom_stopwords.RData')
review = read.csv("~/Desktop/all_chinese_rw.csv",stringsAsFactors = FALSE, encoding = 'utf-8')
rw = review
food_stopwords = c('food', 'good', 'place', 'get', 'great', 'service', 
                   'restaurant', 'got', 'really', 'can', 'order', 'time',
                   'back', 'nice', 'love', 'make')
review_dfm = dfm(rw$text, removePunct = T, remove = c(stopwords("english"), stopwords("german"), stopwords("french"), custom_stopwords,food_stopwords))
#review_dfm = dfm_trim(review_dfm, min_count=5, min_docfreq=5)
print("remaining number of words"); print(review_dfm@Dim[2])
print("remaining number of documents"); print(review_dfm@Dim[1])

rw_topic = LDA(review_dfm, k=15, method = "Gibbs", control = list(iter = 100))
#top10_word2topic = get_terms(rw_topic, 10)
top30_word2topic = get_terms(rw_topic, 30)

topics.per.document <- function(m, as.wordassignments=F) {
  ids = as.numeric(m@documents)
  if(as.wordassignments) {
    tpd = t(documentsums(m))
  } else{
    tpd = posterior(m)$topics  
  }
  cbind(id=ids, data.frame(tpd))
}
topic2doc = as.data.frame(topics.per.document(rw_topic))
topic2doc = topic2doc[,-1]
topic2doc['max'] = apply(topic2doc, 1, which.max)
table(topic2doc$max)

write.csv(topic2doc, file='topic2doc.csv') 
write.csv(top30_word2topic, file = 'top30_word2topic.csv')
write.csv(top10_word2topic, file = 'top10_word2topic.csv')
