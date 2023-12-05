
import os

os.chdir(r" ") #Put the folder path here

d_list = (os.listdir())

j = 0

for file in d_list:
    if ' [1]' in file:
        x = file.split(' [1]')[0]    
        x2 = str(x)+".wav"        
        print(x2)
        os.rename(file, x2)
        print(file)    


#Change the parameters according to your needs. For example, in this case the file name is split at ' [1]' and then renamed accordingly to a .wav file

