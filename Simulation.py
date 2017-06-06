class Simulation(object):
    Times = 10000
    TH = 50
    CSTime = 3
    Success = 0

    def __init__(self, Times=None, TH=None, CSTime=None):
        self.Times = Times or self.Times
        self.TH = TH or self.TH
        self.CSTime = CSTime or self.CSTime

    def __repr__(self):
        return 'Total Times:{}, At Least Rolls:{}, Consecutive Times:{}, Success:{}'.format(self.Times, self.TH, self.CSTime, self.Success)

    @staticmethod
    def roll():
        import random
        return random.randint(1, 6)

    def process(self):
        success = 0
        for each in range(0, self.Times):
            count = 0
            last = 0
            n = 0
            while count < self.CSTime:
                n = n + 1
                num = self.roll()
                if last != num:
                    last = num
                    count = 0
                else:
                    count = count + 1
            if n >= self.TH:
                success = success + 1
        self.Success = success
        return success / self.Times

if __name__ == '__main__':
    s = Simulation()
    print('Probability : ', s.process())
    print(s)
