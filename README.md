# [1462. Course Schedule IV](https://leetcode.com/problems/course-schedule-iv?envType=daily-question&envId=2025-01-27)

**Type:** Medium <br>
**Topics:** Depth-First Search, Breadth-First Search, Graph, Topological Sort
<hr>

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you **must** take course <code>a<sub>i</sub></code> first if you want to take course <code>b<sub>i</sub></code>.

- For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.

Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

You are also given an array `queries` where <code>queries[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>. For the <code>j<sup>th</sup></code> query, you should answer whether course <code>u<sub>j</sub></code> is a prerequisite of course <code>v<sub>j</sub></code> or not.

Return _a boolean array_ `answer`, _where_ `answer[j]` _is the answer to the_ <code>j<sup>th</sup></code> _query_.
<hr>

- ### Examples
    - **Example 1:**<br>
    ![](https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg)
        ```
        Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
        Output: [false,true]
        Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
        Course 0 is not a prerequisite of course 1, but the opposite is true.
        ```
    - **Example 2:**
        ```
        Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
        Output: [false,false]
        Explanation: There are no prerequisites, and each course is independent.
        ```
    - **Example 3:** <br>
    ![](https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg)
        ```
        Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
        Output: [true,true]
        ```
<hr>

- ### Constraints:
    - `2 <= numCourses <= 100`
    - `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
    - `prerequisites[i].length == 2`
    - <code>0 <= a<sub>i</sub>, b<sub>i</sub> <= numCourses - 1</code>
    - <code>a<sub>i</sub> != b<sub>i</sub></code>
    - All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are **unique**.
    - The prerequisites graph has no cycles.
    - <code>1 <= queries.length <= 10<sup>4</sup></code>
    - <code>0 <= u<sub>i</sub>, <sub>i</sub> <= numCourses - 1</code>
    - <code>u<sub>i</sub> != v<sub>i</sub></code>

- ### Hints
    - Imagine if the courses are nodes of a graph. We need to build an array isReachable[i][j].
    - Start a bfs from each course i and assign for each course j you visit isReachable[i][j] = True.
    - Answer the queries from the isReachable array.