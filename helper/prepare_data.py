
class DataPreparer():
    
    def __init__(self, data):
        self.data = data
        self.filtered_data = self._filter_data()
        self.grouped_data = self._group_data()
        
    def _filter_data(self, parameter='year', value=2021):
        filter_condition = self.data[parameter] == value
        filtered_data = self.data[filter_condition]
        
        return filtered_data
    
    def _group_data(self, group_col='Regional indicator', agg_col='Ladder score', agg_func='mean'):
        grouped_data = self.filtered_data.groupby(group_col).agg(score=(agg_col, agg_func))
        grouped_data.reset_index(inplace=True)
        
        return grouped_data
    
    def create_json(self):
        return self.grouped_data.to_json()
        
