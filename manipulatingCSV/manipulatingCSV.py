import csv
import cv2


with open('metadata.csv', newline='') as csvIn, open('metadataOut.csv','w+', newline='\n') as csvOut:
    reader = csv.DictReader(csvIn)
    fieldnames = ['id','dob','photo_taken','full_path','gender','name']
    writer = csv.DictWriter(csvOut, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        path=row['full_path']
        sizePath=len(path)
        path=path[2:sizePath-2]
        
        print(path)
        img=cv2.imread(path)
        print(row)
        cv2.imshow("imagem", img)
        key = cv2.waitKey(0)
             
        writer.writerow({'id': row['id'],'dob': row['dob'],'photo_taken': row['photo_taken']
                            ,'full_path':row['full_path'],'gender':key-48,'name': row['name']})

