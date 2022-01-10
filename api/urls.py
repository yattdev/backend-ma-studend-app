#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from .views.utils_view import get_csrf_token
from .views.appartment_views import AppartmentViewSet

from rest_framework.routers import SimpleRouter

# -------------------------
# student application endpoints
router = SimpleRouter()

# Appartment List/Details endpoints
router.register('appartments', AppartmentViewSet, basename="appartments")

urlpatterns = [
    path('get-token/', get_csrf_token, name="get-token"),  # to get csrf_token
    # third party apps urls for users authentication
    path("auth", include("rest_framework.urls")),
    path('auth', include('djoser.urls'), name="auth"),
    path('auth', include('djoser.urls.jwt')),
] + router.urls
