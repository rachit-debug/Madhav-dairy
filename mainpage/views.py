from django.contrib.auth import authenticate,login
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,SetPasswordForm
from django.core.mail import send_mail, EmailMultiAlternatives
from mainpage.models import *
import datetime
# Create your views here.
def indexpage(request):
     blog=Blog.objects.all()
     categories = Category.objects.all()  # Retrieve all categories
     allp=Product.objects.all()
     return render(request,'index.html',{'categories': categories,'allp':allp,'blog':blog})

def productview(request,myid):
    categories = Category.objects.all()
    allcategories=Category.objects.all()
    blog=Blog.objects.all()
    myproducts=Product.objects.filter(id=myid)
    return render(request,'productview.html',{'myproducts':myproducts[0],'categories': categories,'blog':blog})


def createaccount(request):
    categories = Category.objects.all()
    allcategories=Category.objects.all()
    if request.method=='POST':
        f_name=request.POST['customername']
        u_name=request.POST['customerusernam']
        passw1=request.POST['customerpassword']
        email=request.POST['customeremail']
        phone1=request.POST['userphone']
        addre=request.POST['customeraddress']
        print(f_name)
        
        if User.objects.filter(username=u_name).exists():
            messages.info(request,'User Name already exists...')
            # print("user pale se available hai")
            return render(request,'signup.html',{'categories': categories})    
        else:
            user=ExtendedUser.objects.create_user(first_name=f_name,username=u_name,email=email,phone_no=phone1,address=addre,password=passw1)
            user.save()
            user=auth.authenticate(username=u_name,password=passw1)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/')
            messages.add_message(request,messages.SUCCESS,' Account Created Successfully..!!!')
            return HttpResponseRedirect('/')     
            messages.add_message(request,messages.SUCCESS,' Account Created Successfully..!!!')
            # print("user created")
    return render(request,'signup.html',{'categories': categories})   

def login(request):
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if request.method=='POST':
            uname=request.POST['username']
            ppass=request.POST['ukapass']
            print(uname,ppass)
            user=auth.authenticate(username=uname,password=ppass)
            print("user jo login kr raha hai",user)
            if user is not None:
                auth.login(request,user)
                allp=Product.objects.all()
                if request.user.is_authenticated:
                   return HttpResponseRedirect('/')
                return render(request,'index.html',{'categories': categories,'allp':allp,'blog':blog})
               
            else:
                print("record not found") 
                messages.info(request,'Password or username is incorrect Or Create your new Account')  
                return HttpResponseRedirect('/')
                # this elif is for get request







def logout(request):
    auth.logout(request)
    return redirect('/')

def userprofile(request):
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if request.user.is_authenticated:
        profile = ExtendedUser.objects.get(user=request.user)
        return render(request,"profiledashboard.html",{'categories': categories,'allp':allp,'blog':blog,'profile':profile})
    return render(request,'signup.html',{'categories': categories})

