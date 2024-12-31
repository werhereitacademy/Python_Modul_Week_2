# https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    comprehensions_list = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i + j + k) != n :
                    comprehensions_list.append([i,j,k])
    print(comprehensions_list)

"""---------------------------------------------------"""
# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_list= tuple(integer_list)
    print(hash(tuple_list))

"""---------------------------------------------------"""
# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    students_sorted = sorted(students, key=lambda x: x[1])
    min_score = students_sorted[0][1]
    second_score = -1000
    second_score_list = list()
    for i in students_sorted:
        if second_score < min_score < i[1] or min_score < i[1] == second_score:
            second_score_list.append(i)
            second_score = i[1]
    if len(second_score_list) > 0:
        second_score_list_sorted = sorted(second_score_list, key=lambda x: x[0])
        for i in second_score_list_sorted:
            print(i[0])
