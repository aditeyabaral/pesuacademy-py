from pesuacademy.models.course import Course


class CourseResult:
    def __init__(
        self,
        course: Course,
        isa_1: float,
        isa_2: float,
        final_isa: float,
        esa: str,
    ):
        self.course = course
        self.isa_1 = isa_1
        self.isa_2 = isa_2
        self.final_isa = final_isa
        self.esa = esa

    def __str__(self):
        return f"{self.__dict__}"


class SemesterResult:
    def __init__(
        self,
        semester: int,
        esa_description: str,
        credits: int,
        sgpa: float,
        cgpa: float,
        course_results: list[CourseResult],
    ):
        self.semester = semester
        self.esa_description = esa_description
        self.credits = credits
        self.sgpa = sgpa
        self.cgpa = cgpa
        self.course_results = course_results

    def __str__(self):
        return f"{self.__dict__}"
