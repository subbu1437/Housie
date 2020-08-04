import re

from django.contrib.auth import get_user_model, login, authenticate


class UserValidator:
    def __init__(self):
        pass


class UserHandler:
    def __init__(self):
        self.model = get_user_model()

    def _is_mobile(self, mobile):
        return re.compile("(0/91)?[6-9][0-9]{9}").match(mobile)

    def _validate(self, name, mobile):
        user = self.model.objects.filter(mobile=mobile)
        if not user.count() == 0:
            return False, "mobile number already registered"

        if not self._is_mobile(mobile):
            return False, "invalid mobile number"
        return True, "true"

    def sign_up(self, name, mobile, password, request=None):
        is_valid, msg = self._validate(name=name, mobile=mobile)

        if not is_valid:
            raise Exception(msg)
            # return is_valid, msg

        user = self.model.objects.create_user(email="", mobile=mobile, password=password, cast="customer")
        user.name = name
        user.save()

        if request:
            login(request, user)
        return user, "success"

    def login(self, mobile, password, request):
        if self._is_mobile(mobile):
            try:
                user = self.model.objects.get(mobile=mobile)
            except self.model.DoesNotExist:
                return False
            auth_user = authenticate(mobile=mobile, password=password)
            if auth_user:
                login(request, user)
            return auth_user
        return False

    def is_exist(self, mobile):
        return self.model.objects.filter(mobile=mobile).count() == 1

    def update_password(self, mobile, password):
        if self._is_mobile(mobile):
            user = self.model.objects.get(mobile=mobile)
            user.set_password(password)
            user.save()
            return True
        return False

    def set_role(self, mobile, role):
        if self._is_mobile(mobile):
            user = self.model.objects.get(mobile=mobile)
            user.cast = role
            user.save()
            return True
        else:
            raise Exception("Invalid mobile number")
