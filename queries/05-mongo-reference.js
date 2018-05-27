// 5. Find all the countries that have not traded *010600* or *010519* in 1998

// 5. Find all the countries that have not traded *010600* or *010519* in 1998

var countries_that_traded = (db.commodities_ref.aggregate([
    {
        $match : {
            "code" : {
                $in : ["010600", "010519"]
            } 
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
            "commodities_trades.year" : "1998"
        }
    },
    {
        $group : {
            _id : 0,
            "countries" : {
                $addToSet: "$commodities_trades.country_or_area"
            } 
        }
    }
]).toArray())[0].countries


var countries_didnt_trade = (db.trades_ref.aggregate([
    {
        $match : {
            "country_or_area" : {
                $nin : countries_that_traded
            }
        }
    },
    {
        $group : {
            _id : 0,
            "countries" : {
                $addToSet : "$country_or_area"
            }
        }
    }
]).toArray())[0].countries

printjson(countries_didnt_trade)