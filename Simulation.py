class Simulation(object):
    Times = 50000
    TH = 40
    CSTime = 3
    Success = 0
    Theory_Value = 0

    def __init__(self, Times=None, TH=None, CSTime=None):
        self.Times = Times or self.Times
        self.TH = TH or self.TH
        self.CSTime = CSTime or self.CSTime
        self.Theory_Value = self.theory()

    def __repr__(self):
        return 'Theory Value:{}, Total Times:{}, At Least Rolls:{}, Consecutive Times:{}, Success:{}'.format(self.Theory_Value, self.Times, self.TH, self.CSTime, self.Success)

    @staticmethod
    def roll():
        import random
        return random.randint(1, 6)

    def theory(self):
        from Tree import Node
        def Deeper(N):
            if N.Left is not None:
                N.Left = Deeper(N.Left)
            if N.Right is not None:
                N.Right = Deeper(N.Right)
            if N.Left is None and N.Right is None:
                if N.One is True:
                    N.Left = Node(one=False, value=5 / 36)
                    N.Right = Node(one=True, value=5 / 6)
                else:
                    N.One = True
            return N

        def Calculate(N):
            if N.Left is not None and N.Right is not None:
                if N.Left.Left is not None:
                    N.Left = Calculate(N.Left)
                if N.Right.Right is not None:
                    N.Right = Calculate(N.Right)
                N.Value = N.Value * (N.Left.Value + N.Right.Value)
            return N

        root = Node(one=True, value=5 / 216)
        for each in range(5, self.TH - 1):
            root = Deeper(root)
        root = Calculate(root)
        return round(1 - root.Value, 6)

    def process(self):
        success = 0
        for each in range(0, self.Times):
            count = 0
            last = 0
            n = 0
            while count < self.CSTime and n < self.TH:
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
        return round(success / self.Times, 6)


if __name__ == '__main__':
    s = Simulation()
    print('Probability : ', s.process())
    print(s)
