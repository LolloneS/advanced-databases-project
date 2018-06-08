// 7. Find out whether Italy traded more goats than Canada

printjson(db.trades.aggregate([
    {
        $match: {
            "commodity.name" : "Goats, live",
            "country_or_area" : {
                $in : ["Canada", "Italy"]
            }
        }
    },
    {
        $group : {
            "_id" : {
                "country_or_area" : "$country_or_area",
            },
            "number_of_sheeps" : {
                $sum : "$trade_details.quantity"
            }
        }
    },
    {
        $project : {
            "_id" : 0,
            "country_or_area" : "$_id.country_or_area",
            "number_of_sheeps" : 1
        }
    }
])['_batch'])