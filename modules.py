class ParsingImplementation:
    def __init__(self, buy, sell, location, amount):
        self.buy = buy
        self.sell = sell
        self.location = location
        self.amount = amount
    
    def print_request(self):
        print(f" You buy '{self.buy}' for '{self.sell}' in "
              f"'{self.location}' in the amount of: {self.amount}, all right?")


template = ParsingImplementation('USD', 'USDT', 'Batumi', 100)

print(template.print_request())
