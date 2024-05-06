from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
import re

class MetaDataPDF(BaseModel):
    doc_id: int = Field(gt=0, lt=4)
    filename: str = Field(pattern=r'^\d{4}-l[1-3]-topics-combined-\d\.pdf$')
    title: str
    idno: str
    level: str
    year: int = Field(gt=2010, lt=2025)
   
    class Config:
        from_attributes = True

    @validator('doc_id')
    @classmethod
    def validate_doc_id(cls, value):
        if value not in [1, 2, 3]:
            raise ValueError("Invalid doc_id: must be 1, 2, or 3.")
        return value

    @validator('level')
    @classmethod
    def validate_level(cls, value):
        if value not in ['l1', 'l2', 'l3']:
            raise ValueError("Invalid level: must be 'Level I', 'Level II', or 'Level III'.")
        return value

    @validator('year')
    @classmethod
    def validate_year(cls, value):
        if not (2010 <= value <= 2025):
            raise ValueError("Invalid year: must be between 2010 and 2025.")
        return value

    @validator('filename')
    @classmethod
    def validate_filename(cls, value):
        if not re.match(r'^\d{4}-l[1-3]-topics-combined-\d\.pdf$', value):
            raise ValueError("Invalid filename format.")
        return value
    
    @validator('title')
    @classmethod
    def validate_title(cls, value):
        if any(char in value for char in ['@', '$', '*', '#']):
            raise ValueError("Invalid characters in title. Only alphanumeric characters and spaces are allowed.")
        return value
    
class ContentPDF(BaseModel):
    content_id: int = Field(gt=0)
    doc_id: int = Field(gt=0)
    level: str
    year: int = Field(gt=2010, lt=2025)
    topic: Optional[str] = None
    section_title: Optional[str] = None
    paragraph_text: Optional[str] = None
   
    class Config:
        from_attributes = True
    
    @validator('content_id')
    @classmethod
    def validate_content_id(cls, value):
        if value <= 0:
            raise ValueError("Invalid content_id: must be greater than 0.")
        return value

    @validator('doc_id')
    @classmethod
    def validate_doc_id(cls, value):
        if value <= 0 >3:
            raise ValueError("Invalid doc_id: must be greater than 0 or less than or equal to 3.")
        return value

    @validator('level')
    @classmethod
    def validate_level(cls, value):
        valid_levels = {'Level I', 'Level II', 'Level III'}
        if value not in valid_levels:
            raise ValueError(f"Invalid level: must be one of {valid_levels}.")
        return value

    @validator('year')
    @classmethod
    def validate_year(cls, value):
        if not (2010 <= value <= 2025):
            raise ValueError("Invalid year: must be between 2010 and 2025.")
        return value
    
    @validator('topic', 'section_title', 'paragraph_text')
    @classmethod
    def validate_title(cls, value):
        if any(char in value for char in ['@', '$', '*', '#']):
            raise ValueError("Invalid characters in text. Only alphanumeric characters and spaces are allowed.")
        return value