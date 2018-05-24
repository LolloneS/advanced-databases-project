// 4. Find out whether Canada traded more "Sheep, live" or "Goats, live"

var before = new Date();


printjson(db.trades.aggregate(
    [
        {
            $match : {
                "country_or_area" : "Canada",
                "commodity.name" : {$in : ["Sheep, live", "Goats, live"]}
            }
        },
        {
            $group: {
                "_id" : "$country_or_area",
                "sheeps" : {
                    "$sum" : {
                        "$cond" : [
                            {
                                "$eq" : ["$commodity.name", "Sheep, live"]
                            },
                            "$trade_details.quantity",
                            0
                        ]
                    }
                },
                "goats" : {
                    "$sum" : {
                        "$cond" : [
                            {
                                "$eq" : ["$commodity.name", "Goats, live"]
                            },
                            "$trade_details.quantity",
                            0
                        ]
                    }
                },
                
            }
        } 
    ]
)['_batch'])


execution_mills = (new Date()) - before

print("Seconds the query took: " + (execution_mills / 1000))