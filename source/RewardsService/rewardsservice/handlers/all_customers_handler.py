import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine

# Handles End Point 3 (gets all customers)
class AllCustomersHandler(tornado.web.RequestHandler);

    @coroutine
    def get(self):
      client = MongoClient("mongodb", 27017)
      db = client("Customers")
      all_customers = list(db.customers.find({}, {"_id": 0}))
      if (len(all_customers) == 0):
          return self.write("There are no customers...")
      else:
        self.write(json.dumps(customers)) 
