

**1. Naive Bayes**

```
## Confusion Matrix and Statistics

##              conf_actual
## conf_pred_c   chinese non-chinese
##   chinese         517        1895
##   non-chinese     154        2148

##  Accuracy 
## 0.5653373
## Precision 
## 0.2143449
##    Recall 
## 0.7704918
```

*problems*: 

1. Naive Bayes function in `sklearn` provide `bernouliNB` and `multinomialNB` for categorical data. However, difficult to deal with **NA data**.
2. naiveBayes in `e1701` is quite helpful to do with NA data by set `na_action`. However, it seems to treat all as Gaussian Distribution. I set `as.factor` for all variables, and not figure out for now which distribution it applied. 
3. In a word,  naive bayes is not suitable for this data set, because NA problem and not independent between attributes.

