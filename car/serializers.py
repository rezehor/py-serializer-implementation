from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(required=True)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    def validate_horse_powers(self, value):
        if 1 <= value <= 1914:
            return value
        raise serializers.ValidationError(
            "Horse power must be between 1 and 1914"
        )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get("model", instance.model)
        instance.is_broken = validated_data.get(
            "is_broken",
            instance.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description
        )
        instance.horse_powers = validated_data.get(
            "horse_powers",
            instance.horse_powers
        )
        instance.save()
        return instance
