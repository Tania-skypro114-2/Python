class Address:
    def __init__(self, ind, gor, ul, dom, kv):
        self.ind = ind
        self.gor = gor
        self.ul = ul
        self.dom = dom
        self.kv = kv

    def __str__(self):
        return f"{self.ind}, {self.gor}, {self.ul}, {self.dom} - {self.kv}"
