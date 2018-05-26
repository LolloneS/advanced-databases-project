// 7. Find out whether Italy traded more goats than Canada

printjson(db.commodities_ref.aggregate([
    {
        $match: {
            "name" : "Goats, live"
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
            "commodities_trades.country_or_area" : {
                $in : ["Canada", "Italy"]
            }
        }
    },
    {
        $group : {
            "_id" : {
                "country_or_area" : "$commodities_trades.country_or_area",
            },
            "number_of_sheeps" : {
                $sum : "$commodities_trades.trade_details.quantity"
            }
        }
    }
])['_batch'])