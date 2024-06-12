# 此列表存储所有学生信息
docs = []


class Student:
    def __init__(self, name, age, class_1, score):
        self.name = name
        self.age = age
        self.class_1 = class_1
        self.score = score


def input_student():
    """输入学生信息"""
    lst = []  # 用于存储学生信息
    while True:
        n = input("请输入学生姓名：")
        if not n:
            break
        a = input("请输入学生年龄：")
        c = input("请输入学生班级：")
        s = input("请输入学生成绩：")
        """d = {
            'name': n,
            'age': a,
            'class': c,
            'score': s
        }  # 存储一位学生信息"""
        lst.append(Student(n, a, c, s))
    return lst


def output_student(lst):
    print('-' * 44)
    print('|' + 'name'.center(8) + '|' + 'age'.center(7) + '|' + 'class'.center(15) + '|' + 'score'.center(9) + '|')
    print('-' * 44)
    for stu in lst:
        print("| %-s | %-s | %-s | %-s |" % (stu.name.center(6),
                                             stu.age.center(5),
                                             stu.class_1.center(13),
                                             stu.score.center(7)))
    print('-' * 44)


def add_student():
    """添加学生信息"""
    global docs
    docs += input_student()


def show_all_student():
    """显示所有学生信息"""
    output_student(docs)


def show_order_by_score_desc():
    """按学生成绩高-低显示学生信息"""
    new_docs = sorted(docs,
                      key=lambda stu: stu['score'],
                      reverse=True)
    output_student(new_docs)


def show_order_by_score_asc():
    """按学生成绩高-低显示学生信息"""
    new_docs = sorted(docs,
                      key=lambda stu: stu['score'])
    output_student(new_docs)


def show_order_by_age_desc():
    """按学生年龄高-低显示学生信息"""
    new_docs = sorted(docs,
                      key=lambda stu: stu['age'],
                      reverse=True)
    output_student(new_docs)


def show_order_by_age_asc():
    """按学生年龄高-低显示学生信息"""
    new_docs = sorted(docs,
                      key=lambda stu: stu['age'])
    output_student(new_docs)
