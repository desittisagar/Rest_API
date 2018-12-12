from django.contrib import admin
from .models import Contests,Colleges,Challenges,View_Stats,Submission_Stats
# Register your models here.
admin.site.register(Contests)
admin.site.register(Colleges)
admin.site.register(Challenges)
admin.site.register(View_Stats)
admin.site.register(Submission_Stats)

