import unittest
from delayed_assert import delayed_assert
from .Solution import Solution

class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        return

    def scenario(self, array):
        return


# 4 1 2 5 3 Yes
# 1 2 4 5 3 yes


# 6
# 5
# 4 1 2 5 3 y
# 5
# 1 2 4 5 3 y
# 3
# 2 1 3 n
# 3
# 2 3 1 y
# 3
# 3 1 2 y
# 3
# 3 2 1 n
