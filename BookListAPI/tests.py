from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User

# Create your tests here.
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1=User.objects.create_user(username="emma", password="emma123")
        testuser1.save()

        #create Book
        test_book=Book.objects.create(title='first day', subtile='school job', author='jon Don', isbn='Bn3455')
        test_book.save()


    def test_title_content(self):
        book=Book.objects.get(id=1)
        title=f'{book.title}'
        subtile=f'{book.subtile}'
        author=f'{book.author}'
        isbn=f'{book.isbn}'
        self.assertEqual(title, 'first day')
        self.assertEqual(subtile, 'school job')
        self.assertEqual(author, 'jon Don')
        self.assertEqual(isbn, 'Bn3455')

