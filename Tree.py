class Node(object):
    def __init__(self, left=None, right=None, one=None, value=None):
        self.Left = left
        self.Right = right
        self.One = one
        self.Value = value

    def __repr__(self):
        return 'Left:{}, Right:{}, One:{}, Value:{}'.format(self.Left, self.Right, self.One, self.Value)

