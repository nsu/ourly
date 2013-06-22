from tastypie.resources import ModelResource
from .models import WorkSession
from tastypie.authorization import Authorization
from datetime import datetime
from django.utils.timezone import utc

from django.contrib.auth.models import User
from tastypie import fields


class WorkSessionAuthorization(Authorization):
    def is_authorized(self, request, object=None):
        return True

    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(user=request.user)

        return object_list.none()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password']

class WorkSessionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    def hydrate(self, bundle, request=None):
        bundle.obj.user = bundle.request.user
        if not bundle.obj.start:
            bundle.obj.start = datetime.utcnow().replace(tzinfo=utc)
        return bundle

    class Meta:
        queryset = WorkSession.objects.all().order_by('-start')
        list_allowed_methods = ['get', 'post', 'put', 'patch']
        authorization = WorkSessionAuthorization()
