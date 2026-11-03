from app.database.database import users_collection


async def get_user_by_username(username: str):

    return await users_collection.find_one({"username": username})


async def create_user(username: str, hashed_password: str):

    user = {
        "username": username,
        "hashed_password": hashed_password
    }

    await users_collection.insert_one(user)

    return user