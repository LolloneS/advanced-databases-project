# Advanced Databases 2CFU Project's Report
# Global Commodity Trade Statistics 
# Lorenzo Soligo - 806954

## Abstract
Comparison between the performances of MongoDB and MySQL with and without indexes whilst working with a huge dataset (~1GB, 8+ million rows) representing trades statistics for many countries.


## Dataset
[Global Commodity Trade Statistics](https://www.kaggle.com/unitednations/global-commodity-trade-statistics) by [United Nations](https://www.kaggle.com/unitednations)

### Fields
The dataset fields are:
* `country_or_area`:
  * name of the country or area the trade refers to
* `year`:
  * year in which the trade was done
* `comm_code`
  * code of the commodity traded
* `commodity`
  * name of the commodity traded
* `flow`
  * flow of the trade: Import, Export, ...
* `trade_usd`
  * amount of the trade, in US dollars
* `weight_kg`
  * weight of the commodity traded, in kilograms
* `quantity_name`
  * type of quantity (e.g. number of items, weight in kilograms, ...)
* `quantity`
  * number representing the quantity (e.g. number of items = 5)
* `category`
  * category of the trade


### Modeling the dataset
Luckily, the dataset is well structured. This let me work with it without worrying too much about preprocessing the data.

In MongoDB, I simply needed to import the CSV as-is with `mongoimport`. This turned out to be a huge help: I ran some tests involving preprocessing the data (using Python3 and PyMongo) and importing the data took many times the time it takes with `mongoimport`.

In MySQL, I decided to split the dataset and put the fields `commodity`, `comm_code` and `category` in a table `commodity`, using `comm_code` as the primary key. This let me save some space, since the same commodities (and relative codes/categories) are often repeated thousands of times.




## MongoDB
* One database
* One collection (*countries*)

### Document structure (example):
```js
{
	"_id" : ObjectId("5b03f43b423dfaf4de96cfe6"),
	"country_or_area" : "Afghanistan",
	"year" : 2016,
	"comm_code" : 10410,
	"commodity" : "Sheep, live",
	"flow" : "Export",
	"trade_usd" : 6088,
	"weight_kg" : 2339,
	"quantity_name" : "Number of items",
	"quantity" : 51,
	"category" : "01_live_animals"
}
```



## MySQL

* One database
* Two tables: 
  * `commodities`: *comm_code*, commodity, category 
  * `trades`: *id*, country_or_area, year, flow, trade_usd, weight_kg, quantity_name, quantity



## Import time

|           MongoDB            | MySQL |
| :--------------------------: | :---: |
| ~3min 30s with `mongoimport` | TODO  |



## Execution time for the selected queries

I imported the dataset and ran the queries 5 times.

Indexes I created:

* on `country_or_area`
* on `commodity` and `comm_code`
* on `year`



#### Computer specs:
- Intel Core i5-6300U (low voltage laptop CPU)
- 8GB RAM DDR4
- 512GB NVMe SSD 


#### 1. Find for each year the country whose Export gain is highest
Indexes \ DB   |            MongoDB          |  MySQL 
---------------|:---------------------------:|:------:
**With Indexes**   | 6.4s, |  TODO  
**Without Indexes**| 7.0s, 6.9s |  TODO  


#### 2. For each year, find the country which traded more kilograms of *10511*
Indexes \ DB   |            MongoDB          |  MySQL 
---------------|:---------------------------:|:------:
**With Indexes**   |   0.02s,   |  TODO  
**Without Indexes**| 3.5s, 3.7s |  TODO  


#### 3. Find the year in which more money was traded across all countries
Indexes \ DB   |            MongoDB          |  MySQL 
---------------|:---------------------------:|:------:
**With Indexes**   |   7.6s,   |  TODO  
**Without Indexes**| 7.6s, 8.8s |  TODO  


#### 4. Find out whether Canada traded more sheeps or goats alive
Indexes \ DB   |            MongoDB          |  MySQL 
---------------|:---------------------------:|:------:
**With Indexes**   |   0.2s   |  TODO  
**Without Indexes**| 3.1s, 4.8s |  TODO  


#### 5. Find all the countries that have not traded 10600 or 10519 in 1998

#### 6. Find the most expensive trade for every year and for each country 

#### 7. Find out whether Italy traded more goats than Canada

#### 8. Find all the categories






