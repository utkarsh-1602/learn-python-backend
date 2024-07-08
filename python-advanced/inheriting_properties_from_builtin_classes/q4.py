from datetime import datetime

class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredDict Created")

    def __getitem__(self, key):
        val = super().__getitem__(key) # it specifically calls the method __getitem__() from the superclass
        self.log_timestamp(f"value for key [{key}] retrieved")
        return val 
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.log_timestamp(f"value for key [{key}]")
    
    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f"{timestampStr} {message}")


inst01 = MonitoredDict()
inst01['a'] = 10
inst01['b'] = 20

print(inst01)
print('Our log book:\n')
print('\n'.join(inst01.log))