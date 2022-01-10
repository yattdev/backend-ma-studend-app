#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from student.models.appartment_models import Appartment
from api.serializers.appartment import AppartmentSerializer


class AppartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """ Class ViewSet for AppartmentSerializer """
    queryset = Appartment.objects.filter(is_rented=False)
    serializer_class = AppartmentSerializer
