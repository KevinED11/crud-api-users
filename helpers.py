from uuid import UUID


from models.create_user import User
from routes.create_user import user_list


def get_user_by_id(uuid: UUID) -> list[User] | None:
    user_in_list: list[User] = list(filter(lambda user: user.id == uuid,
                                           user_list))
    if not user_in_list:
        return None

    return user_in_list
