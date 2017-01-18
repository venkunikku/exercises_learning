class UnionFindSimple:

    def __init__(self,n):
        self.li = list(range(0,n))
        #print(li[3])
        print(len(self.li))

    def union(self,p,q):
        p_val = self.li[p]
        q_val = self.li[q]
        for i,v in enumerate(self.li[:]):
            if v == p_val:
                self.li[i] = q_val


    def comibned(self,p,q):
        print(p,q,'are  ',self.li[p] == self.li[q], ' Combined')

    def display(self):
        print(self.li)
        for i,v in enumerate(self.li):
            print(i,v)


if __name__ == '__main__':
    uf = UnionFindSimple(10)
    uf.union(4,3)
    uf.union(3,8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    uf.union(8, 9) #

    uf.comibned(8, 9)
    uf.comibned(1, 8)
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.display()