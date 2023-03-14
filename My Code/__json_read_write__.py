import json

class json_read_write():
    def __init__(self) -> None:
        self.data = None
    
    def read(self, path):
        with open(path) as file:
            return json.load(file)
        
    def write_json(self,path,data):
        with open(path, "w+") as file:
            return file.write(json.dumps(data, indent=2))
    
test = json_read_write()

test.write_json("Data/write_test.json",test.read("Data/sample.json"))
print(test.read("Data/write_test.json"))

