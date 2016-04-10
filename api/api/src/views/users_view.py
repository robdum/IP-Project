import httplib

from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.models.user_model import UserModel, UserSerializer
from api.src.utils import schemas, create_account_utils, login_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class UsersView(BaseView):

    @validate_request(user_required=UserTypeEnum.ADMIN)
    def get(self, request, user_id, token_payload, id=None):
        return self.get_one_or_all(request, UserModel, UserSerializer, id)

    @validate_request(schema=schemas.schema_users_post, user_required=UserTypeEnum.ADMIN)
    def post(self, request, received_json, user_id, token_payload):
        received_json['password_hash'] = create_account_utils.hash_password(received_json['password'])
        return self.post_one(request, received_json, UserModel)

    @validate_request(schema=schemas.schema_users_put, user_required=UserTypeEnum.ADMIN)
    def put(self, request, received_json, user_id, token_payload):
        received_json['password_hash'] = create_account_utils.hash_password(received_json['password'])
        return self.put_one(request, received_json, UserModel)
