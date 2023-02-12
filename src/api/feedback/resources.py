from datetime import datetime
from flask_restful import Resource, abort, current_app
from flask import request
import os
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user

from src.commons.constants import ALLOWED_FILE_EXTENSIONS
from src.feedback.helpers import validate_csv_header, normalize_csv
from src.feedback.service import FeedbackService


class Feedback(Resource):
    method_decorators = [jwt_required()]
    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXTENSIONS
    
    def post(self):
        feedback_file = request.files.get("feedback", None)
        community_data = request.form.to_dict()
        if not (
            feedback_file and
            validate_csv_header(feedback_file) and
            self.allowed_file(feedback_file.filename) and
            community_data
        ):
            return abort(400)
        community_data['size'] = int(community_data['size'])
        file_name = f'{datetime.timestamp(datetime.utcnow())}.csv'
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
        feedback_file.save(file_path)
        
        data = {
            "community": community_data,
            "created_at": float(file_name.split('.')[0]),
            "issues": [
                issue 
                for issue in 
                normalize_csv(current_app.config['UPLOAD_FOLDER'], file_name)
            ],
            "submitted_by": current_user.id,
            "csv_path": file_path,
        }
        FeedbackService().create_feedback(**data)
        return {}, 201