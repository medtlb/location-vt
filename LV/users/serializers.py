from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import CategoryCar, Car, AvailabilityCar, Reservation


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user
    
class CategoryCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCar
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class AvailabilityCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilityCar
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

# from .models import Client

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'
    
#     def create(self, validated_data):
#         client = Client.objects.create_client(
            
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"]
#             email=validated_data["last_name"]
#         )
#         return client
    
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)
