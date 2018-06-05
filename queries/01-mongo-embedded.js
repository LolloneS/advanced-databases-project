// 1. Find for each year the country whose Export gain is highest

printjson(db.trades.aggregate(
    [
        {
            $match : {
                "trade_details.flow" : "Export"
            }
        },
        {
            $group : {
                "_id" : {
                    country_or_area : "$country_or_area", 
                    year : "$year"
                },
                "total_cash" : {
                    $sum : "$trade_details.trade_usd"
                }
            }
        },
        {
            $sort : {
                "total_cash" : 1
            }
        },
        {
            $group : {
                "_id" : "$_id.year",
                "richest_country_name" : {
                    $last : "$_id.country_or_area"
                },
                "richest_country_cash" : {
                    $last : "$total_cash"
                }
            }
        },
        {
            $project : {
                "_id" : 0,
                "year" : "$_id",
                "richest_country" : {
                    "name" : "$richest_country_name",
                    "cash" : "$richest_country_cash"
                }
            }
        },
        {
            $sort : {
                "year" : 1
            }
        }
    ]
)['_batch'])