from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

from submissions.views.utils import get_popular
from django.contrib.contenttypes.models import ContentType
import os
from django.conf import settings

def popular(request, ctype, filterby, template="submissions/popular/popular_load.html"):
    content_type = get_object_or_404(ContentType, name__iexact=ctype)
    object_dict = get_popular(ctype=content_type, filterby=filterby.lower())

    return render_to_response(template, {
        'ctype': content_type,
        'filterby': filterby,
        'objects': object_dict.items(),
    })
