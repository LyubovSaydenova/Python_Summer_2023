class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
class Professor:
    def __init__(self):
        self.work = 0
    def check(self, info, *student):
        for i in student:
            i.resolve(info)
            self.work += 1
class Student:
    def __init__(self):
        self.solution = []
    def resolve(self, info):
        self.solution.append(info)
task = Data('task completed', 'task failed')
professor = Professor()
student1 = Student()
student2 = Student()
professor.check(task[0], student1)
professor.check(task[1], student2)
print("Student1 =", student1.solution)
print("Student2 =", student2.solution)