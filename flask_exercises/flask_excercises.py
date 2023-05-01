import json
from typing import Tuple, Dict, Any, Union

from flask import Flask
from flask import request


users: Dict = {}


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route("/user", methods=["POST"])
        def post() -> Tuple[Dict[str, Any], int]:
            data = json.loads(request.data)

            if "name" in data:
                username = data["name"]
                users[username] = {}

                return {"data": f"User {username} is created!"}, 201

            return {"errors": {"name": "This field is required"}}, 422

        @app.route("/user/<name>", methods=["GET", "PATCH", "DELETE"])
        def manage_user(name: str) -> Tuple[Union[str, Dict[str, Any]], int]:

            if request.method == "GET":

                if name in users:
                    return {"data": f"My name is {name}"}, 200

                return {"data": f"User with name {name} does not exist!"}, 404

            if request.method == "PATCH":

                if name in users:
                    data = json.loads(request.data)
                    new_name = data["name"]
                    users[new_name] = users.pop(name)

                    return {"data": f"My name is {new_name}"}, 200

            if request.method == "DELETE":

                if name in users:
                    users.pop(name)
                    return "", 204

            return {"errors": {"name": f"{name} is not found"}}, 404
