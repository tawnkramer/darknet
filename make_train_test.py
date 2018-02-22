import os                                                                                   
import sys                                                                                  
import glob                                                                                 
import json                                                                                 
import random                                                                               
                                                                                            
dest = sys.argv[1]                                                                          
                                                                                            
files = glob.glob('**/record_*.json', recursive=True)                                       
print('found %d files.' % len(files))                                                       
                                                                                            
arr = []                                                                                    
                                                                                            
for file in files:                                                                          
        base_path = os.path.join(os.getcwd(), os.path.dirname(file))                        
        with open(file, 'r') as fp:                                                         
                json_data = json.load(fp)                                                   
        image_filename = json_data["cam/image_array"]                                       
        full_filename = os.path.join(base_path, image_filename)                             
        arr.append(full_filename)                                                           
        label_file = full_filename.replace(".jpg", ".txt")                                  
        with open(label_file, "w") as fp:                                                  
                fp.write("%f %f\n" % (json_data['user/angle'], json_data['user/throttle'])) 
                fp.close()                                                                  
                                                                                            
def train_split(factor, arr, train, test):                                                  
        for item in arr:                                                                    
                if random.uniform(0.0, 1.0) < factor:                                       
                        train.append(item)                                                  
                else:                                                                       
                        test.append(item)                                                   
                                                                                            
train = []                                                                                  
test = []                                                                                   
                                                                                            
train_split(0.8, arr, train, test)                                                          
                                                                                            
dest_train_filename = dest + '.train.list'                                                  
with open(dest_train_filename, "w") as fp:                                                 
        for item in train:                                                                  
                fp.write('%s\n' % item)

dest_test_filename = dest + '.test.list'                                                    
with open(dest_test_filename, "w") as fp:                                                  
        for item in test:                                                                   
                fp.write('%s\n' % item) 

