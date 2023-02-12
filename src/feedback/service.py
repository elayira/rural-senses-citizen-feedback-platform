from .models import Feedback
from .schemas import FeedbackSchema

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
