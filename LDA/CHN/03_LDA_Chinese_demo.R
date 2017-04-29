library(quantedaData)
library(quanteda)
library(tidytext)
library(topicmodels)
library(ldatuning)
library(stringi)

review = read.csv("./Documents/Spring2017/CUSP_5006_ML4C/yelp-challenge/Anomaly/torronto_chi.csv",
                  stringsAsFactors = FALSE)
review_dfm = dfm(review$text, removePunct = T, remove = stopwords("english"))
review_dfm = dfm_trim(review_dfm, min_count=1, min_docfreq=20)
print("remaining number of words"); print(review_dfm@Dim[2])
print("remaining number of documents"); print(review_dfm@Dim[1])

rowTotals <- apply(review_dfm , 1, sum)
rw_dfm_new <- review_dfm[rowTotals> 0, ]

rw_topic = LDA(rw_dfm_new, k=5, method = "Gibbs", 
                control = list(iter = 100))
top10_word2topic = get_terms(rw_topic, 10)


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
