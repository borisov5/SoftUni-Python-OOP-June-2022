from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('John', {
            'Web Programming': ['note1', 'note2'],
            'Database Basics': ['note3', 'note4']
        })

    def test_init_only_with_name(self):
        name = 'John'
        student = Student(name)

        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        name = 'John'
        courses = {
            'Web Programming': ['note1', 'note2'],
            'Database Basics': ['note3', 'note4']
        }

        student = Student(name, courses)

        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_adds_notes_to_the_course(self):
        new_notes = ['new note']
        course = 'Database Basics'

        expected_notes = self.student.courses[course] + new_notes

        result = self.student.enroll(course, ['new note'])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(expected_notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_adds_the_course_with_notes(self):
        course = 'Front-End Basics'
        notes = ['FE1', 'FE2']

        result = self.student.enroll(course, notes, 'Y')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_and_empty_string_adds_the_course_with_notes(self):
        course = 'Front-End Basics'
        notes = ['FE1', 'FE2']

        result = self.student.enroll(course, notes, '')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_adds_the_course_without_notes(self):
        course = 'Front-End Basics'

        result = self.student.enroll(course, ['FE1', 'FE2'], 'N')

        self.assertEqual('Course has been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_adds_notes_to_existing_course(self):
        course = 'Database Basics'
        result = self.student.add_notes(course, 'extra note')

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note3', 'note4', 'extra note'], self.student.courses[course])

    def test_add_notes_raises_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Invalid course', 'random note')
        self.assertEqual('Cannot add notes. Course not found.', str(context.exception))

    def test_leave_course_removes_the_course_from_the_student(self):
        course = 'Database Basics'
        result = self.student.leave_course(course)

        self.assertEqual('Course has been removed', result)
        self.assertTrue(course not in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_raises_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('Invalid course')

        self.assertEqual('Cannot remove course. Course not found.', str(context.exception))


if __name__ == '__main__':
    main()
