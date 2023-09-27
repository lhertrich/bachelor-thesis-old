from app import ma 

class TableViewFieldSchema(ma.Schema):
    class Meta:
        fields = ('id', 'data_base_name', 'model_code', 'entity_class_code', 'entity_stereotype', 'comment')

table_view_field_schema = TableViewFieldSchema()
table_view_fields_schema = TableViewFieldSchema(many=True)