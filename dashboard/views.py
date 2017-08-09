# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/index.html'
    url = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Presidential%2F1/info.json"

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)
        # url = "https://apitest.secured.vote/jsons/round1/results/Kenya_Elections_Presidential/1/info.json"
        headers = {
            'content-type': "application/json",
        }
        try:
            response = requests.request("GET", self.url, headers=headers)
            data = response.json()
            print data
            context['polling'] = data['progress']
            context['parties'] = data['results']['parties']
            context['title'] = 'Presedential'
            return context
        except:
            print('Error In Connection')
            context['error'] = True
            return context


class SenetorsListTemplateView(DashboardTemplateView):
    url = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Senator%2F1%2F1047/info.json"

    def get_context_data(self, **kwargs):
        context = super(SenetorsListTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Senetor | Nairobi'
        return context


class GovernorListTemplateView(DashboardTemplateView):
    url = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Governor%2F1%2F1047/info.json"

    def get_context_data(self, **kwargs):
        context = super(GovernorListTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Governor | Nairobi'
        return context


class WomensRepListTemplateView(DashboardTemplateView):
    url = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Women_Rep%2F1%2F1047/info.json"

    def get_context_data(self, **kwargs):
        context = super(WomensRepListTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Women Representative | Nairobi'
        return context