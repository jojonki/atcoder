class UnionFind:
    def __init__(self, size) -> None:
        self.parent = [-1] * size
        self.size = [1] * size

    def root(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:  # already same group
            return False

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        return True

    def print(self):
        print('----')
        print('parent', self.parent)
        print('size  ', self.size)


if __name__ == "__main__":
    N = 7
    uf = UnionFind(N)
    uf.unite(1, 2)
    uf.print()
    uf.unite(2, 3)
    uf.print()
    uf.unite(5, 6)
    uf.print()
    assert uf.is_same(1, 3) == True
    assert uf.is_same(2, 5) == False
    uf.unite(1, 6)
    uf.print()
    assert uf.is_same(2, 5) == True

    n_graph = 0
    for x in range(N):
        if uf.root(x) == x:  # if x is roote
            n_graph += 1
    print('n_graph:', n_graph)
