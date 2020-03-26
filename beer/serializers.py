from builtins import object

class BeerSerializer(object):
    def __init__(self, body):
        self.body = body
    
    @property
    def all_beers(self):
        output = {'beers': []}

        for beer in self.body:
            beer_details = {
                'beer_name': beer.beer_name,
                'brewery': beer.brewery,
                'abv': beer.abv
            }
            output['beers'].append(beer_details)

        return output
    
    @property
    def beer_detail(self):
        return {
            'beer_name': self.body.beer_name,
            'brewery': self.body.brewery,
            'abv': self.body.abv
        }