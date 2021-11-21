user = {
    'name': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10
        }
    },
    'age': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'number',
            'min': 0,
            'max': 199
        }
    }
}