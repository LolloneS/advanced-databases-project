var before = new Date();

var ops = [];
db.trades.aggregate([
    {
        "$project": {
            "commodity_agg": {
                "name": "$commodity", 
                "code": "$comm_code"
            } 
        }
    }
]).forEach(function(doc) {
    ops.push({
        "updateOne": {
            "filter": { "_id": doc._id },
            "update": {
                "$unset": { "comm_code": "", "commodity": "" },
                "$set": { "commodity_agg": doc.commodity }
            }
        }
    });

    if (ops.length === 10000) {
        db.Acc_Details.bulkWrite(ops);
        ops = [];
    }
})

if (ops.length > 0)  db.trades.bulkWrite(ops)

execution_mills = (new Date()) - before

print("Merging the commodities took: " + (execution_mills / 1000))