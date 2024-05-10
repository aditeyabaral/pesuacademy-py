import requests_html
from typing import Optional
from pesuacademy.models.results import SemesterResult, CourseResult

class ResultsPageHandler:
    @staticmethod
    def get_results_in_semester(
        session: requests_html.HTMLSession, semester_id: Optional[int] = None) -> SemesterResult:
