// 8. Find all the categories
printjson(db.runCommand({distinct : "commodities_ref", key : "category"}))