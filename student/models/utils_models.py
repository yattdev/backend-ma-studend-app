#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Communaute(models.Model):
    """ Model for Communauté """
    name = models.CharField(max_length=100,
                            verbose_name="Nom de l'association",
                            null=False,
                            unique=True,
                            blank=False)


class AllowedNumber(models.Model):
    """ Model for allowed phone number """
    phone = models.CharField(max_length=10,
                             unique=True,
                             null=False,
                             blank=False,
                             verbose_name="Whats'app")
    communaute = models.ForeignKey(Communaute,
                                   related_name="phones",
                                   on_delete=models.CASCADE,
                                   verbose_name="Communauté")
