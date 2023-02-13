from .helpers import feedback_issue_processor
from .models import Feedback
from .schemas import FeedbackSchema
from src.config import UPLOAD_FOLDER

class FeedbackService:
    model = Feedback
    schema = FeedbackSchema

    def create_feedback(self, **fields):
        instance = self.schema().load(fields)
        instance.save()
        return instance
    
    def update_feedback(self, instance, **fields):
        instance = self.schema().update(instance, fields)
        instance.save()
        return instance
    
    def process_feedback(self, csv_file_name, data):
        instance = self.create_feedback(**data)
        issues = []
        issue_analysis = {}
        for item in feedback_issue_processor(UPLOAD_FOLDER, csv_file_name):
            if not item.get('age', None):
                issue_analysis = item
            else:
                issues.append(item)
        self.update_feedback(
            instance, issues=issues, issue_analysis=issue_analysis
        )
        return instance
