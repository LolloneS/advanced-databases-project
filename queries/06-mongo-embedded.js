// 6. Find the most expensive trade for every year and for each country

printjson(db.trades.aggregate([
    {
        $group : {
            "_id" : {
                "country_or_area" : "$country_or_area",
                "year" : "$year",
            },
            "max_value" : {
                $max : "$trade_details.trade_usd",
            }
        }
    },
    {
        $sort : {
            "_id.year" : 1
        }
    },
    {
        $project : {
            "_id" : 0,
            "country_or_area" : "$_id.country_or_area",
            "year" : "$_id.year",
            "most_expensive_trade_dollars" : "$max_value"
        }
    }
])['_batch'])