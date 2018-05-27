// 5. Find all the countries that have not traded *010600* or *010519* in 1998

var countries_that_traded = (db.trades.aggregate([
    {
        $match : {
            "year" : "1998",
            "commodity.code" : {
                $in : ["010600", "010519"]
            } 
        }
    },
    {
        $group : {
            _id : 0,
            "countries" : {
                $addToSet: "$country_or_area"
            } 
        }
    }
]).toArray())[0].countries


var countries_didnt_trade = (db.trades.aggregate([
    {
        $match : {
            "country_or_area" : {
                $nin : countries_that_traded
            }
        }
    },
    {
        $group : {
            _id : 0,
            "countries" : {
                $addToSet : "$country_or_area"
            }
        }
    }
]).toArray())[0].countries

printjson(countries_didnt_trade)