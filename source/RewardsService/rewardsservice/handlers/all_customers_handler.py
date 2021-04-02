import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine

# Handles End Point 3
# Returns same rewards data as Endpoint 2 for all customers
class AllCustomersHandler(tornado.web.RequestHandler);

    @coroutine
    def get(self):
      client = MongoClient("mongodb", 27017)
      db = client("Customers")
      allCustomers = list(db.customers.find({}, {"_id": 0}))
      if (len(allCustomers) == 0):
          return self.write("There are no customers...")
      self.write(json.dumps(customers)) 
