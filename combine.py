import csv

count = -1

with open('combined.csv', 'wb') as csvoutputfile:
    csvwriter = csv.writer(csvoutputfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

    with open('sfbusinesses.csv', 'rb') as csvfile:
        sfreader = csv.reader(csvfile, delimiter=',', quotechar='"')


        # "business_id","name","address","city","state","postal_code","latitude","longitude","phone_number"
        for r in sfreader:
            if(r[1] != ""):
                csvwriter.writerow([count]+r+[""])
                count+=1

    #0,id,name,url,phone,address,city,postal_code,latitude,longitude
    with open('yelpbusinesses.csv', 'rb') as csvfile2:
        yreader = csv.reader(csvfile2, delimiter=',', quotechar='"')
        first = False
        for r in yreader:

            csvwriter.writerow([count,"",r[2],r[5],r[6],r[7],"CA",r[8],r[9],r[4],r[3]])
            if(first):
                count+=1
            first = True
