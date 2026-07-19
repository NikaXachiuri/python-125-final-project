from django.core.exceptions import ValidationError

def validate_name(value):
    if len(value) > 10:
        raise ValidationError("NAME MUSTN'T BE MORE THAN 10 CHARACTERS LONG")

def validate_comment(value):
    if len(value) > 100:
        raise ValidationError("PLEASE TRY TO KEEP YOUR COMMENT UNDER 100 CHARACTERS LENGTH")