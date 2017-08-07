# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)
        url = "https://apitest.secured.vote/jsons/round1/results/Kenya_Elections_Presidential/1/info.json"
        headers = {
            'content-type': "application/json",
        }
        try:
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            print data
            context['polling'] = data['progress']
            context['parties'] = data['results']['parties']
            return context
        except:
            print('Error In Connection')
            context['error'] = True
            return context