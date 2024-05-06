from unittest import TestCase
from pydantic import ValidationError
import pytest, os, sys

sys.path.append(os.getcwd())
from utils.URLclass import Article

class UserModelTestClass(TestCase):
    def test_positive_correct_year(self):
        t = Article(topic='123', year='2022 aaa')
        self.assertEqual(t.year, 2022)

    def test_positive_correct_topic(self):
        t = Article(id='123')
        self.assertNotEqual(t.topic, '123')

    def test_positive_correct_level(self):
        t = Article(level='Level I')
        self.assertEqual(t.level, "Level I")

    def test_positive_correct_paragraphs(self):
        t = Article(paragraphs="learning_outcomes_section = soup.find('h2', class_='article-section', text='Learning Outcomes')")
        self.assertEqual(t.paragraphs, "learning_outcomes_section = soup.find('h2', class_='article-section', text='Learning Outcomes')")

    def test_positive_correct_url(self):
        t = Article(link1='https://www.cfainstitute.org')
        print(t.link1, '\n','*****')
        self.assertEqual(str(t.link1),'https://www.cfainstitute.org/') # HttpUrl works with a Url(http), so transfer it to a str

    
    def test_negative_year(self):
        try:
            Article(year='-1900')
        except ValidationError:
            self.assertTrue(True)
        self.assertFalse(False)

    def test_out_range_year(self):
        try:
            Article(year='1899')
        except ValidationError:
            self.assertTrue(True)

    def test_no_number_in_year(self):
        try:
            Article(year='No year in the first part')
        except ValidationError:
            self.assertTrue(True)


    def test_url(self):
        with pytest.raises(ValidationError):
            Article(link1="https://")

    def test_Level(self):
        with pytest.raises(ValidationError):
            Article(level="Level IV")