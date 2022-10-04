from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from quiz.models import Word
from quiz.models import Score

# Create your views here.
def index(request):
  word_list = Word.objects.all()
  data = { 'word_list': word_list }

  return render(request, 'word_list.html', data)


def add_word(request):
  if request.method == 'POST':
    word = Word(english=request.POST.get('english'), korean=request.POST.get('korean'))
    word.save()

    return redirect('quiz:index')
  else:
    return render(request, 'word_add.html')


def delete_word(request, word_id):
  word = Word.objects.get(id=word_id)
  word.delete()

  return redirect('quiz:index')


def edit_word(request, word_id):
  if request.method == 'POST':
    word = Word.objects.get(id=word_id)
    word.english = request.POST.get('english')
    word.korean = request.POST.get('korean')
    word.save()

    return redirect('quiz:index')
  else:
    word = Word.objects.get(id=word_id)
    data = { 'word': word }

    return render(request, 'word_edit.html', data)


def start_quiz(request):
  if request.method == 'POST':
    score = 0
    words_korean = []

    for korean in request.POST:
      words_korean.append(korean)
    words_korean.pop(0)

    for korean in words_korean:
      word = Word.objects.get(korean=korean)
      if (word.english == request.POST.get(korean)):
        score += 1
    
    score_all = Score.objects.all()
    if score_all:
      score_all.delete()
    
    score_model = Score(score=score, total_score=len(words_korean))
    score_model.save()

    return redirect('quiz:show_quiz_result')
  else:
    word_list = Word.objects.order_by('?')
    data = { 'word_list': word_list }

    return render(request, 'word_quiz.html', data)


def show_quiz_result(request):
  score_model = Score.objects.all().first()
  data = { 'score': score_model.score, 'total_score': score_model.total_score }

  return render(request, 'word_quiz_result.html', data)