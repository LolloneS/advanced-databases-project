// 2. For each year, find the country which traded more kilograms of *010511*


/*
{
   "_id":ObjectId("5b07d0fb0cea1a04a4bfade6"),
   "name":"Sheep, live",
   "code":"010410",
   "category":"01_live_animals",
   "commodities_trades": {
      "_id":ObjectId("5b07cf980cea1a04a442180f"),
      "country_or_area":"Afghanistan",
      "year":"2016",
      "comm_code":"010410",
      "trade_details": {
         "flow":"Export",
         "weight_kg":2339,
         "trade_usd":6088,
         "quantity":51,
         "quantity_name":"Number of items"
      }
   }
}
*/

printjson(db.commodities_ref.aggregate(
    [
        {
            $match: {
                "code" : "010511"
            }
        },
        {
            $project : {
                "_id" : 0,
                "code" : "$code"
            }
        },
        {
            $lookup: {
                from : "trades_ref",
                localField : "code",
                foreignField : "comm_code",
                as : "commodities_trades"
            }
        },
        {
            $unwind : "$commodities_trades"
        },
        {
            $project : {
                "_id" : 0,
                "year" : "$commodities_trades.year",
                "country_or_area" : "$commodities_trades.country_or_area",
                "weight_kg" : "$commodities_trades.trade_details.weight_kg"
            }
        },
        {
            $group : {
                "_id" : {
                    country_or_area : "$country_or_area", 
                    year : "$year"
                },
                "total_weight" : {
                    $sum : "$weight_kg"
                }
            }
        },
        {
            $group : {
                "_id" : "$_id.year",
                "most_kgs_country" : {
                    $last : "$_id.country_or_area"
                },
                "kgs" : {
                    $max : "$total_weight"
                }
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
