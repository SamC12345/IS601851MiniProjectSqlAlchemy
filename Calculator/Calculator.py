from Statistics.Statistics import Statistics as statistic

class Calculator:
    result = 0
    stat = statistic()
    def __init__(self):
        pass

    def add(self, a,b):
        self.result = self.stat.add(a,b)
        return self.result

    def subtract(self, a,b):
        self.result = self.stat.subtract(a,b)
        return self.result

    def divide(self, a,b):
        self.result = self.stat.divide(a,b)
        return self.result

    def multiply(self, a,b):
        self.result = self.stat.multiply(a,b)
        return self.result

    def square(self, a):
        self.result = self.stat.square(a)
        return self.result
    
    def squareRoot(self, a):
        self.result = self.stat.squareRoot(a)
        return self.result