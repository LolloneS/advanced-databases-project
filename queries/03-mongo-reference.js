// 3. Find the year in which more money was traded across all countries

printjson(db.trades_ref.aggregate(
    [
        { 
            $group : {
                "_id" : {
                        year : "$year"
                },
                "money_aggregated" : {
                    $sum : "$trade_details.trade_usd"
                }
            }
        },
        {
            $group : {
                "_id" : {year : "$_id.year"},
                "money_traded" : {$max : "$money_aggregated"} 
            }
        },
        {
            $sort : {
                "max_money" : -1
            }
        },
        {
            $limit : 1
        }
    ]
)['_batch'])