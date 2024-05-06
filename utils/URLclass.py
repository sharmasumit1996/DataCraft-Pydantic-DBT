
from pydantic import BaseModel, PositiveInt, HttpUrl,validator,field_validator, model_validator, ValidationError, ValidationInfo
from typing import List
import re

class Article(BaseModel):
    # data = [topic, year, level, introdu, Learning outcome, PDF, link]
    NameOfTopic: str = 'None'
    Title: str = 'None'
    Year: PositiveInt = 1900
    Level: str = 'Level I'
    Introduction: str = 'None'
    LearningOutcome: str = 'None'
    LinkToPDF: HttpUrl = 'www.example.org'
    LinkToSummary: HttpUrl = 'www.example.org'

    ## year: 2024 Curriculum
    @field_validator('Year',mode='before')
    @classmethod
    def extract_year(cls, v):
        if isinstance(v, str):  
            # extract year from the str
            year_part = v.split(' ')[0]  # year at the first
            year_part = int(year_part)
            if 1900 <= year_part <= 2100: # year_part is String
                return int(year_part)  # return to int
            else:    
                raise ValueError(f"Year {year_part} not in range 1900-2100.")

        return v # default number should be good

    ## 
    @field_validator('Level', mode='before')
    @classmethod
    def level_only_have_three(cls, v):
        match = re.search(r'^Level\s(I{1,3})$', v) # start with Level and have 1-3 I
        if match:
            return v
        else:
            raise ValueError(f"Not proper level {v}")
