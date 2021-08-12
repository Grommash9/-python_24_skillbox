class StudentClass:

    def __init__(self, name, group, marks):
        self.name = name
        self.group = group
        self.marks = marks
        self.average_score = sum(marks) / len(marks)

    def info(self):
        info = ('ФИ: {name}, группа {group}, оценки {marks}, средний балл {score}'.format(
            name=self.name,
            group=self.group,
            score=self.average_score,
            marks=self.marks
        ))
        return info
