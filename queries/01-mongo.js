// 1. Find for each year the country whose Export gain is highest

var before = new Date();

printjson(db.countries.aggregate(
    [
        {
            $match : {
                "flow" : "Export"
            }
        },
        {
            $group : {
                "_id" : {country_or_area : "$country_or_area", year : "$year"},
                "total_cash" : {$sum : "$trade_usd"}
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
                "richest_country_name" : {$last : "$_id.country_or_area"},
                "richest_country_cash" : {$last : "$total_cash"}
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

execution_mills = (new Date()) - before

print("Seconds the query took: " + (execution_mills / 1000))