def productsearch(request):
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if "qry" in request.GET:
        q=request.GET["qry"]
        print(q)
        if Product.objects.filter(category=q):
            myproducts=Product.objects.filter(category=q)
            print(myproducts)
            return render(request,'customerview.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts})
    return HttpResponse("not fond")


def search(request):
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if "qry" in request.GET:
        q=request.GET["qry"]
        print(q)
        if Product.objects.filter(name__icontains=q):
            myproducts=Product.objects.filter(name__icontains=q)
            return render(request,'search.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts})
        elif Product.objects.filter(description__icontains=q):  
            myproducts=Product.objects.filter(description__icontains=q)
            return render(request,'search.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts})
        elif Product.objects.filter( prod_price__icontains=q):  
            myproducts=Product.objects.filter( prod_price__icontains=q)
            return render(request,'search.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts}) 
        elif Product.objects.filter(prod_mrp__icontains=q):  
            myproducts=Product.objects.filter(prod_mrp__icontains=q)
            return render(request,'search.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts}) 
       
        elif Product.objects.filter(prod_price__icontains=q):  
            myproducts=Product.objects.filter( prod_price__icontains=q)
            return render(request,'search.html',{'categories': categories,'allp':allp,'blog':blog,'myproducts':myproducts})   
    return HttpResponse("<h1>No result found</h1>") 

def myaddtocart(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        print(productt)
        cart=request.session.get('cart')
        print("empty card = ",cart)
        if cart:
           quantity = cart.get(productt)
           print(cart.get(productt))
           if quantity:
                cart[productt] = quantity+1  
                print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def mycart(request):
    allcategories=Category.objects.all()
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    cart=request.session.get('cart')
    if not cart:
        request.session.cart={}
        return render(request,'showcart.html',{"categories":categories})
    print(request.session.get('cart'))
    print(request.session.get('cart').keys())
    print("list of keys = ",list(request.session.get('cart').keys()))
    ids=list(request.session.get('cart').keys())
    print(ids)
    myproducts=Product.objects.filter(id__in=ids)
    print(myproducts)
    return render(request,'showcart.html',{'myproducts':myproducts,"categories":categories})

def clearcart(request):
    # request.session.get('cart').clear()
    request.session['cart'] = {}
    print("cart clear")
    return HttpResponseRedirect('/')

def myaddtocarttcart(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        remove=request.POST['remove']
        print(productt,remove)
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
               if remove:
                   if quantity<=1:
                       cart.pop(productt)
                       print("pop kiya")
                   else:    
                      cart[productt] = quantity-1
                      print("-1 kiya")
               else:
                 cart[productt] = quantity+1  
                 print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart')  

def myaddtocartcart(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
                cart[productt] = quantity+1  
                print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart') 

def removecatitem(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        remove=request.POST['remove']
        print(productt,remove)
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
               if remove:
                   if quantity:
                       cart.pop(productt)
                       print("pop kiya")
                   else:    
                       cart.pop(productt)
                       print("pop kiya")
               else:
                 cart[productt] = quantity+1  
                 print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart')  
    
def orderdone(request):
     if request.user.is_authenticated:
        profile = ExtendedUser.objects.get(user=request.user)
        currentcustomer=profile.user_id
        cart=request.session.get('cart')
        print("my cart = ",cart)
        mproducts=Product.objects.filter(id__in=list(cart.keys()))
        print(mproducts)
        for i in mproducts:
            print("quant",cart.get(str(i.id)))
            Product_ki_quantity=cart.get(str(i.id))
            p=Product_ki_quantity*i.prod_price
            print("total order cost=",p)
            ordernow=order(customer_id=currentcustomer,product_order_id=i.id,customer_no=currentcustomer,customer_name=profile.first_name,customer_username=profile.username,phone=profile.phone_no,email=profile.email,address=profile.address,Product_quantity=cart.get(str(i.id)),Product_id=i.id,product_price=i.prod_price,product_name=i.name,product_img=i.prod_img,total_cost=p)
            ordernow.save()
        request.session['cart'] = {}    
        return render(request,'orderdone.html')
     return render(request,'signup.html') 


def myorders(request):
    if request.user.is_authenticated:
         tt=datetime.datetime.now()
         profile = ExtendedUser.objects.get(user=request.user)
         blog=Blog.objects.all()[:2]
         categories = Category.objects.all()  # Retrieve all categories
         allp=Product.objects.all()
         mcart=order.objects.filter(customer_no=request.user.id)
         count=0
         sscount=0
             
         for i in mcart:
             if i.status:
                 count=count+1
             else:
                 sscount=sscount+1
                 
             
         print(count)
         print(sscount)
         return render(request,'profiledashboard.html',{'mcart':mcart,'blog':blog,'categories':categories,'allp':allp,'profile':profile,'count':count,'tt':tt,'sscount':sscount})
    return render(request,'signup.html')

def studyblog(request,myid):
    bl=Blog.objects.filter(id=myid).first()
    return render(request,"readblog.html",{'bl':bl})

def returnandshipping(request):
    ship=Returns_Shipping_Policy.objects.all().first()
    return render(request,"returnandshipping.html",{"ship":ship})

def cancelpolicy(request):
    canp=Cancelation_Policy.objects.all().first()
    return render(request,"cancelationpolicy.html",{"canp":canp})

def pripolicy(request):
    ppo=Privacy_Policy.objects.all().first()
    return render(request,"privacypolicy.html",{"ppo":ppo})


def aboutus(request):
    categories = Category.objects.all()
    aboutc=about_compeny.objects.all().first()
    return render(request,"about.html",{"aboutc":aboutc,"categories":categories})


def changepassword(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                # print(fm)
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password change Successfully')
                return HttpResponseRedirect('profile')
        else:    
            fm=PasswordChangeForm(user=request.user)
        return render (request,'changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')     

# another method to change password is old password nai hoga
def changepassword2(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password change Successfully')
                return HttpResponseRedirect('profile')
        else:    
            fm=SetPasswordForm(user=request.user)
        return render (request,'changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')    






