import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine

class OrdersHandler(tornado.web.RequestHandler):

  @coroutine
  def post(self, keys):
    client = MongoClient("mongodb", 27017)
    customersdb = client["Customer"]
    
    email = self.__getattribute__("email", "")
    order_total = self.__getattribute__("order_total", "")

    reward_tier = self.reward_tier(order_total)
    reward_tier_name = self.reward_tier_name(reward_tier)

    next_reward_tier = self.next_reward_tier_name(reward_tier_name)
    next_reward_tier_name = self.next_reward_tier_name(next_reward_tier)
    next_reward_points = self.next_reward_points(next_reward_tier)

    points = int(float(order_total))

    if (next_reward_points == "N/A"):
      progress = "N/A"
    progress - round(float(orderTotal) / next_reward_points, 2)
    customerData = {"Email Address": email, "Reward Points": points, "Reward Tier": reward_tier, 
    "Reward Tier Name": reward_tier_name, "Next Reward Tier": next_reward_tier, 
    "Next Reward Tier Name": next_reward_tier_name, "Next Reward Tier Progress": progress}
    db.customers.insert(customerData)

  def reward_tier(self, total_spent):
    if total_spent >= 1000:
      return "J"
    elif total_spent >= 900 and total_spent < 1000:
      return "I"
    elif total_spent >= 800 and total_spent < 900:
      return "H"
    elif total_spent >= 700 and total_spent < 800:
      return "G"
    elif total_spent >= 600 and total_spent < 700:
      return "F"
    elif total_spent >= 500 and total_spent < 600:
      return "E"
    elif total_spent >= 400 and total_spent < 500:
      return "D"
    elif total_spent >= 300 and total_spent < 400:
      return "C"
    elif total_spent >= 200 and total_spent < 300:
      return "B"
    elif total_spent >= 100 and total_spent < 200:
      return "A"
    elif total_spent < 100:
      return ""
    
  def next_reward_tier(self, total_spent):
     if total_spent >= 1000:
      return "J"
    elif total_spent >= 900 and total_spent < 1000:
      return "J"
    elif total_spent >= 800 and total_spent < 900:
      return "I"
    elif total_spent >= 700 and total_spent < 800:
      return "H"
    elif total_spent >= 600 and total_spent < 700:
      return "G"
    elif total_spent >= 500 and total_spent < 600:
      return "F"
    elif total_spent >= 400 and total_spent < 500:
      return "E"
    elif total_spent >= 300 and total_spent < 400:
      return "D"
    elif total_spent >= 200 and total_spent < 300:
      return "C"
    elif total_spent >= 100 and total_spent < 200:
      return "B"
    elif total_spent < 100:
      return "A"

  def next_reward_tier_name(self, next_reward_tier)
    if (next_reward_tier == "N/A"):
      return "N/A"
    for map in maps:
      if (map["tier"] == next_reward_tier):
        return map["reward_name"]

  def next_reward_points(self, next_reward_tier):
    if(next_reward_tier == "N/A"):
      return "N/A"
    for map in maps:
      if (map["tier"] == next_reward_tier):
        return map["points"]

  
