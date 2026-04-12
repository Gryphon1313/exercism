class Garden:
    plant_mapping = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    def __init__(self, diagram: str, students: list[str] = None):
        self.diagram = diagram
        self.students = students or [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
            'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]
        self.students.sort()
    
    def plants(self, student: str) -> list[str]:
        index = self.students.index(student)
        rows = self.diagram.splitlines()
        return [self.plant_mapping[rows[row][index * 2:(index + 1) * 2][i]] for row in range(2) for i in range(2)]
    

