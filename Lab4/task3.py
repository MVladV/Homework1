from abc import abstractmethod, ABC
from jsonschema import validate
import json
import jsonschema

schema = {
    "type": "object",
    "name": {"type": "string"},
    "program": {"type": "list"},
    "type_course": {"type": "string"},
    "teacher": {"type": "string"},
}


class ITeacher(ABC):

    @property
    @abstractmethod
    def name_teacher(self):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass


class ICourseFactory(ABC):

    @abstractmethod
    def create_course(self):
        pass


class ILocalCourse(ABC):

    @abstractmethod
    def study(self):
        pass


class IOffsiteCourse(ABC):

    @abstractmethod
    def study(self):
        pass


class ICourse(ABC):

    @property
    @abstractmethod
    def name_course(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass


class Course(ICourse):

    def __init__(self, name_course, course_program, teacher):
        self.name_course = name_course
        self.course_program = course_program
        self.name_teacher = teacher

    @property
    def name_course(self):
        return self.__name_course

    @name_course.setter
    def name_course(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name_course = name

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, program):
        if not isinstance(program, list):
            raise TypeError
        if not all(isinstance(t, str) for t in program):
            raise ValueError
        self.__course_program = program

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError
        self.__teacher = teacher

    def __str__(self) -> str:
        return f'Course:' \
               f'\n\tName of course - {self.__name_course}' \
               f'\n\tCourse`s program - {self.__course_program}'


class Teacher(ITeacher):

    def __init__(self, name_teacher):
        self.name_teacher = name_teacher
        self.courses = Course("1", ["1"], "1")

    @property
    def name_teacher(self):
        return self.__name_teacher

    @name_teacher.setter
    def name_teacher(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name_teacher = name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        if not isinstance(courses, Course):
            raise TypeError
        # if not all(isinstance(course, Course) for course in courses):
        #     raise ValueError
        self.__courses = courses

    def __str__(self):
        return f'Teacher:' \
               f'\n\tname - {self.__name_teacher}' \
               f'\n\tcourses - {self.__courses}'


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)

    def study(self):
        print("Offsite")

    def __str__(self) -> str:
        return super().__str__()


class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, program, teacher):
        super().__init__(name, program, teacher)

    def study(self):
        print("Local")

    def __str__(self) -> str:
        return super().__str__()


class CourseFactory(ICourseFactory):
    file_courses = []

    def __init__(self):
        self.name = "English course"
        self.program = ['Print', 'Math']
        self.type = "local"
        self.teacher_name = "Oleh"
        self.teacher = Teacher(self.teacher_name)

    def create_course(self):
        if self.type == 'local':
            return LocalCourse(self.name, self.program, self.teacher)
        elif self.type == 'online':
            return OffsiteCourse(self.name, self.program, self.teacher)

    def create_teacher(self, course):
        self.teacher.courses = course
        return self.teacher

    def get_info(self):
        with open("info.json", "r") as read_file:
            courses = json.load(read_file)
        self.file_courses.append(courses)
        for cours in self.file_courses:
            self.name = cours["name"]
            self.program = cours["program"]
            self.type = cours["type_course"]
            self.teacher_name = cours["teacher"]

    def add_cource(self, name, program, type, teacher):  # add to .json file
        my_course = {
            "name": name,
            "program": program,
            "type_course": type,
            "teacher": teacher
        }
        validate(instance={"name": "English course", "program": "['Print', 'List', 'Tuple']", "type_course": "local"},
                 schema=schema)

        with open("info.json", "w") as write_file:
            json.dump(my_course, write_file)
        write_file.close()


if __name__ == '__main__':
    program = ['Print', 'List', 'Tuple']
    factory = CourseFactory()
    factory.add_cource("English course", program, "local", "Vlad")
    factory.get_info()
    course = factory.create_course()
    # course_list = []
    # course_list.append(course)
    teacher1 = factory.create_teacher(course)
    print("Local")
    print(teacher1)
    print(course)

