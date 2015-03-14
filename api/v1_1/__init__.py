from flask import Blueprint, g
from ..errors import not_found

api_1_1 = Blueprint('api_1_1', __name__)

@api_1_1.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


@api_1_1.errorhandler(404)
def not_found_error(e):
    return not_found('item not found')

# do this last to avoid circular dependencies
from . import restaurants, violations
