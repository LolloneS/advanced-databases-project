# Advanced Databases 2CFU Project
# Global Commodity Trade Statistics 

Dataset: [Global Commodity Trade Statistics](https://www.kaggle.com/unitednations/global-commodity-trade-statistics) by [United Nations](https://www.kaggle.com/unitednations)


## Abstract
Comparison between the performances of MongoDB with and without indexes whilst working with a huge dataset representing trades statistics for many countries.

## MongoDB structure
* One database
* One collection

Document structure (example):
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

## Queries (?)
#### 1. Find for each year the country whose Export gain is highest

#### 2. For each year, find the country which traded more kilograms of *010511*

#### 3. Find the year in which more money was traded across all countries

#### 4. Find the most expensive trade for every year and for each country 

#### 5. Find out whether Italy traded 010600

#### 6. Find all the countries that have not traded 010600 or 010519 in 1998

#### 7. Find out whether Albania traded more "Sheep, live" or "Goat, live"



