#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.views.appartment_views import AppartmentViewSet
from api.views.utils_view import get_csrf_token

__all__ = [AppartmentViewSet, get_csrf_token]
