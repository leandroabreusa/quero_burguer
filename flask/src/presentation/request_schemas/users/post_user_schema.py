from marshmallow import Schema, fields, validate


class EmailErrorsSchema(Schema):
    error_type = fields.Integer(required=True)
    error_at = fields.DateTime(required=True)
    status_code = fields.Integer(required=True)
    reason = fields.String(required=True)
    email = fields.Email(required=True)

class PostUserSchema(Schema):
    relational_db_id = fields.Integer(required=True)
    uuid = fields.String(required=True)
    email_error = fields.Dict(
        fields.Nested(EmailErrorsSchema()),
        required=True
    )