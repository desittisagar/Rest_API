from django.shortcuts import render
from rest_framework import viewsets
from first_app.serializers import ContestsSerializer,ChallengesSerializer,CollegesSerializer,ViewStatsSerializer,SubmissionStatsSerializer,ProblemSolutionSerializer
from .models import Contests,Colleges,Challenges,View_Stats,Submission_Stats
from django.db.models import Sum
# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection


class ContestViewSet(viewsets.ModelViewSet):
	queryset = Contests.objects.all()
	serializer_class = ContestsSerializer

class CollegeViewSet(viewsets.ModelViewSet):
	queryset = Colleges.objects.all()
	serializer_class = CollegesSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
	queryset = Challenges.objects.all()
	serializer_class = ChallengesSerializer

class TotalViewSet(viewsets.ModelViewSet):
	queryset = View_Stats.objects.all()
	serializer_class = ViewStatsSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
	queryset = Submission_Stats.objects.all()
	serializer_class = SubmissionStatsSerializer

class ProblemSolutionView(APIView):
	def get(self,request):
		cursor = connection.cursor()
		cursor.execute("SELECT con.contest_id, con.hacker_id, con.name, SUM(sg.total_submissions), SUM(sg.total_accepted_submissions), SUM(vg.total_views), SUM(vg.total_unique_views) FROM Contests AS con JOIN Colleges AS col ON con.contest_id = col.contest_id JOIN Challenges AS cha ON cha.college_id = col.college_id LEFT JOIN (SELECT ss.challenge_id, SUM(ss.total_submissions) AS total_submissions, SUM(ss.total_accepted_submissions) AS total_accepted_submissions FROM Submission_Stats AS ss GROUP BY ss.challenge_id) AS sg ON cha.challenge_id = sg.challenge_id LEFT JOIN (SELECT vs.challenge_id, SUM(vs.total_views) AS total_views, SUM(vs.total_unique_views) AS total_unique_views FROM View_Stats AS vs GROUP BY vs.challenge_id) AS vg ON cha.challenge_id = vg.challenge_id GROUP BY con.contest_id, con.hacker_id, con.name HAVING SUM(sg.total_submissions) + SUM(sg.total_accepted_submissions) + SUM(vg.total_views) + SUM(vg.total_unique_views) > 0 ORDER BY con.contest_id;")
		q1 = cursor.fetchall()
		print("hii")
		serializer = ProblemSolutionSerializer(q1, many=True)
		return Response(serializer.data)

	def post(self):
		pass	


# 	#tot = View_Stats.objects.aggregate(Sum('total_views'))
# 	#print(tot)
# 	queryset = Contests.objects.all()
# 	#print(queryset)
# 	serializer_class = ProblemSolution
