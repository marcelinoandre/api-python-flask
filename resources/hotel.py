import uuid

from flask_restful import Resource, reqparse
from models.hotel import HotelModel



hoteis = [
  {
    'id' : f'1f60a438-6a91-4db2-925a-49429ae9ae3f',
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
  argumentos =  reqparse.RequestParser()
  argumentos.add_argument('nome')
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade')

  def find_hotel(self, id) :
    for hotel in hoteis:
      if hotel['id'] == id:
        return hotel
    return None

  def get(self, id):
    hotel = self.find_hotel(id)    

    if hotel:
      return hotel
    
    return {'message' : 'Hotel not found'}, 404


  
  def post(self, id):


    #chaves e valores de todos os argumentos passados
    dados = Hotel.argumentos.parse_args()

    obj_hotel =HotelModel(id= f'{uuid.uuid4()}' , **dados)
    novo_hotel = obj_hotel.json()

    hoteis.append(novo_hotel)
    return novo_hotel, 201


  def put(self, id):
    dados = Hotel.argumentos.parse_args()
    
    hotel = self.find_hotel(id)
    if not hotel:
      return {'message': 'Hotel not found'}

    hotel_update = HotelModel(id  , **dados)
    hotel_update = hotel_update.json()
    hotel.update(hotel_update)

    return hotel_update, 200

  def delete(self, id):
    global hoteis

    hoteis = [hotel for hotel in hoteis if hotel['id'] != id ]

    return {'message': 'Hotel deleted'}


