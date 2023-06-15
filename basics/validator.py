#this is a module for validating emails 

import re as regular_expressions

def validate_email(email):
    if len(email) > 7:
        return bool(regular_expressions.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
    return False
#this is a module for validating emailsls