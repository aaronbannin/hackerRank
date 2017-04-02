class SpecialNumber(object):
    def __init__(self, base10):
        self.base10 = base10
        self.base2 = ""

        self._divide_by_two(self.base10)
        self.repeating_ones = self._calculate_repeating_ones()

    def _divide_by_two(self, integer):
        if integer == 0:
            self.base2 = 0
        else:
            self.base2 = str(integer % 2) + self.base2
            if integer / 2 != 0.5:
                self._divide_by_two(int(integer / 2))

    def _calculate_repeating_ones(self):
        if self.base2 == "":
            return 0
        elif self.base2 == 0:
            return 0
        elif "0" not in self.base2:
            return len(self.base2)

        # local vars
        max_repeats = 0
        current_repeats = 0

        for char in self.base2:
            if int(char) == 0:
                if current_repeats > max_repeats:
                    max_repeats = current_repeats
                current_repeats = 0
            elif int(char) == 1:
                current_repeats += 1

        if current_repeats > max_repeats:
            return current_repeats
        else:
            return max_repeats

    @classmethod
    def main(cls, integer):
        obj = cls(integer)
        # print(obj.repeating_ones)
        print(obj.__dict__)

for n in range(0,100):
    SpecialNumber.main(n)

# SpecialNumber.main(5)
# SpecialNumber.main(6)
# SpecialNumber.main(13)
# SpecialNumber.main(25)
# SpecialNumber.main(0)
# SpecialNumber.main(1)
