courses = [["58", "A"], ["94", "B"], ["17", "A"],["58", "B"],["17", "B"],["58", "C"]]
from collections import defaultdict
def getAllIntersect(input_courses):
    courses = defaultdict(set)

    for student, course in input_courses:
        courses[student].add(course)
    students = list(courses.keys())
    for i in range(0, len(students)):
        for j in range(i + 1, len(students)):
            overlap = list(courses[students[i]] & courses[students[j]])
            tmp = "[{}, {}]:".format(students[i], students[j]) 
            print(tmp, overlap)
#getAllIntersect(courses)

courses = [["A","B"],["C","D"],["B","C"],["E","F"],["D","E"],["F","G"]]

def middle_course(courses):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for src, dst in courses:
        indegree[dst] += 1
        graph[src].append(dst)
    root = None
    for course in graph.keys():
        if indegree[course] == 0:
            root = course
            break
    path = []

    curr = root

    while curr:
        path.append(curr)
        if graph[curr]:
            curr = graph[curr][0]
        else:
            curr = None
    if len(path) % 2 != 0:
        print(path[len(path) // 2])
    else:
        print(path[len(path) // 2 - 1])

middle_course(courses)
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

def find_all_middle_courses(courses):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for src, dst in courses:
        indegree[dst] += 1
        graph[src].append(dst)
    roots = []
    for course in graph.keys():
        if indegree[course] == 0:
            roots.append(course)
    res = set()
    def backtracking(curr, path):
        nonlocal res
        if not curr:
            if len(path) % 2 != 0:
                res.add(path[len(path) // 2])
            else:
                res.add(path[len(path) // 2 - 1])
            print(path)
            return
        path.append(curr)
        if graph[curr]:
            for adj in graph[curr]:
                backtracking(adj, path)
        else:
            backtracking(None, path)
        path.pop()
    for root in roots:
        backtracking(root, [])
    print(list(res))
find_all_middle_courses(all_courses)