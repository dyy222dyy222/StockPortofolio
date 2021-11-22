class Portfolio:
    def __init__(self):
        self._stocks = []

    def buy(self, name, shares, price):
        self._stocks.append((name, shares, price))

    def cost(self):
        cost = 0
        for stock in self._stocks:
            cost += stock[1] * stock[2]
        return cost