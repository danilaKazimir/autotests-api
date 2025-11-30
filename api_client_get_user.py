from clients.private_http_builder import AuthenticationUserDict
from clients.user.private_users_client import get_private_users_client
from clients.user.public_users_client import (
    CreateUserRequestDict,
    get_public_users_client,
)


public_users_clinet = get_public_users_client()


create_user_request = CreateUserRequestDict(
    email="testxxx333222x@test.com",
    password="123xxx",
    lastName="testxxx",
    firstName="testxxx",
    middleName="testxxx",
)
create_user_response = public_users_clinet.create_user_api(create_user_request).json()


auth_user = AuthenticationUserDict(
    email=create_user_request.get("email"), password=create_user_request.get("password")
)
private_users_client = get_private_users_client(auth_user)

get_user_response = private_users_client.get_user_api(
    create_user_response.get("user").get("id")
).json()
print("Get user data:" + str(get_user_response))
