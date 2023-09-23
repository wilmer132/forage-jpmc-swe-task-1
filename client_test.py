import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      datapoint = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
      self.assertEqual(getDataPoint(quote), datapoint)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      datapoint = (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2)
      self.assertEqual(getDataPoint(quote), datapoint)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceB_zero(self):
    quotes = [
      {'top_ask': {'price': 5.00, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 3}, 'id': '0.109974697771', 'stock': 'ABC'},
    ]

    for quote in quotes:
      self.assertEqual(getRatio(quote['top_ask']['price'], quote['top_bid']['price']), None)

  def test_getRatio_priceA_zero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 4.00, 'size': 3}, 'id': '0.109974697771', 'stock': 'ABC'},
    ]

    for quote in quotes:
      self.assertEqual(getRatio(quote['top_ask']['price'], quote['top_bid']['price']), float(0))


if __name__ == '__main__':
    unittest.main()
