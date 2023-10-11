from django.forms import *
from api.models import *


class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'
        exclude = ['pupil_count']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['which_direction']


class LogicForm(ModelForm):
    class Meta:
        model = LogicQuestion
        fields = ['logic_question']