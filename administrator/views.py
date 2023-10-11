from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from api.models import*
from django.utils.dateparse import parse_duration
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def create_question_view(request, pk):
    form = QuestionForm()
    dir = Direction.objects.get(id=pk)
    context = {
        'form':form,
        'dir': dir,
    }
    if request.method == 'GET':
        return render(request, 'create-question.html', context)
    try:
        if request.method == 'POST' and request.POST.get('adding') == '001':
            q = Question.objects.create(
                which_direction=Direction.objects.get(id=pk),
                question=request.POST['question'],
                answer_a=request.POST['answer_a'],
                answer_b=request.POST['answer_b'],
                answer_c=request.POST['answer_c'],
                answer_d=request.POST['answer_d'],
                true_answer=request.POST['true_answer'],
            )
            if dir.is_logic == True:
                LogicQuestion.objects.create(
                    which_direction=Direction.objects.get(id=pk),
                    logic_question = request.POST.get("logic_question"),
                    which_question=Question.objects.get(id=q.id)
                )
            return redirect('create_question', pk)
        
        if request.method == 'POST' and request.POST.get('editing') == '002':
            q = Question.objects.create(
                which_direction=Direction.objects.get(id=pk),
                question=request.POST['question'],
                answer_a=request.POST['answer_a'],
                answer_b=request.POST['answer_b'],
                answer_c=request.POST['answer_c'],
                answer_d=request.POST['answer_d'],
                true_answer=request.POST['true_answer'],
            )
            if dir.is_logic == True:
                LogicQuestion.objects.create(
                    which_direction=Direction.objects.get(id=pk),
                    logic_question = request.POST.get("logic_question"),
                    which_question=Question.objects.get(id=q.id)
                )
            return redirect('single_question_edit', q.id)
        
        if request.method == 'POST':
            q = Question.objects.create(
                which_direction=Direction.objects.get(id=pk),
                question=request.POST['question'],
                answer_a=request.POST['answer_a'],
                answer_b=request.POST['answer_b'],
                answer_c=request.POST['answer_c'],
                answer_d=request.POST['answer_d'],
                true_answer=request.POST['true_answer'],
            )
            if dir.is_logic == True:
                LogicQuestion.objects.create(
                    which_direction=Direction.objects.get(id=pk),
                    logic_question = request.POST.get("logic_question"),
                    which_question=Question.objects.get(id=q.id)
                )
            return redirect('selected_direction', pk)
    except:
        return redirect('backend_error', pk)
    
@login_required
def create_lg_question_view(request, pk):
    if request.method == 'GET':
        form = LogicForm()
        context={
            'form':form
        }
        return render(request, 'create-logic-question.html', context)
    if request.method == 'POST' and request.POST.get('adding') == '001':
        LogicQuestion.objects.create(
                which_direction=Direction.objects.get(id=pk),
                logic_question = request.POST.get("logic_question"),
            )
        return redirect('create_lg_question', pk)
    if request.method == 'POST' and request.POST.get('editing') == '002':
        lg = LogicQuestion.objects.create(
                which_direction=Direction.objects.get(id=pk),
                logic_question = request.POST.get("logic_question"),
            )
        return redirect('single_logic_question_edit', lg.id)
    if request.method == 'POST':
        LogicQuestion.objects.create(
                which_direction=Direction.objects.get(id=pk),
                logic_question = request.POST.get("logic_question"),
            )
        return redirect('selected_direction_logic', pk)
    
@login_required
def single_logic_question_edit(request, pk):
    if request.method == 'GET':
        obj = get_object_or_404(LogicQuestion, id=pk)
        form = LogicForm(instance=obj)
        context={
            'form':form,
            'pk': pk
        }
        return render(request, 'single-logic-question-edit.html', context)
    if request.method == 'POST' and request.POST.get('adding') == '001':
        obj = get_object_or_404(LogicQuestion, id=pk)
        form = LogicForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('create_lg_question', pk)
    if request.method == 'POST' and request.POST.get('editing') == '002':
        obj = get_object_or_404(LogicQuestion, id=pk)
        form = LogicForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('single_logic_question_edit', pk)
    if request.method == "POST":
        obj = get_object_or_404(LogicQuestion, id=pk)
        form = LogicForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('selected_direction_logic', obj.which_direction.id)
    

def dash_view(request):
    if request.user.username == '':
        return redirect('login')
    else:
        return render(request, 'dash.html')
    
def qwqw(request):
    return redirect('login')

