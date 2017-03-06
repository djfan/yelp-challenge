## Data Processing for Further Analyses

Data from JSON files dowloaded from [YelpChallenge](https://www.yelp.com/dataset_challenge).


### 1. Build Table of Business Categories
(See [**1.1-Yelp\_business\_category\_table.ipynb**](https://github.com/Alan-F/yelp-challenge/blob/master/data_processeing/1.1-Yelp_business_category_table.ipynb)) <br/>
Takes Yelp Business data (yelp\_academic\_dataset\_business.json)<br/>
and match business with their corresponding categories (one list or words per business).<br/>

**data file created: Yelp\_Business\_Catergory\_Table.p**  (appox.1.4GB)<br/>
Row: Business <br/>
Column: Descriptive words for the businesses (non-repetitive, from Yelp Business data)<br/>
values: 0/1<br/>
    --0 if the business's categories do not include this word; <br/>
    --1 if the business's categories do include this word<br/>






