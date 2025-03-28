from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('local/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
 path('search',views.search,name='search'),
path('productsearch',views.productsearch,name='productsearch'),
path('login',views.login,name='login'),
path('productview/<int:myid>',views.productview,name='productview'),
path('createaccount',views.createaccount,name='createaccount'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('userprofile',views.userprofile,name='userprofile'), 
path('search',views.search,name='search'),
path('myaddtocart',views.myaddtocart,name='myaddtocart'),
path('productview/myaddtocart',views.myaddtocart,name='myaddtocart'),
path('mycart',views.mycart,name='mycart'), 
path('productview/mycart',views.mycart,name='mycart'),
path('clearcart',views.clearcart,name='clearcart'),
path('myaddtocarttcart',views.myaddtocarttcart,name='myaddtocarttcart'),
path('myaddtocartcart',views.myaddtocartcart,name='myaddtocartcart'),
path('removecatitem',views.removecatitem,name='removecatitem'),
path('orderdone',views.orderdone,name='orderdone'),
path('myorders',views.myorders,name='myorders'),
path('studyblog/<int:myid>',views.studyblog,name='studyblog'),
path('returnandshipping',views.returnandshipping,name='returnandshipping'),
path('cancelpolicy',views.cancelpolicy,name='cancelpolicy'),
path('pripolicy',views.pripolicy,name='pripolicy'),
path('aboutus',views.aboutus,name='aboutus'),
# password
 path('changepassword',views.changepassword,name='changepassword'),
    path('changepassword2',views.changepassword2,name='changepassword2'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),


]
