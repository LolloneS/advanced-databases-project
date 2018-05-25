// 4. Find out whether Canada traded more "Sheep, live" or "Goats, live"

printjson(db.trades.aggregate(
    [
        {
            $match : {
                "country_or_area" : "Canada",
                "commodity.name" : {$in : ["Sheep, live", "Goats, live"]}
            }
        },
        {
            $project : {
                "_id" : 0,
                "name" : "$commodity.name",
                "quantity" : "$trade_details.quantity"
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
