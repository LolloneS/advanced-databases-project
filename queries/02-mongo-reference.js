// 2. For each year, find the country which traded more kilograms of *010511*

var before = new Date();

printjson(db.commodities_ref.aggregate(
    [
        {
            $match: {
                "code" : "010511"
            }
        },
        {
            $lookup: {
                from : "trades",
                localField : "code",
                foreignField : "comm_code",
                as : "commodities_trades"
            }
        },
        {
            $project : {
                "_id" : 0,
                "year" : "$commodities_trades.year",
                "country_or_area" : "$commodities_trades.country_or_area",
                "weight_kg" : "$commodities_trades.weight_kgs"
            }
        },
        {
            $group : {
                "_id" : {country_or_area : "$country_or_area", year : "$year"},
                "total_weight" : {$sum : "$weight_kg"}
            }
        },
        {
            $sort : {
                "total_weight" : 1
            }
        },
        {
            $group : {
                "_id" : "$_id.year",
                "most_kgs_country" : {$last : "$_id.country_or_area"},
                "kgs" : {$last : "$total_weight"}
            }
        },
        {
            $project : {
                "_id" : 0,
                "year" : "$_id",
                "most_kilos" : {
                    "country" : "$most_kgs_country",
                    "kilograms" : "$kgs"
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