class WeightedUnionFind:
    def __init__(self, n):
        self.data = [-1 for n in range(n)]
        self.nr_blocks = n

    def weighted_find(self, idx):
        tpl, tpu = 0, 0
        while self.data[idx] > 0:
            idx = self.data[idx]
            tpl += 1
            # print(idx, self.data[idx])
        return idx, tpl, tpu

    def pc_weighted_find(self, idx):
        _, tpl, _ = self.weighted_find(idx)
        tpu = 0
        org_idx = idx
        while self.data[idx] > 0:
            idx = self.data[idx]
        while self.data[org_idx] > 0:
            parent = self.data[org_idx]
            self.data[org_idx] = idx
            org_idx = parent
            tpu += 1
        return idx, tpl, tpu

    def ps_weighted_find(self, idx):
        _, tpl, _ = self.weighted_find(idx)
        tpu = 0
        while self.data[idx] > 0:
            aux_idx = self.data[idx]
            self.data[idx] = self.data[self.data[idx]] if self.data[self.data[idx]] > 0 else self.data[idx]
            idx = aux_idx
            tpu += 1
        return idx, tpl, tpu

    def ph_weighted_find(self, idx):
        _, tpl, _ = self.weighted_find(idx)
        tpu = 0
        while self.data[idx] > 0:
            self.data[idx] = self.data[self.data[idx]] if self.data[self.data[idx]] > 0 else self.data[idx]
            idx = self.data[idx]
            tpu += 1
        return idx, tpl, tpu

    def union_by_weight(self, i, j):
        ri, _, _ = self.weighted_find(i)
        rj, _, _ = self.weighted_find(j)
        # print(ri, rj, self.data[ri], self.data[rj])
        # print(self.data)
        if ri == rj:
            return
        if self.data[ri] >= self.data[rj]:
            self.data[rj] += self.data[ri]
            self.data[ri] = rj

        else:
            self.data[ri] += self.data[rj]
            self.data[rj] = ri

        self.nr_blocks -= 1
