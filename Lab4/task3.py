from abc import abstractmethod, ABC


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
    def create_course(self, name: str, course_program: list, course_type: str, teacher: ITeacher):
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
        self.teacher = teacher

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
               f'\n\tTeacher - {self.__teacher.name_teacher}' \
               f'\n\tCourse`s program - {self.__course_program}'


class Teacher(ITeacher):

    def __init__(self, name_teacher):
        self.name_teacher = name_teacher
        self.courses = []

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
        if not isinstance(courses, list):
            raise TypeError
        if not all(isinstance(course, Course) for course in courses):
            raise ValueError
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

    def create_course(self, name, course_program, course_type, teacher):
        if course_type == 'local':
            return LocalCourse(name, course_program, teacher)
        elif course_type == 'online':
            return OffsiteCourse(name, course_program, teacher)

    def create_teacher(self, teacher, courses):
        teacher.courses = courses
        return teacher


if __name__ == '__main__':
    teacher1 = Teacher('Vladislav')
    factory = CourseFactory()
    program = ['Print', 'List', 'Tuple']
    course = factory.create_course('English course', program, 'local', teacher1)
    course_list = [course]
    teacher1 = factory.create_teacher(teacher1, course_list)
    course.study()
    print(teacher1)
    print(course)
