class School:
    def __init__(self):
        self.students = {}
        self.added_name = []

    def add_student(self, name: str, grade: int):
        for grade_students in self.students.values():
            if name in grade_students:
                self.added_name.append(False)
                return
        if grade not in self.students:
            self.students[grade] = set()
        self.students[grade].add(name)
        self.added_name.append(True)

    def roster(self):
        roster = list()
        for grade in sorted(self.students.keys()):
            students = self.students[grade]
            roster.extend(sorted(list(students)))
        return roster

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, set()))

    def added(self):
        return self.added_name
