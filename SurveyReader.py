import csv
import pprint

with open('data.csv', 'rb') as csvfile:
    surveyReader = csv.DictReader(csvfile)
    results = []
    for row in surveyReader:
        results.append(row)
        
 


pprint.pprint(results)
