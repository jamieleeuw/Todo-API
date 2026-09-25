def _to_positive_int(value):
    value = value.strip()
    if value.isdigit():
        value = int(value)
        if value > 0:
            return value
    return False

def input_(choice):
    return _to_positive_int(choice)

def user_id(userid):
    return _to_positive_int(userid)

def validate_title(title):
    title = title.strip()
    if title:
        return title
    return False