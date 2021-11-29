from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from helper.prepare_data import DataPreparer
from helper.persist_data import OutputGenerator
from helper.generate_graph import GraphGenerator

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('https://raw.githubusercontent.com/Akaori/avaliacao_modulo_2/main/data/happiness.csv')

class Happiness(Resource):
    def get(self):
        # prepare data (filter, group)
        prepared_data = DataPreparer(df)
        
        # persist csv and json
        generator = OutputGenerator(prepared_data.grouped_data)
        generator.persist_csv()
        generator.persist_json()
        
        # create graph
        graph = GraphGenerator(prepared_data.filtered_data)
        graph.create_boxplot()
        
        return prepared_data.create_json()

api.add_resource(Happiness, '/happiness')

if __name__ == '__main__':
    app.run(debug=True)
