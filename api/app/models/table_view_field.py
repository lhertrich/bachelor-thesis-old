from app import db

class TableViewField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_base_name = db.Column(db.String)
    model_code = db.Column(db.String)
    entity_class_code = db.Column(db.String)
    entity_stereo_type = db.Column(db.String)
    comment = db.Column(db.String)

    def __init__(self, data_base_name, model_code, entity_class_code, entity_stereo_type, comment):
        self.data_base_name = data_base_name
        self.model_code = model_code
        self.entity_class_code = entity_class_code
        self.entity_stereo_type = entity_stereo_type
        self.comment = comment