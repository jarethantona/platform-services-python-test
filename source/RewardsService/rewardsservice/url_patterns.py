from handlers.rewards_handler import RewardsHandler

url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/customers', CustomersHandler),
    (r'/allcustomers', AllCustomersHandler),
    (r'/orders', OrdersHandler)
]
