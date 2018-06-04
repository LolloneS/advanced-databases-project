// 6. Find the most expensive trade for every year and for each country

/*

var before = new Date();
printjson(db.commodities_ref.aggregate([
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
        $group : {
            "_id" : {
                "country_or_area" : "$commodities_trades.country_or_area",
                "year" : "$commodities_trades.year",
            },
            "max_value" : {
                $max : "$commodities_trades.trade_details.trade_usd",
            }
        }
    },
    {
        $sort : {
            "_id.year" : 1
        }
    }
])['_batch']);
var after = new Date();
print (after-date)
*/
