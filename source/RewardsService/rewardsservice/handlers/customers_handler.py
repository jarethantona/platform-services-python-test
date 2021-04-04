import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine


class CustomersHandler(tornado.web.RequestHandler);

    @coroutine
    def get(self):
      client = MongoClient("mongodb", 27017)
      db = client("Customers")
      email = self.get_argument("email", "")
      self.write(email)
      customer_data = db.customers.find_one{{"Email Address": email}}

      if (not customer_data):
        return self.write("This must be an invalid input.")
      self.write({"Customer Data": customer_data})
