from collections.abc import Iterable
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Welcome(models.Model):
    # name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='welcome/')
    bg_img = models.ImageField(upload_to="welcome/")


class Direction(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='directions/')
    pupil_count = models.PositiveIntegerField(default=0)
    quantity_of_questions = models.PositiveIntegerField()
    quantity_of_logic_questions = models.PositiveIntegerField(null=True, blank=True)
    timer = models.DurationField(default=0)
    is_logic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Pupil(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(unique=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.direction.pupil_count += 1
        self.direction.save()
        return super().save( *args, **kwargs)
    
    def delete(self):
        self.direction.pupil_count -= 1
        self.direction.save()
        return super().delete()

    def __str__(self):
        return self.name


class Question(models.Model):
    which_direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    question = RichTextUploadingField()
    answer_a = RichTextUploadingField()
    answer_b = RichTextUploadingField()
    answer_c = RichTextUploadingField()
    answer_d = RichTextUploadingField()
    true_answer = models.IntegerField(choices=(
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
        )
    )

    def save(self, *args, **kwargs):
        q = Question.objects.filter(which_direction=self.which_direction)
        if q.count() < self.which_direction.quantity_of_questions and q.count() != self.which_direction.quantity_of_questions:
            return super().save(*args, **kwargs)
        else:
            raise SystemError(f"Savol qo'shish chegaralangan! maksimum {self.which_direction.quantity_of_questions}!")


class LogicQuestion(models.Model):
    which_direction = models.ForeignKey(Direction, on_delete=models.DO_NOTHING)
    logic_question = RichTextUploadingField()


class Result(models.Model):
    user = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    which_direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    how_many_true = models.PositiveIntegerField()
    how_many_false = models.PositiveIntegerField()
    total_questions = models.IntegerField()


class UserAnswer(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    question = models.OneToOneField(LogicQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
