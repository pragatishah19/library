from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:author_detail_view", kwargs={"pk": self.pk})

class Genre(models.Model):
    name = models.CharField(max_length=32)
    document = models.FileField(upload_to='book_doc',null = True,blank = True)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=32,help_text="enter book name")
    author= models.ForeignKey(Author,on_delete=models.CASCADE)
    price= models.DecimalField(decimal_places=2,max_digits=4)
    is_available= models.BooleanField(default=True)
    pub_date=models.DateField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='book_pic', null = True, blank = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:book_detail_view", kwargs={"pk": self.pk})
    
class User(models.Model):
    name = models.CharField(max_length=32)
    mobile = models.IntegerField()
    books = models.ManyToManyField(Books,null = True,blank = True)
    no_of_books_taken = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:user_detail_view", kwargs={"pk": self.pk})
