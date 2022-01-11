#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from student.models.appartment import Appartment


class AppartmentSerializer(serializers.ModelSerializer):
    """ Class serializer for Appartment models from student app"""
    class Meta:
        model = Appartment
        fields = [
            'id',
            'lessor_name',
            'lessor_number',
            'description',
            'site',
            'is_rented',
            'image',
        ]
        read_only_fields = ['id', 'lessor_name', 'lessor_number']
