from collections import deque
from functools import reduce

class PseudoRng(object):
    def __init__(self, initial_secret):
        self.initial_secret = initial_secret
        self.secret = self.initial_secret

        self.prices = dict()
        self.diffs = deque(maxlen=4)

    def _reset(self):
        self.secret = self.initial_secret

    def _run_iter(self):

        init_price = self.price

        self.secret ^= (self.secret * 64)
        self.secret %= 16777216

        self.secret ^= (self.secret // 32)
        self.secret %= 16777216

        self.secret ^= (self.secret * 2048)
        self.secret %= 16777216

        final_price = self.price

        diff = final_price - init_price

        self.diffs.append(diff)

        if len(self.diffs) == 4:
            key = (self.diffs[0], self.diffs[1], self.diffs[2], self.diffs[3])

            if key not in self.prices:
                self.prices[key] = final_price



    def nth_secret(self, nth):
        for _ in range(nth):
            self._run_iter()

        return self.secret

    @property
    def price(self):
        return self.secret % 10

def main():

    data = None
    with open('../data/day_22/sample_data.txt', 'r') as fp:
        data = fp.readlines()
        data = map(lambda x: int(x.strip()), data)
        data = list(data)

    total = 0
    rngs = []
    for entry in data:
        rng = PseudoRng(entry)
        rngs.append(rng)
        result = rng.nth_secret(2000)
        total += result


    print(total)
    only_keys = map(lambda x: x.prices.keys(), rngs)
    final_keys = reduce(lambda x,y: x | y, only_keys)
    print('Calculated keys')

    total_max = 0
    max_key = None
    for key in final_keys:
        cur_max = 0

        for rng in rngs:
            cur_max += rng.prices.get(key, 0)

        
        if cur_max > total_max:
            total_max = cur_max
            max_key = key

    print(total_max, max_key)

if __name__ == '__main__':
    main()