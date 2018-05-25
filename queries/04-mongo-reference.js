// 4. Find out whether Canada traded more "Sheep, live" or "Goats, live"


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
            $match : {
                "name" : {$in : ["Sheep, live", "Goats, live"]}
            }
        },
        {
            $lookup : {
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
            $match : {
                "commodities_trades.country_or_area" : "Canada"
            }
        },
        {
            $project : {
                "_id" : 0,
                "name" : "$name",
                "quantity" : "$commodities_trades.trade_details.quantity"
            }
        },
        {
            $group: {
                "_id" : "$name",
                "quantity" : {
                    "$sum" : "$quantity"
                }
            }
        }
    ]
)['_batch'])
