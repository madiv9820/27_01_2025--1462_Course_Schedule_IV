from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: (2, [[1,0]], [[0,1],[1,0]], [False,True]),
                            2: (2, [], [[1,0],[1,0]], [False,False]),
                            3: (3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]], [True,True])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        numCourses, prerequisites, queries, output = self.__testcases[1]
        result = self.__obj.checkIfPrerequisite(numCourses = numCourses, prerequisites = prerequisites, queries = queries)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_2(self):
        numCourses, prerequisites, queries, output = self.__testcases[2]
        result = self.__obj.checkIfPrerequisite(numCourses = numCourses, prerequisites = prerequisites, queries = queries)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_3(self):
        numCourses, prerequisites, queries, output = self.__testcases[3]
        result = self.__obj.checkIfPrerequisite(numCourses = numCourses, prerequisites = prerequisites, queries = queries)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

if __name__ == '__main__': unittest.main()