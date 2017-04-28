library(quanteda)
library(tidytext)
library(topicmodels)
library(ldatuning)
library(stringi)

review = read.csv("./Documents/Spring2017/CUSP_5006_ML4C/yelp-challenge/Anomaly/torronto_chi.csv",
                  stringsAsFactors = FALSE)
rw = aggregate(review$text ~ review$business_id, review, paste0)
review_dfm = dfm(rw$`review$text`, removePunct = T, remove = stopwords("english"))
review_dfm = dfm_trim(review_dfm, min_count=1, min_docfreq=20)
print("remaining number of words"); print(review_dfm@Dim[2])
print("remaining number of documents"); print(review_dfm@Dim[1])
