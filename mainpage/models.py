from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    prod_price=models.FloatField(default=0)
    prod_mrp=models.FloatField(default=0)
    prod_img=models.ImageField(upload_to='productimages',default=0)
    prod_img2=models.ImageField(upload_to='productimages',default=0)
    prod_img3=models.ImageField(upload_to='productimages',default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_outofstock=models.BooleanField(default=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Blog(models.Model):
    Blog_name = models.CharField(max_length=100)
    blorrer_image=models.ImageField(upload_to='productimages',default=0)
    add_on=models.DateTimeField(auto_now_add=True,null=True)
    description = RichTextField()
    def __str__(self):
        return self.Blog_name
class ExtendedUser(User):
      user=models.OneToOneField(User,parent_link=True,primary_key=True,on_delete=models.CASCADE)
      phone_no=models.CharField(max_length=12,default=0)  
      alt_no=models.CharField(max_length=12,default=0)
      address=models.CharField(max_length=500,default=0)
     
      def __str__(self):
            return self.user.username
   
class order(models.Model):
    customer=models.ForeignKey(ExtendedUser,on_delete=models.CASCADE) 
    product_order=models.ForeignKey(Product,on_delete=models.CASCADE) 
    customer_no=models.IntegerField(default=0)
    customer_name=models.CharField(max_length=100,default=0)
    customer_username=models.CharField(max_length=100,default=0)
    phone=models.CharField(max_length=12,default=0) 
    email=models.CharField(max_length=100,default=0)
    address=models.CharField(max_length=500,default=0)
    Product_id=models.IntegerField(default=0)
    product_img=models.ImageField(upload_to='productimages',default=0)
    Product_quantity=models.IntegerField(default=1)
    product_price=models.FloatField(default=0)
    product_name=models.CharField(max_length=100,default=0)
    status=models.BooleanField(default=False)
    add_on=models.DateTimeField(auto_now_add=True,null=True)
    total_cost=models.FloatField(default=0)
    def __str__(self):
            return self.customer_name
    






class Returns_Shipping_Policy(models.Model):
    description = RichTextField()
class Privacy_Policy(models.Model):
    description = RichTextField()
class Cancelation_Policy(models.Model):
    description = RichTextField()


class about_compeny(models.Model):
    product_img=models.ImageField(upload_to='aboutusbanner',default=0)
    description = RichTextField()
    