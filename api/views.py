from rest_framework.decorators import api_view
from rest_framework.permissions import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def get_welcome(request):
    model = Welcome.objects.last()
    serializer = WelcomeSerializer(model).data
    return Response({'data':serializer})

@api_view(["GET"])
def get_direction(request):
    model = Direction.objects.all()
    serializer = DirectionSerializer(model, many=True).data
    return Response({'data':serializer})


@api_view(["POST"])
def create_pupil(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    direction = Direction.objects.get(id=request.POST["direction"])
    user = Pupil.objects.create(
        name = name,
        phone = phone,
        direction = direction,
    )
    return Response({"creates": True, "User": PupilSerializer(user).data})


@api_view(["GET"])
def get_test(request):
        user_id = request.GET["user_id"]
        user = get_object_or_404(Pupil, id=user_id)
        if user.direction.is_logic == False:
            questions = Question.objects.filter(which_direction=user.direction).order_by('?')
            return Response({"success": "True", "Question": QuestionSerializer(questions, many=True).data})
        else:
            questions = Question.objects.filter(which_direction=user.direction).order_by('?')
            logic_questions = LogicQuestion.objects.filter(which_direction=user.direction)
            return Response({"success": "True", "Question": QuestionSerializer(questions, many=True).data, "Logic": LogicQuestionSerializer(logic_questions, many=True).data})

@api_view(["POST"])
def create_result(request):
    try:
        user_id = request.POST["user_id"]
        user = get_object_or_404(Pupil, id=user_id)
        result_id = Result.objects.create(
            user = user,
            which_direction = user.direction,
            how_many_true = request.POST['how_many_true'],
            how_many_false = request.POST['how_many_false'],
            total_questions = user.direction.quantity_of_questions,
        )
        return Response({'success': True, "result_id": {"id":result_id.id}})
    except Exception as err:
        return Response({"success": f"{err}"})

@api_view(['POST'])
def create_logic_reault(request):
    try:
        result_id = request.POST["result_id"]
        result = get_object_or_404(Result, id=result_id)
        question = request.POST["logic_question"]
        UserAnswer.objects.create(
            result = result,
            question = get_object_or_404(LogicQuestion, id=question),
            answer = request.POST["answer"],
        )
        return Response({"success": True})
    except Exception as err:
        return Response({"success": f"{err}"})
