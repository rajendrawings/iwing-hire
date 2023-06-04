from django.contrib.auth.models import User


def create_user(validated_data):
    data = {
        "username": validated_data.get("email", ""),
        "email": validated_data.get("email", ""),
        "password": validated_data.get("password", "")
    }

    password = validated_data.pop('password', None)
    instance = User.objects.create(**data)
    
    # Adding the below line made it work for me.
    instance.is_active = True
    if password is not None:
        # Set password does the hash, so you don't need to call make_password 
        instance.set_password(password)
    instance.save()
    return instance