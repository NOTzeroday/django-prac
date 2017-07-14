# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.utils import timezone
import datetime

from .models import Question

# Create your tests here.
class QuestionModelTest(TestCase):

	#test method must begin with "test"
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns true when checking questions with pub_date in the future
		"""
		future_time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=future_time)
		self.assertIs(future_question.was_published_recently(), False)