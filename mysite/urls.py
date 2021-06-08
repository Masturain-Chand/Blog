from django.conf.urls import url
from mysite.core import views as core_views

urlpatterns = [
    ...
    url(r'^$', core_views.home, name='home')
    url(r'^signup/$', core_views.signup, name='signup'),
url(r'^login/$',
 auth_views.LoginView.as_view(template_name='login.html'),
name='login'),
 url(r'admin/', admin.site.urls),

]