@login_required
def single_question_edit(request, pk):
    obj = get_object_or_404(Question, id=pk)
    dir = Direction.objects.get(id=Question.objects.get(id=pk).which_direction.id)
    try:
        if request.method =='POST' and request.POST.get('adding') == '001':
            d_id = Direction.objects.get(id=Question.objects.get(id=pk).which_direction.id).id
            form = QuestionForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('create_question', d_id)
        if request.method =='POST' and request.POST.get('editing') == '002':
            d_id = Direction.objects.get(id=Question.objects.get(id=pk).which_direction.id).id
            form = QuestionForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('single_question_edit', pk)
        if request.method =='POST':
            d_id = Direction.objects.get(id=Question.objects.get(id=pk).which_direction.id).id
            form = QuestionForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('selected_direction', d_id)
        logy = LogicQuestion.objects.filter(which_direction=dir)
        context = {'form': QuestionForm(instance=obj), "pk": pk, 'dir': dir, 'logy':logy}
            
        return render(request, 'single-question-edit.html', context)
    except:
        logy = LogicQuestion.objects.filter(which_direction=dir)
        obj = get_object_or_404(Question, id=pk)
        dir = Direction.objects.get(id=Question.objects.get(id=pk).which_direction.id)
        context = {'form': QuestionForm(instance=obj), "pk": pk, 'dir': dir, 'logy':logy}
        return render(request, 'single-question-edit.html', context)
    
@login_required
def directions(request):
    return render(request, 'questions-page.html')

@login_required
def create_direction_view(request):
    if request.method == 'POST' and request.POST.get('adding') == '001':
        name=request.POST['name']
        img=request.FILES['img']
        quantity_of_questions=request.POST['quantity_of_questions']
        quantity_of_logic_questions=request.POST['quantity_of_logic_questions']
        timer=request.POST['timer']
        is_logic=request.POST.get('is_logic')
        Direction.objects.create(
            name=name,
            img=img,
            quantity_of_questions=quantity_of_questions,
            quantity_of_logic_questions=quantity_of_logic_questions,
            timer=parse_duration(timer),
            is_logic=True if is_logic == "on" else False,
        )
        return redirect("create_direction")
    
    elif request.method == 'POST' and request.POST.get('editing') == '002':
        name=request.POST['name']
        img=request.FILES['img']
        quantity_of_questions=request.POST['quantity_of_questions']
        quantity_of_logic_questions=request.POST['quantity_of_logic_questions']
        timer=request.POST['timer']
        is_logic=request.POST.get('is_logic')
        obj = Direction.objects.create(
            name=name,
            img=img,
            quantity_of_questions=quantity_of_questions,
            quantity_of_logic_questions=quantity_of_logic_questions,
            timer=parse_duration(timer),
            is_logic=True if is_logic == "on" else False,
        )
        return redirect("direction_edit", obj.id)
    
    if request.method == 'POST':
        name=request.POST['name']
        img=request.FILES['img']
        quantity_of_questions=request.POST['quantity_of_questions']
        quantity_of_logic_questions=request.POST['quantity_of_logic_questions']
        timer=request.POST['timer']
        is_logic=request.POST.get('is_logic')
        Direction.objects.create(
            name=name,
            img=img,
            quantity_of_questions=quantity_of_questions,
            quantity_of_logic_questions=quantity_of_logic_questions,
            timer=parse_duration(timer),
            is_logic=True if is_logic == "on" else False,
        )
        return redirect("directions")
    return render(request, 'create-direction.html')

@login_required
def create_welcome_view(request):

    obj = Welcome.objects.last()

    if request.method == 'GET' and obj:
        context = {
            'obj': obj
        }
        return render(request, 'edit-welcome.html', context)
    
    if request.method == 'GET' and not obj:

        return render(request, 'create-welcome.html')
    
    if request.method == 'POST' and obj:
        if request.FILES and request.FILES.get('logo') != None and request.FILES.get('bg_img') == None:
            logo = request.FILES.get('logo')
            # bg_img = request.FILES.get('bg_img')
            obj.logo=logo
            # obj.bg_img=bg_img
            obj.save()
            return redirect('create_welcome')
        if request.FILES and request.FILES.get('logo') == None and request.FILES.get('bg_img') != None:
            # logo = request.FILES.get('logo')
            bg_img = request.FILES.get('bg_img')
            # obj.logo=logo
            obj.bg_img=bg_img
            obj.save()
            return redirect('create_welcome')
        if request.FILES and request.FILES.get('logo') != None and request.FILES.get('bg_img') != None:
            logo = request.FILES.get('logo')
            bg_img = request.FILES.get('bg_img')
            obj.logo=logo
            obj.bg_img=bg_img
            obj.save()
            return redirect('create_welcome')
        return redirect('create_welcome')

    elif request.method == "POST" and not obj:
        if request.FILES:
            logo = request.FILES.get('logo')
            bg_img = request.FILES.get('bg_img')
            Welcome.objects.create(
                logo=logo,
                bg_img=bg_img,
            )
            return redirect('create_welcome')
        return redirect('create_welcome')

