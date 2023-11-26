from flask import Blueprint, jsonify

from src.core.app.task.get_all.GetTasks import GetTasks
from src.core.infrastructure.Core import core

get_all_bp = Blueprint('get_all', __name__)


@get_all_bp.route('/tasks', methods=['GET'])
def get_all():
    result = core.execute(GetTasks())
    return jsonify(result)
