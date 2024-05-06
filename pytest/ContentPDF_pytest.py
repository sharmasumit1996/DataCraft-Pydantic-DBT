import pytest
from unittest import TestCase
import os
import sys

utils_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(utils_path)

from utils.Model_PDFClass import MetaDataPDF, ContentPDF
from notebooks.PDFParsing.PDFParsing import METADATA_FILES, CONTENT_FILES
from pydantic import ValidationError

class TEIFileTestClass(TestCase):
    def setUp(self):
        xml_folder = os.path.join(os.path.dirname(os.getcwd()), 'xml')
        METADATA_FILES = [os.path.join(xml_folder, f'Grobid_RR_2024_l{i}_combined_metadata.xml') for i in range(1, 4)]
        CONTENT_FILES = [os.path.join(xml_folder, f'2024-l{i}-topics-combined-2.pdf.tei.xml') for i in range(1, 4)]

# Positive Tests

def test_valid_content():
    data = {
        "content_id": 1,
        "doc_id": 1,
        "level": "Level I",
        "year": 2012,
        "topic": "Sample Topic",
        "section_title": "Sample Section Title",
        "paragraph_text": "Sample Paragraph Text"
    }
    obj = ContentPDF(**data)
    assert obj

def test_valid_content_with_optional_fields():
    data = {
        "content_id": 2,
        "doc_id": 2,
        "level": "Level II",
        "year": 2015,
        "topic": "Sample Topic",
    }
    obj = ContentPDF(**data)
    assert obj

def test_valid_content_with_empty_optional_fields():
    data = {
        "content_id": 3,
        "doc_id": 3,
        "level": "Level III",
        "year": 2020,
    }
    obj = ContentPDF(**data)
    assert obj

def test_valid_content_with_whitespace():
    data = {
        "content_id": 4,
        "doc_id": 1,
        "level": "Level I",
        "year": 2012,
        "topic": "  Sample Topic  ",
        "section_title": "  Sample Section Title  ",
        "paragraph_text": "  Sample Paragraph Text  "
    }
    obj = ContentPDF(**data)
    assert obj

def test_valid_content_with_special_characters_in_optional_fields():
    data = {
        "content_id": 5,
        "doc_id": 2,
        "level": "Level II",
        "year": 2015,
        "topic": "Sample@$*#Topic",
    }
    obj = ContentPDF(**data)
    assert obj

# Negative Tests

def test_invalid_content_id():
    with pytest.raises(ValueError, match="Invalid content_id: must be greater than 0."):
        data = {
            "content_id": 0,
            "doc_id": 1,
            "level": "Level I",
            "year": 2012,
            "topic": "Sample Topic",
            "section_title": "Sample Section Title",
            "paragraph_text": "Sample Paragraph Text"
        }
        ContentPDF(**data)

def test_invalid_doc_id():
    with pytest.raises(ValueError, match="Invalid doc_id: must be greater than 0 or less than or equal to 3."):
        data = {
            "content_id": 1,
            "doc_id": 0,
            "level": "Level I",
            "year": 2012,
            "topic": "Sample Topic",
            "section_title": "Sample Section Title",
            "paragraph_text": "Sample Paragraph Text"
        }
        ContentPDF(**data)

def test_invalid_level():
    with pytest.raises(ValueError, match="Invalid level: must be 'Level I', 'Level II', or 'Level III'."):
        data = {
            "content_id": 1,
            "doc_id": 1,
            "level": "Level IV",
            "year": 2024,
            "topic": "Sample Topic",
            "section_title": "Sample Section Title",
            "paragraph_text": "Sample Paragraph Text"
        }
        ContentPDF(**data)

def test_invalid_year():
    with pytest.raises(ValueError, match="Invalid year: must be between 2010 and 2025."):
        data = {
            "content_id": 1,
            "doc_id": 1,
            "level": "Level I",
            "year": 2030,
            "topic": "Sample Topic",
            "section_title": "Sample Section Title",
            "paragraph_text": "Sample Paragraph Text"
        }
        ContentPDF(**data)

def test_invalid_text_with_special_characters():
    with pytest.raises(ValueError, match="Invalid characters in text. Only alphanumeric characters and spaces are allowed."):
        data = {
            "content_id": 1,
            "doc_id": 1,
            "level": "Level I",
            "year": 2012,
            "topic": "Sample Topic",
            "section_title": "Sample Section Title",
            "paragraph_text": "Sample Paragraph @$*# Text"
        }
        ContentPDF(**data)