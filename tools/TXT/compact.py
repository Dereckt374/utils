import os 

path= r"C:\Users\Virgil MESLE\Documents\2-Satellites\DJIBOUTI 1A\TEST\TVAC\LOGsR1U"
os.chdir(path)
print(os.getcwd())
fichiers = os.listdir()

file_result = "result.txt"

with open(file_result,'w') as f :
    for i in fichiers:
        lst = [line.strip() for line in open(i)]
        for j in lst:
            f.write(j+'\n')