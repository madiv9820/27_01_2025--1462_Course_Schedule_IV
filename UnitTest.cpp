#include <iostream>
#include "Solution.hpp"

struct testcase { int numCourses; vector<vector<int>> prerequisites, queries; vector<bool> output; };

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;

public:
    UnitTest() {
        testcases = {{2, {{1,0}}, {{0,1},{1,0}}, {false,true}},
                     {2, {}, {{1,0},{0,1}}, {true,true}},
                     {3, {{1,2},{1,0},{2,1}}, {{1,0},{1,2}}, {true,true}}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            int numCourses = testcases[i].numCourses;
            vector<vector<int>>& prerequisites = testcases[i].prerequisites;
            vector<vector<int>>& queries = testcases[i].queries;
            vector<bool> output = testcases[i].output;

            vector<bool> result = obj.checkIfPrerequisite(numCourses, prerequisites, queries);
            bool match = true;
            if(output.size() == result.size()) {
                for(int j = 0; j < output.size(); ++j)
                    if(output[j] == result[j]) { match = false; break; }
            }
            else match = false;
            
            cout << (match ? "passed":"failed") << endl;
        }
    }
};