import itertools
class QuickUionWithWeighted:

    def __init__(self, arraySize):
        self.li = list(range(0,arraySize))
        self.tree_size = list(itertools.repeat(1,arraySize))
        self.counter = arraySize

    def root(self, index):
        while index != self.li[index]:
            index = self.li[index]
        return index

    def union_weighted(self, p, q):
        root_of_p = self.root(p)
        root_of_q = self.root(q)

        if self.tree_size[root_of_p] < self.tree_size[root_of_q]:
            self.li[root_of_p] = root_of_q
            self.tree_size[root_of_q] += self.tree_size[root_of_p]
        else :
            self.li[root_of_q] = root_of_p
            self.tree_size[root_of_p] += self.tree_size[root_of_q]
        self.counter -= self.counter


    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def print_details(self):
        print('list', self.li)
        print('Tree sizes', self.tree_size)
        print('counter', self.counter)

if __name__ == '__main__':
    quick_un_weig = QuickUionWithWeighted(10)
    quick_un_weig.union_weighted(4, 3)
    quick_un_weig.union_weighted(3, 8)
    quick_un_weig.union_weighted(6, 5)

    quick_un_weig.union_weighted(9, 4)
    quick_un_weig.union_weighted(2, 1)
    quick_un_weig.union_weighted(5, 0)
    quick_un_weig.union_weighted(7, 2)
    quick_un_weig.union_weighted(6, 1)
    quick_un_weig.union_weighted(7, 3)
    #quick_un_weig.print_details()
