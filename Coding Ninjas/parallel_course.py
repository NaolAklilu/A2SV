from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    course_pre = defaultdict(list)
    indegree = defaultdict(int)

    for pre, course in prerequisites:
        course_pre[pre].append(course)
        indegree[course] += 1

    queue = deque()
    for course in range(1, n+1):
        if indegree[course] == 0:
            queue.append(course)

    levelCount = 0
    orders = []
    while queue:
        levelCount += 1
        length = len(queue)
        for _ in range(length):
            curCourse = queue.popleft()
            orders.append(curCourse)
            for course in course_pre[curCourse]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

    if len(orders) == n:
        return levelCount

    return -1
