var before = new Date()

db.countries.aggregate(
    [
        {
            $match : {
                "comm_code" : 10511,
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
)

execution_mills = (new Date()) - before
