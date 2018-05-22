USING PERIODIC COMMIT 1000

LOAD CSV WITH HEADERS FROM "http://0.0.0.0:4748/dataset_minuscolo.csv" AS line
WITH line
WHERE line.quantity IS NOT NULL AND line.quantity_name IS NOT NULL AND line.weight_kg IS NOT NULL
MERGE (c:Country {name : line.country_or_area})
MERGE (p:Commodity {comm_code : line.comm_code, commodity : line.commodity, category : line.category})
MERGE (c) - [r:TRADED {quantity_name : line.quantity_name, quantity : toInteger(line.quantity), weight_kg : toInteger(line.weight_kg), year : toInteger(line.year), flow : line.flow}] -> (p)