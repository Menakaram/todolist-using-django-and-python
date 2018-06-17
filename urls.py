from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addtask', views.addtask, name='addtask')
    url(r'^details/(?P<id>\w{0,50})/$', views.details,name='details'),
    url(r'^add', views.add, name='add')
    url(r'^complete/<todo_id>', views.completeTodo, name='complete'),
    url(r'^deletecomplete', views.deleteCompleted, name='deletecomplete'),
    url(r'^deleteall', views.deleteAll, name='deleteall')
]