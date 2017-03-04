## Store Yelp data in to SQLite Database

### This script reads data from JSON files dowloaded from [YelpChallenge](https://www.yelp.com/dataset_challenge).
### As the size of datasets are large, one table is be created each time running this script, by entering the target dataset name-- Business, review, User, Checkin, or Tip.

### From each dataset we pick certain columns:

**yelp\_academic\_dataset\_business.json** <br/>
{
    "business_id":"encrypted business id",<br/>
    "name":"business name",<br/>
    "neighborhood":"hood name",<br/>
    "address":"full address",<br/>
    "city":"city",<br/>
    "state":"state -- if applicable --",<br/>
    "postal code":"postal code",<br/>
    "latitude":latitude,<br/>
    "longitude":longitude,<br/>
    "stars":star rating, rounded to half-stars,<br/>
    "review_count":number of reviews,<br/>
    "is_open":0/1 (closed/open),<br/>
    "attributes":["an array of strings: each array element is an attribute"],<br/>
    "categories":["an array of strings of business categories"],<br/>
    "hours":["an array of strings of business hours"]<br/>
}

**yelp\_academic\_dataset\_review.json**<br/>
{<br/>
    "review_id":"encrypted review id",<br/>
    "user_id":"encrypted user id",<br/>
    "business_id":"encrypted business id",<br/>
    "stars":star rating, rounded to half-stars,<br/>
    "date":"date formatted like 2009-12-19",<br/>
    "text":"review text",<br/>
    "useful":number of useful votes received,<br/>
    "funny":number of funny votes received,<br/>
    "cool": number of cool review votes received<br/>
}

**yelp\_academic\_dataset\_user.json**<br/>
{<br/>
    "user_id":"encrypted user id",<br/>
    "name":"first name",<br/>
    "review_count":number of reviews,<br/>
    "yelping_since": date formatted like "2009-12-19",<br/>
    "friends":["an array of encrypted ids of friends"],<br/>
    "useful":"number of useful votes sent by the user",<br/>
    "funny":"number of funny votes sent by the user",<br/>
    "cool":"number of cool votes sent by the user",<br/>
    "fans":"number of fans the user has",<br/>
    "elite":["an array of years the user was elite"],<br/>
    "average_stars":floating point average like 4.31,<br/>
    "compliment_hot":number of hot compliments received by the user,<br/>
    "compliment_more":number of more compliments received by the user,<br/>
    "compliment_profile": number of profile compliments received by the user,<br/>
    "compliment_cute": number of cute compliments received by the user,<br/>
    "compliment_list": number of list compliments received by the user,<br/>
    "compliment_note": number of note compliments received by the user,<br/>
    "compliment_plain": number of plain compliments received by the user,<br/>
    "compliment_cool": number of cool compliments received by the user,<br/>
    "compliment_funny": number of funny compliments received by the user,<br/>
    "compliment_writer": number of writer compliments received by the user,<br/>
    "compliment_photos": number of photo compliments received by the user,<br/>
}

**yelp\_academic\_dataset\_checkin.json**<br/>
{<br/>
    "time":["an array of check ins with the format day-hour:number of check ins from hour to hour+1"],<br/>
    "business_id":"encrypted business id",<br/>
}

**yelp\_academic\_dataset\_tip.json**<br/>
{<br/>
    "text":"text of the tip",<br/>
    "date":"date formatted like 2009-12-19",<br/>
    "likes":compliment count,<br/>
    "business_id":"encrypted business id",<br/>
    "user_id":"encrypted user id",<br/>
}


## Note: 
Some columns such as **"categories":["an array of strings of business categories"]** are stored as TEXT in SQLite. They might be turned into unicode when later being selected from the database and presented in Pandas dataframe. <br/>
Therefore, conversion might be needed to convert the unicodes to lists or other forms for further analysis.


