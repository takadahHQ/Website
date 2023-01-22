from modules.accounts.models import User, UserMeta
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from typing import Dict, List

# User
def create_user(
    name: str,
    description: str,
    address: str,
    address2: str,
    phone: str,
    birthday: str,
    city: str,
    state: str,
    country: str,
    zip_code: str,
    bio: str,
    locale: str,
    business_name: str,
):
    try:
        object = User.objects.create(
            name=name,
            description=description,
            address=address,
            address2=address2,
            phone=phone,
            birthday=birthday,
            city=city,
            state=state,
            country=country,
            zip_code=zip_code,
            bio=bio,
            locale=locale,
            business_name=business_name,
        )
        return object
    except:
        error = {"error": "Could not create the user"}
        return error


def register_user(details: dict):
    try:
        name = details["name"]
        description = details["description"]
        user = create_user(name, description)
        return user
    except:
        error = {"error": "Could not create the user"}
        return error


def update_user(user: int, value: dict):
    try:
        object = User.objects.filter(id=user).update(value)
        return object
    except:
        error = {"error": "Could not update user"}
        return error


def read_user(user: int):
    try:
        object = User.objects.get(id=user)
        return object
    except:
        error = {"error": "Could not read the user"}
        return error


def delete_user(user: int) -> bool:
    try:
        object = User.objects.filter(id=user).delete()
        return True
    except:
        return False


def authenticate(username: str, password: str) -> None:
    try:
        user = User.objects.get(
            Q(phone=username) | Q(email=username) | Q(username=username)
        )

    except User.DoesNotExist:
        return None

    if user and check_password(password, user.password):
        return user

    return None


def signin(username: str, password: str, request) -> dict:
    try:
        user = authenticate(username=username, password=password)
        login(request, user)
        msg = {"success": "Sucessfuly loggedin"}
        return msg
    except:
        msg = {"error": "Could not read the user"}
        return msg


def signout(request) -> dict:
    if request.user.is_authenticated:
        logout(request)
        msg = {"success": "Successfuly logged out"}
        return msg
    else:
        msg = {"error": "User already logged out"}
        return msg
