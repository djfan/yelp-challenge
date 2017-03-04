
# coding: utf-8

# In[20]:

'''
# Read Yelp Data in JSON file and write in SQLite
Each time a name (i.e. Business) will be prompted to read and import it to SQLite

# SQLite size limit for database
# 1.4e+14 bytes (140 terabytes, or 128 tebibytes, or 140,000 gigabytes or 128,000 gibibytes

####### Below might be needed for view or adjustments ##########
#!head yelp_dataset_challenge_round9/yelp_academic_dataset_Business.json

#DROP TABLE IF EXISTS Business;
#DROP TABLE IF EXISTS Checkin;
#DROP TABLE IF EXISTS Review;
#DROP TABLE IF EXISTS Tip;
#DROP TABLE IF EXISTS User;

## longitude = sqlite3_column_double(stmt, column_index_here)
'''

import json
import sqlite3

conn = sqlite3.connect('YelpData.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Business;
CREATE TABLE IF NOT EXISTS Business(
    business_id varchar(100) NOT NULL PRIMARY KEY UNIQUE,
    name TEXT UNIQUE,
    neighborhood TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    latitude DOUBLE,
    longitude DOUBLE,
    stars_biz DOUBLE,
    review_count INT,
    is_open INT,
    attributes TEXT,
    categories TEXT,
    hours TEXT
);

CREATE TABLE IF NOT EXISTS User(
    user_id varchar(100) NOT NULL PRIMARY KEY UNIQUE,
    first_name TEXT,
    review_count INT,
    yelping_since TEXT,
    friends VARCHAR(500),
    useful INT,
    funny INT,
    cool INT,
    fans INT,
    elite VARCHAR(500),
    average_stars DOUBLE,
    compliment_hot INT,
    compliment_more INT,
    compliment_profile INT,
    compliment_cute INT,
    compliment_list INT,
    compliment_note INT,
    compliment_plain INT,
    compliment_cool INT,
    compliment_funny INT,
    compliment_writer INT,
    compliment_photos INT
);

CREATE TABLE IF NOT EXISTS Review( 
    review_id varchar(100) NOT NULL PRIMARY KEY UNIQUE,
    user_id varchar(100),
    business_id varchar(100),
    stars_customer DOUBLE,
    text TEXT,
    date TEXT,
    useful INT,
    funny INT,  
    cool INT
); 

CREATE TABLE IF NOT EXISTS Checkin(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    business_id varchar(100),
    time varchar(10000)
);

CREATE TABLE IF NOT EXISTS Tip(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    text TEXT,
    date TEXT,
    likes INT,
    business_id varchar(200),
    user_id varchar(200)
)
''')

datasets = {'Business': 'yelp_academic_dataset_business.json',            'User': 'yelp_academic_dataset_user.json',            'Review':'yelp_academic_dataset_review.json',            'Checkin': 'yelp_academic_dataset_checkin.json',            'Tip':'yelp_academic_dataset_tip.json'}

dataset = raw_input('enter data set name: ')

#for dataset in datasets.iterkeys():
fname = 'yelp_dataset_challenge_round9/' + datasets[dataset]
#data = open(fname).read()
#js_data = json.loads(data)

js_data = []
with open(fname) as data:
    for line in data:
        js_data.append(json.loads(line))


################################
# import Business data
if dataset == 'Business':
    for entry in js_data:
        business_id = entry["business_id"];
        name = entry["name"];
        neighborhood = entry["neighborhood"];
        address = entry["address"];
        city = entry["city"];
        state = entry["state"];
        postal_code = entry["postal_code"];
        latitude = entry["latitude"];
        longitude = entry["longitude"];
        stars_biz = entry["stars"];
        review_count = entry["review_count"];
        is_open = entry["is_open"];
        attributes = str(entry["attributes"]);
        categories = str(entry["categories"]);
        hours = str(entry["hours"]);

        #print 
        cur.execute('''INSERT OR IGNORE INTO Business(business_id,name,neighborhood,address,city,state,postal_code,        latitude,longitude,stars_biz,review_count,is_open,attributes,categories,hours)         VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(business_id,name,neighborhood,address,city,state,postal_code,                                                  latitude,longitude,stars_biz,review_count,is_open,attributes,categories,hours) )        

    conn.commit()

########################################          
# Import User
elif dataset == 'User':
    for entry in js_data:
        user_id = entry["user_id"];
        first_name = entry["name"]; # "name": first_name
        review_count = entry["review_count"];
        yelping_since = entry["yelping_since"];
        friends = str(entry["friends"]);
        useful = entry["useful"];
        funny = entry["funny"];
        cool = entry["cool"];
        fans = entry["fans"];
        elite = str(entry["elite"]);
        average_stars = entry["average_stars"];
        compliment_hot = entry["compliment_hot"];
        compliment_more = entry["compliment_more"];
        compliment_profile = entry["compliment_profile"];
        compliment_cute = entry["compliment_cute"];
        compliment_list = entry["compliment_list"];
        compliment_note = entry["compliment_note"];
        compliment_plain = entry["compliment_plain"];
        compliment_cool = entry["compliment_cool"];
        compliment_funny = entry["compliment_funny"];   ###?? the same with compliment_cool???
        compliment_writer = entry["compliment_writer"];
        compliment_photos = entry["compliment_photos"];

        cur.execute('''INSERT OR IGNORE INTO User(user_id,first_name,review_count,yelping_since,friends,useful,funny,cool,fans,elite,                     average_stars,compliment_hot,compliment_more,compliment_profile,compliment_cute,                     compliment_list,compliment_note,compliment_plain,compliment_cool,compliment_funny,                     compliment_writer,compliment_photos)         VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',                    (user_id,first_name,review_count,yelping_since,friends,useful,funny,cool,fans,elite,                     average_stars,compliment_hot,compliment_more,compliment_profile,compliment_cute,                     compliment_list,compliment_note,compliment_plain,compliment_cool,compliment_funny,                     compliment_writer,compliment_photos) )

    conn.commit()     


########################################    
# import Review data
elif dataset == 'Review':
    for entry in js_data:
        review_id = entry["review_id"];
        user_id = entry["user_id"];
        business_id = entry["business_id"];
        stars_customer = entry["stars"];  #change the name
        text = entry["text"];
        date = entry["date"];
        useful = entry["useful"];
        funny = entry["funny"];
        cool = entry["cool"];

        cur.execute('''INSERT OR IGNORE INTO Review(review_id,user_id,business_id,stars_customer,text,date,useful,        funny,cool)        VALUES(?,?,?,?,?,?,?,?,?)''',(review_id,user_id,business_id,stars_customer,text,date,useful,                                      funny,cool) )

    conn.commit()     

########################################  
# Import Checkin
elif dataset == 'Checkin':
    for entry in js_data:
        business_id = entry["business_id"];
        time = str(entry["time"]);

        cur.execute('''INSERT OR IGNORE INTO Checkin(business_id,time) VALUES(?,?)''',(business_id,time) )

    conn.commit()  

########################################  
# Import Tips
elif dataset == 'Tip':
    for entry in js_data: 
        text = entry["text"];
        date = entry["date"];
        likes = entry["likes"];
        business_id = entry["business_id"];
        user_id = entry["user_id"];
        #type_ = entry["type_"]

        cur.execute('''INSERT OR IGNORE INTO Tip(text,date,likes,business_id,user_id)         VALUES(?,?,?,?,?)''',(text,date,likes,business_id,user_id) )

    conn.commit()

cur.close()

