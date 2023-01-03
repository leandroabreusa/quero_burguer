from marshmallow import Schema, fields

class UpdateDeliveryFeeSchema(Schema):
    value = fields.Decimal(required=True)