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

def test_valid_metadata():
    data = {
        "doc_id": 1,
        "filename": "2022-l1-topics-combined-1.pdf",
        "title": "Sample Title",
        "idno": "ABC123",
        "level": "l1",
        "year": 2012
    }
    obj = MetaDataPDF(**data)
    assert obj

def test_valid_metadata_with_optional_fields():
    data = {
        "doc_id": 2,
        "filename": "2023-l2-topics-combined-2.pdf",
        "title": "Sample Title",
        "idno": "XYZ456",
        "level": "l2",
        "year": 2015
    }
    obj = MetaDataPDF(**data)
    assert obj

def test_valid_metadata_with_empty_optional_fields():
    data = {
        "doc_id": 3,
        "filename": "2024-l3-topics-combined-3.pdf",
        "title": "Sample Title",
        "idno": "PQR789",
        "level": "l2",
        "year": 2020,
        "optional_field": None
    }
    obj = MetaDataPDF(**data)
    assert obj

def test_valid_metadata_with_special_characters():
    data = {
        "doc_id": 1,
        "filename": "2022-l1-topics-combined-1.pdf",
        "title": "Sample Title",
        "idno": "ABC_123",
        "level": "l3",
        "year": 2012
    }
    obj = MetaDataPDF(**data)
    assert obj

def test_valid_metadata_with_whitespace():
    data = {
        "doc_id": 2,
        "filename": "2023-l2-topics-combined-2.pdf",
        "title": "  Sample Title  ",
        "idno": "XYZ456",
        "level": "l2",
        "year": 2015
    }
    obj = MetaDataPDF(**data)
    assert obj

# Negative Tests
    
def test_invalid_title_with_special_chars():
    with pytest.raises(ValidationError) as e:
        data = {
            "doc_id": 1,
            "filename": "2022-l1-topics-combined-1.pdf",
            "title": "Sample Title @#$%",
            "idno": "ABC123",
            "level": "l1",
            "year": 2012
        }
        MetaDataPDF(**data)
    
    assert str(e.value) == "1 validation error for MetaDataPDF\ntitle\n  String can only contain alphanumeric characters and spaces [type=value_error.str.alphanumeric]"

def test_invalid_doc_id():
    with pytest.raises(ValidationError) as e:
        data = {
            "doc_id": 4,
            "filename": "2022-l1-topics-combined-1.pdf",
            "title": "Sample Title",
            "idno": "ABC123",
            "level": "l1",
            "year": 2012
        }
        MetaDataPDF(**data)
    
    assert str(e.value) == "1 validation error for MetaDataPDF\ndoc_id\n  Input should be less than 4 [type=less_than, input_value=4, input_type=int]"

def test_invalid_level():
    with pytest.raises(ValidationError) as e:
        data = {
            "doc_id": 1,
            "filename": "2022-l1-topics-combined-1.pdf",
            "title": "Sample Title",
            "idno": "ABC123",
            "level": "Invalid Level",
            "year": 2012
        }
        MetaDataPDF(**data)
    
    assert str(e.value) == "1 validation error for MetaDataPDF\nlevel\n  Value error, Invalid level: must be 'Level I', 'Level II', or 'Level III'. [type=value_error, input_value='Invalid Level', input_type=str]"

def test_invalid_year():
    with pytest.raises(ValidationError) as e:
        data = {
            "doc_id": 1,
            "filename": "2022-l1-topics-combined-1.pdf",
            "title": "Sample Title",
            "idno": "ABC123",
            "level": "l3",
            "year": 2030
        }
        MetaDataPDF(**data)
    
    assert str(e.value) == "1 validation error for MetaDataPDF\nyear\n  Input should be less than 2025 [type=less_than, input_value=2030, input_type=int]"

def test_invalid_filename():
    with pytest.raises(ValidationError) as e:
        data = {
            "doc_id": 1,
            "filename": "invalid-filename.pdf",
            "title": "Sample Title",
            "idno": "ABC123",
            "level": "l3",
            "year": 2012
        }
        MetaDataPDF(**data)
    
    assert str(e.value) == "1 validation error for MetaDataPDF\nfilename\n  String does not match pattern '^\d{4}-l[1-3]-topics-combined-\d\.pdf$' [type=string_pattern_mismatch, input_value='invalid-filename.pdf', input_type=str]"
