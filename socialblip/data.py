import os

class Data:
    
    def __init__(self,  data_dir_name):
        self.data_dir_name = data_dir_name
        
    def has_been_inited(self):
        if not os.path.exists(self.data_dir_name) or not os.path.isdir(self.data_dir_name):
            return False
        
        init_file = os.path.join(self.data_dir_name,  'init.txt')
        if not os.path.exists(init_file) or not os.path.isfile(init_file):
           return False
          
        return True
        
    def  init(self,  blipfoto):
        if not os.path.exists(self.data_dir_name) or not os.path.isdir(self.data_dir_name):
            raise Exception("Data dir not there")
        
        entries = blipfoto.get_entries()
        for entry in entries:
            (year, month,  day) = entry['date'].split("-")
            dir = os.path.join(self.data_dir_name,  year,  month,  day)
            os.makedirs(dir)
            with open(os.path.join(dir,  "data.txt"),  "w") as f:
                f.write("INIT")
                
        with open(os.path.join(self.data_dir_name,  "init.txt"),  "w") as f:
            f.write("INITED")
        
    def has_entry(self,  year,  month,  day):
         file = os.path.join(self.data_dir_name,  year,  month,  day,  "data.txt")
         return os.path.exists(file) and os.path.isfile(file)
         
    def create_entry(self,  year,  month,  day):
        dir = os.path.join(self.data_dir_name,  year,  month,  day)
        os.makedirs(dir)
        with open(os.path.join(dir,  "data.txt"),  "w") as f:
            f.write("FOUND")
