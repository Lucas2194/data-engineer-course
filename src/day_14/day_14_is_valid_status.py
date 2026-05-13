def is_valid_status(status):
    allowed_statues = ['paid', 'cancel', 'pending']
    return status in allowed_statues

print(is_valid_status('paid'))
print(is_valid_status('sss'))