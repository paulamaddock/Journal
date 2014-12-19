from django.shortcuts import render

# Create your views here.

from WorkJournal.models import Entry

def getEntries(request,range):
    """
    Retrieve entries that fall in the range of dates
    :param request:
    :param range:
    :return:
    """