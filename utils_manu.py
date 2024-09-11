from copy import copy

class indexed_set(object):
    def __init__(self, arg=None):
        if arg is None:
            self.table = []
            self.dict = dict()
        elif type(arg) == list:
            self.table = copy(arg)
            self.dict = { v:i for i,v in enumerate(self.table) }
        elif type(arg) == set:
            self.table = list(arg)
            self.dict = { v:i for i,v in enumerate(self.table) }
        else:
            raise TypeError('cannot deal with this type')
    def add(self, v):
        try:
            return self.dict[v]
        except KeyError:
            pass
        k = len(self.table)
        self.dict[v] = k
        self.table.append(v)
        return k
    def index(self, v):
        return self.dict[v]
    def __getitem__(self, i):
        return self.table[i]
    def __len__(self):
        return len(self.table)
    def sort(self, *args, **kwargs):
        self.table.sort(*args, **kwargs)
        self.dict = { v:i for i,v in enumerate(self.table) }
