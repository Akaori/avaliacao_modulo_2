from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('data/happiness.csv')

class Happiness(Resource):
    def get(self):
        happiness_year = df['year'] == 2021
        filtered_df = df[happiness_year]
        
        grouped_df = filtered_df.groupby('Regional indicator').agg(score=('Ladder score', 'mean'))
        grouped_df.reset_index(inplace=True)
        
        grouped_df.to_csv('output/grouped.csv', index=False)
        grouped_df.to_json('output/grouped.json')
        
        figure = plt.figure(figsize=(10, 5))

        sns.boxplot(data=filtered_df, x='Ladder score', y='Regional indicator')

        figure.savefig('output/grafico.jpg')
        
        return grouped_df.to_json()

api.add_resource(Happiness, '/happiness')

if __name__ == '__main__':
    app.run(debug=True)
