from django.db import models

# Create your models here.''


class Contests(models.Model):
	contest_id = models.IntegerField(primary_key=True)
	hacker_id = models.IntegerField()
	name = models.CharField(max_length = 100)

class Colleges(models.Model):
	college_id = models.IntegerField(primary_key=True)
	contest_id = models.ForeignKey(Contests,on_delete = models.CASCADE)

class Challenges(models.Model):
	challenge_id = 	models.IntegerField(primary_key=True)
	college_id = models.ForeignKey(Colleges, on_delete=models.CASCADE)

class  View_Stats(models.Model):
	challenge_id = models.ForeignKey(Challenges,on_delete=models.CASCADE)
	total_views = models.IntegerField()
	total_unique_views = models.IntegerField()

class Submission_Stats(models.Model):
	challenge_id = models.ForeignKey(Challenges,on_delete=models.CASCADE)
	total_submission = models.IntegerField()
	total_accepted_submission = models.IntegerField()
