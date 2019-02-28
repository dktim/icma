#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify


@login_required()
@permission_verify()
def index(request):
    return redirect('/navi/')