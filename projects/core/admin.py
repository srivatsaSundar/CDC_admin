from django.contrib import admin
from .models import login,company,upcoming,todo_list,add_task,admin_user

admin.site.register(login)
admin.site.register(admin_user)
admin.site.register(company)
admin.site.register(upcoming)
admin.site.register(todo_list)
admin.site.register(add_task)
