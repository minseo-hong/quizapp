from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [
  path('', views.index, name='index'),
  path('word/add/', views.add_word, name='add_word'),
  path('word/delete/<int:word_id>', views.delete_word, name='delete_word'),
  path('word/edit/<int:word_id>', views.edit_word, name='edit_word'),
  path('quiz/', views.start_quiz, name='start_quiz'),
  path('quiz/result', views.show_quiz_result, name='show_quiz_result')
]