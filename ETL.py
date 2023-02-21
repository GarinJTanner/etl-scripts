## Python ETL: Shake-Shack

target_path = 'C:/Users/a/OneDrive/Tech/ETL/target/Shake-Shack.csv'
output_path = 'C:/Users/a/OneDrive/Tech/ETL/output/Shake-Shack.txt'

def file_len(target_path):
    with open(target_path) as f:
        for i, l in enumerate(f):
            pass
    return enumerate(f,1)
                                                                                                                                                                         
file1 = open(output_path, "w")
toFile = ("insert into locations (latitude,longitude,location) VALUES ")
file1.write(toFile)
file1.close()

len = int(file_len(target_path) [0])
i = 0
While i < file_len(target_path):

	theline = str(linecache.getline(target_path, i))
	latitude = theline.split(",")[0]
	longitude = theline.split(",")[1]
	location = theline.split(",")[2]
	
import linecache
	file2 = open(output_path, "a+")
	toFile2 = "(',latitude,',',longitude,',',location,'),"
	file2.write(toFile2)
	file2.close()

i = i +1

	theline = linecache.getline('C:/Users/a/OneDrive/Tech/ETL/target/Shake-Shack.csv', i)
	latitude = theline.split(",")[0]
	longitude = theline.split(",")[1]
	location = theline.split(",")[2]

	file3 = open(output_path, "a+")
	toFile3 = "(',latitude,',',longitude,',',location,')"
	file3.write(toFile3)
	file3.close()

