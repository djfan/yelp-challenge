## Data Processing for Further Analyses

Data from JSON files dowloaded from [YelpChallenge](https://www.yelp.com/dataset_challenge).


### 1. Build Table of Business Categories
(See **1.1-Yelp\_business\_category\_table.ipynb**)
Takes Yelp Business data (yelp\_academic\_dataset\_business.json)
and match business with their corresponding categories (one list or words per business).

**data file created: Yelp\_Business\_Catergory\_Table.p**
Row: Business
column: Descriptive words for the businesses (non-repetitive, from Yelp Business data)
values: 0/1
--0 if the business's categories do not include this word; 
--1 if the business's categories do include this word






