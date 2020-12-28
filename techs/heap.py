# けんちょん本10章
import math


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] >= x:
                # heap is valid
                break
            # swap parent
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x

    def top(self):
        if len(self.heap) == 0:
            return -1
        return self.heap[0]

    def pop(self):
        if len(self.heap) == 0:
            return

        i = 0
        v = self.heap[-1]
        self.heap[i] = v
        self.heap = self.heap[:-1]
        while 2 * i + 1 < len(self.heap):
            child1, child2 = 2 * i + 1, 2 * i + 2
            if child2 < len(self.heap)  \
                    and self.heap[child2] > self.heap[child1]:
                child1 = child2
            if self.heap[i] < self.heap[child1]:
                self.heap[i] = self.heap[child1]
                i = child1
            else:
                break
        self.heap[i] = v

    def print(self):
        print('heap:', self.heap)
        n_layers = math.ceil(math.log2(len(self.heap) + 1))
        print('n_layers', n_layers)
        for k in range(n_layers):
            layer_vals = []
            for i in range(2**k - 1, 2**(k + 1) - 1):
                if i >= len(self.heap):
                    break
                layer_vals.append(self.heap[i])
            print(f'Layer {k}: {layer_vals}')


if __name__ == "__main__":
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)
    h.print()
    assert h.top() == 7
    h.pop()
    print('after pop')
    h.print()
    assert h.top() == 5
    h.push(11)
    assert h.top() == 11
    print('after pop')
    h.print()
