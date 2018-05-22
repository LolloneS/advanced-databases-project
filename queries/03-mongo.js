// 3. Find the year in which more money was traded across all countries

var before = new Date();

printjson(db.countries.aggregate(
    [
        {},
        {},
        {}
    ]
)['_batch'])

execution_mills = (new Date()) - before

print("Seconds the query took: " + (execution_mills / 1000))