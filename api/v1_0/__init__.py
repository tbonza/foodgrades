from flask import Blueprint, g
from ..errors import not_found

api = Blueprint('api', __name__)

@api.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


@api.errorhandler(404)
def not_found_error(e):
    return not_found('item not found')

# do this last to avoid circular dependencies
from . import restaurants, violations
