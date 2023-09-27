from app import ma 

class InterfaceDefintionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'schema_name', 'schema_id', 'data_core_layer', 'object_name', 'object_id', 'object_type', 'object_type_description', 'object_sql_code_anzahl_character', 'object_sql_code_first_3276_characters')

interface_definition_schema = InterfaceDefintionSchema()
interface_definitions_schema = InterfaceDefintionSchema(many=True)