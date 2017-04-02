input_str = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""

new = """-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5"""

# array_values = []
# for line in input_str.split('\n'):
#     array_values.append(line.split(' '))



class HourglassSum(object):
    def __init__(self, input_str):
        self.array_values = []
        self.max_sum = -999
        for line in input_str.split('\n'):
            self.array_values.append([int(x) for x in line.split(' ')])

    def extract_and_sum(self, row_index, column_index):
        left_index = column_index - 1
        right_index = column_index + 2
        top = self.array_values[row_index - 1][left_index:right_index]
        middle = [self.array_values[row_index][column_index]]
        bottom = self.array_values[row_index + 1][left_index:right_index]
        values = top + middle + bottom
        return sum(values)


    def main(self):
        # row_index = 1
        for row_index in range(1, len(self.array_values) - 1):
            for column_index in range(1, len(self.array_values[0]) - 1):
                result = self.extract_and_sum(row_index, column_index)
                if result > self.max_sum:
                    self.max_sum = result

        print(self.max_sum)

obj = HourglassSum(new)
obj.main()
