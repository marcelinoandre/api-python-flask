from flask_restful import Resource

hoteis = [
  {
    'id' : '123456a',
    'nome' : 'Alpha Hotel',
    'estrelas' : 4.3,
    'diaria' : 420.34,
    'cidade' : 'SP'
  },
  
  {
    'id' : '123456b',
    'nome' : 'Confort',
    'estrelas' : 4.5,
    'diaria' : 420.34,
    'cidade' : 'RJ'
  },
  {
    'id' : '123456c',
    'nome' : 'Blue Tree',
    'estrelas' : 4.3,
    'diaria' : 420.34,
    'cidade' : 'MG'
  },
  {
    'id' : 'Plaza Sul',
    'nome' : 'Alpha Hotel',
    'estrelas' : 3.3,
    'diaria' : 220.34,
    'cidade' : 'SP'
  },

]

class Hoteis(Resource):
  def get(self):
    return {'hoteis' : hoteis}

class Hotel(Resource) :
  def get(self, id):
    for hotel in hoteis:
      if hotel['id'] == id:
        return hotel
    
    return {'message' : 'Hotel not found'}, 404
  
  def post(self, id):
    pass

  def put(self, id):
    pass

  def delete(self, id):
    pass


