from django.urls import path
from .views import GetHomeworkProgress, GetUpcomingLessonsProgress, GetTasksProgress, GetLeaderBoard, GetMyCoursesBoard

urlpatterns = [
    path('homework/', GetHomeworkProgress.as_view()),
    path('lessons/', GetUpcomingLessonsProgress.as_view()),
    path('tasks/', GetTasksProgress.as_view()),
    path('leaderboard/', GetLeaderBoard.as_view()),
    path('mycourses/', GetMyCoursesBoard.as_view()),
]
