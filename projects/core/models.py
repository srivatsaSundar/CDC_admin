from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user or ''
    
class admin_user(models.Model):
    add_user=models.CharField(max_length=100)
    add_password=models.CharField(max_length=100)

    def __str__(self):
        return self.user or ''
    
def one_week_hence():
    return datetime.date.today() + datetime.timedelta(days=7)

class todo_list(models.Model):
    title=models.CharField(max_length=100)

    def get_url(self):
        return reverse('todo_list', kwargs={'todo_list_id': self.id})
    
    def __str__(self):
        return self.title or ''
    
class add_task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    create_date=models.DateField(default=datetime.date.today)
    due_date=models.DateField(default=one_week_hence)
    status=models.CharField(max_length=100)
    todo_list=models.ForeignKey(todo_list, on_delete=models.CASCADE)
    owned_by=models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('item_update',args=[str(self.todo_list.id),str(self.id)])
    
    def __str__(self):
        return f"{self.title} ({self.status}) ({self.due_date}) ({self.owned_by})" or ''
    
    class meta:
        ordering=['-due_date']
    
class company(models.Model):
    company_name=models.CharField(max_length=100)
    company_loaction=models.CharField(max_length=100)
    company_email=models.CharField(max_length=100)
    company_phone=models.CharField(max_length=100)
    company_website=models.CharField(max_length=100)
    company_status=models.CharField(max_length=100)
    date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return f"({self.company_name}) ({self.company_status})" or ''
    
class upcoming(models.Model):
    name_company=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    job_location=models.CharField(max_length=100)
    job_description=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    drive_date=models.DateField(default=datetime.date.today)
    def __str__(self):

        return f"({self.name_company}) ({self.job_title}) ({self.job_location}) ({self.job_description}) ({self.salary}) ({self.status})" or ''