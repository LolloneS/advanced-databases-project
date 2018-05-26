// 8. Find all the categories
printjson(db.runCommand({distinct : "trades", key : "commodity.category"}))