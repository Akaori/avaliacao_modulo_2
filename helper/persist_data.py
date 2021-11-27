

class OutputGenerator():
    
    def __init__(self, data):
        self.data = data
    
    def persist_csv(self, output_path='output/data.csv'):
        self.data.to_csv(output_path, index=False)
        
    def persist_json(self, output_path='output/data.json'):
        self.data.to_json(output_path)
