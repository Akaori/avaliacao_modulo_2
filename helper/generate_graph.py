import seaborn as sns
import matplotlib.pyplot as plt

class GraphGenerator():
    
    def __init__(self, data):
        self.data = data
        
    def create_boxplot(self, output_path='output/graph.jpg', axis_x='Ladder score', axis_y='Regional indicator'):
        figure = plt.figure(figsize=(10, 5))
        
        sns.boxplot(data=self.data, x=axis_x, y=axis_y)

        figure.savefig(output_path)
