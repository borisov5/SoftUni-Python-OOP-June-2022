from project.library import Library

from unittest import TestCase


class Test(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_library_init(self):
        library_name = 'Library'
        library = Library(library_name)

        self.assertEqual('Library', library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_when_name_is_empty_string(self):
        with self.assertRaises(ValueError) as context:
            library.name = Library('')
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book_when_author_is_not_in_books_by_authors_dict(self):
        author = 'Ivan'
        self.library.add_book(author, [])

        self.assertTrue(author in self.library.books_by_authors.keys())

    def test_add_book_when_title_is_not_in_books_by_authors_dict(self):
        author = 'Ivan'
        title = 'Title'
        self.library.add_book(author, title)

        self.assertTrue(title in self.library.books_by_authors[author])

    def test_add_reader_which_is_not_in_readers_list(self):
        reader = 'Ivelin'
        self.library.add_reader(reader)

        self.assertTrue(reader in self.library.readers.keys())

    def test_add_reader_which_is_already_in_readers_dict(self):
        reader = 'Ivelin'

        self.assertEqual({}, self.library.readers)
        self.library.add_reader(reader)
        self.assertEqual({'Ivelin': []}, self.library.readers)

        result = self.library.add_reader(reader)
        self.assertEqual("Ivelin is already registered in the Library library.", result)

    def test_rent_book_where_reader_name_is_not_in_readers_dict(self):
        reader_name = 'Ivelin'
        book_author = 'Ivan'
        book_title = 'Title'

        self.assertFalse(reader_name in self.library.readers)
        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual("Ivelin is not registered in the Library Library.", result)

    def test_rent_book_when_book_author_is_not_in_books_by_authors_dict(self):
        reader_name = 'Ivelin'
        book_author = 'Ivan'
        book_title = 'Title'

        self.library.add_reader(reader_name)
        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual("Library Library does not have any Ivan's books.", result)

    def test_rent_book_when_book_title_is_not_in_books_by_authors_dict(self):
        reader_name = 'Ivelin'
        book_author = 'Ivan'
        book_title = 'Title'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, [])
        result = self.library.rent_book(reader_name, book_author, book_title)

        self.assertEqual("""Library Library does not have Ivan's "Title".""", result)

    def test_rent_book_when_reader_name_book_author_and_book_title_are_added_to_dictionaries(self):
        reader_name = 'Ivelin'
        book_author = 'Ivan'
        book_title = 'Title'

        self.library.add_book(book_author, book_title)
        self.library.add_reader(reader_name)
        self.assertEqual({'Ivan': ['Title']}, self.library.books_by_authors)
        self.library.rent_book(reader_name, book_author, book_title)

        self.assertTrue(reader_name in self.library.readers.keys())
        self.assertEqual([{'Ivan': 'Title'}], self.library.readers[reader_name])
        self.assertEqual({'Ivan': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
