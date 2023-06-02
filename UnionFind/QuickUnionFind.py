class QuickUnionFind:
    def __init__(self, n):
        self.data = [i for i in range(n)]
        self.nr_blocks = n

    def quick_find(self, idx):
        tpl, tpu = 0, 0
        while self.data[idx] != idx:
            idx = self.data[idx]
            tpl += 1  # Increase TPL for each iteration
        return idx, tpl, tpu

    def pc_find(self, idx):
        _, tpl, _ = self.quick_find(idx)
        tpu = 0
        org_idx = idx
        while self.data[idx] != idx:
            idx = self.data[idx]
        while self.data[org_idx] != org_idx:  # Iterate a second time and set all elements on the path to previously found representative
            org_idx = self.data[org_idx]
            self.data[org_idx] = idx
            tpu += 1
        return idx, tpl, tpu

    def ps_find(self, idx):
        _, tpl, _ = self.quick_find(idx)
        tpu = 0
        while self.data[idx] != idx:
            aux_idx = self.data[idx]
            self.data[idx] = self.data[self.data[idx]]
            idx = aux_idx
            tpu += 1
        return idx, tpl, tpu

    def ph_find(self, idx):
        _, tpl, _ = self.quick_find(idx)
        tpu = 0
        while self.data[idx] != idx:
            self.data[idx] = self.data[self.data[idx]]
            idx = self.data[idx]
            tpu += 1
        return idx, tpl, tpu

    def quick_union(self, i, j):
        ri, _, _ = self.quick_find(i)
        rj, _, _ = self.quick_find(j)
        if ri != rj:
            self.data[ri] = rj
            self.nr_blocks -= 1

    def quick_pc_union(self, i, j):
        ri, _, _ = self.pc_find(i)
        rj, _, _ = self.pc_find(j)
        if ri != rj:
            self.data[ri] = rj
            self.nr_blocks -= 1

    def quick_ps_union(self, i, j):
        ri, _, _ = self.ps_find(i)
        rj, _, _ = self.ps_find(j)
        if ri != rj:
            self.data[ri] = rj
            self.nr_blocks -= 1

    def quick_ph_union(self, i, j):
        ri, _, _ = self.ph_find(i)
        rj, _, _ = self.ph_find(j)
        if ri != rj:
            self.data[ri] = rj
            self.nr_blocks -= 1


if __name__ == '__main__':
    f = QuickUnionFind(100)
    f.quick_union(4, 5)
    f.quick_union(6, 5)
    f.quick_union(5, 3)
    f.quick_union(7, 5)
    f.quick_union(9, 5)
    f.quick_union(5, 12)
    print(f.data)

    print(f.ps_find(4))
    print(f.data)
    print(f.nr_blocks)
