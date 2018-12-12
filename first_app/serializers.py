from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Contests, Challenges , Colleges, View_Stats, Submission_Stats

class ContestsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contests
		fields = ('url','contest_id', 'hacker_id','name')
class CollegesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Colleges
		fields = ('url','college_id', 'contest_id')

class ChallengesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Challenges
		fields = ('url','challenge_id', 'college_id')


class ViewStatsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = View_Stats
		fields = ('url','challenge_id', 'total_views','total_unique_views')

class SubmissionStatsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Submission_Stats
		fields = ('url','challenge_id','total_submission','total_accepted_submission')	
class ProblemSolutionSerializer(serializers.Serializer):
	contest_id = serializers.IntegerField()
	hacker_id = serializers.IntegerField()
	name = serializers.CharField(max_length=100)
	sum_total_sub = serializers.IntegerField()
	sum_tatal_acccepted = serializers.IntegerField()	
	sum_total_views = serializers.IntegerField()
	sum_total_unique_views = serializers.IntegerField()