@login_required
def select_direction_view(request):
    context = {
        'dirs': Direction.objects.all().order_by('-name')
    }
    return render(request, 'select-direction.html', context=context)

@login_required
def logic_question_view(request):
    context = {
        'dirs': Direction.objects.all().order_by('-name')
    }
    return render(request, 'select-direction_lg.html', context=context)

@login_required
def selected_direction_view(request, pk):
    direction = Direction.objects.get(id=pk)
    question_list = Question.objects.filter(which_direction=direction).order_by('-id')
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'questions-page.html', context={'questions':questions, 'dir': pk, 'direction': direction})

@login_required
def selected_direction_logic_view(request, pk):
    direction = Direction.objects.get(id=pk)
    question_list = LogicQuestion.objects.filter(which_direction=direction).order_by('-id')
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    lg_questions = paginator.get_page(page)
    return render(request, 'lg-questions-page.html', context={'questions':lg_questions, 'dir': pk, 'direction': direction})

@login_required
def delete_question_view(request, pk):
    a = Question.objects.get(id=pk).which_direction.id
    Question.objects.get(id=pk).delete()
    return redirect('selected_direction', a)

@login_required
def delete_logic_question_view(request, pk):
    a = LogicQuestion.objects.get(id=pk).which_direction.id
    LogicQuestion.objects.get(id=pk).delete()
    return redirect('selected_direction', a)

@login_required
def direction_view(request):
    context = {
        "direction": Direction.objects.all().order_by('-id')
    }
    return render(request, 'direction-page.html', context)

@login_required
def direction_edit_view(request, pk):
    form = get_object_or_404(Direction, id=pk)
    if request.method == 'POST' and request.POST.get('editing') == '002':
        dform = DirectionForm(request.POST, request.FILES, instance=form)
        if dform.is_valid():
            dform.save()
        return redirect('direction_edit', pk)
    elif request.method == 'POST' and request.POST.get('adding') == '001':
        dform = DirectionForm(request.POST, request.FILES, instance=form)
        if dform.is_valid():
            dform.save()
        return redirect('create_direction')
    elif request.method == 'POST':
        dform = DirectionForm(request.POST, request.FILES, instance=form)
        if dform.is_valid():
            dform.save()
        return redirect('directions')
    return render(request, 'direction-edit.html', context={'form':DirectionForm(instance=form), 'pk':pk})

@login_required
def delete_direction_view(request, pk):
    Direction.objects.get(id=pk).delete()
    return redirect('directions')

@login_required
def continue_dir_view(request, pk):
    form = get_object_or_404(Direction, id=pk)
    if request.method == 'POST':
        dform = DirectionForm(request.POST, request.FILES, instance=form)
        if dform.is_valid():
            dform.save()
        return redirect('direction_edit', pk)
    return render(request, 'direction-edit.html', context={'form':DirectionForm(instance=form), 'pk':pk})

@login_required
def get_result_view(request):
    result_list = Result.objects.all().order_by('-id')
    paginator = Paginator(result_list, 10)  # Разбиваем на 10 элементов на странице
    page = request.GET.get('page')
    result = paginator.get_page(page)
    context={
        'obj': result,
    }

    return render(request, 'results.html', context)

@login_required
def logic_answers_view(request, pk):
    user = UserAnswer.objects.filter(result=Result.objects.get(id=pk))
    result = Result.objects.get(id=pk)
    user_answer = UserAnswer.objects.filter(result=result)
    context={
        'user': user,
        'user_answer':user_answer
    }
    return render(request, 'view-logic-answers.html', context)


def login_view(request):
    if request.user.username != '':
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'pages-sign-in.html')
    return render(request, 'pages-sign-in.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard')

def reset_passwd_view(request):
    return render(request, 'forgot.html')

def return_previous_is_logic_view(request, pk):
    q = Question.objects.get(id=pk)
    if q.which_direction.is_logic == True:
        q.which_direction.is_logic=False
        q.which_direction.save()
    else:
        q.which_direction.is_logic=True
        q.which_direction.save()
    return redirect('single_question_edit', pk)

@login_required
def backend_error(request, pk):
    dir = Direction.objects.get(id=pk)
    return render(request, 'pages-500.html', context={'dir': dir})