from rest_framework import serializers
from .models import *

class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class LogicQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogicQuestion
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"