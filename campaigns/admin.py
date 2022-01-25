from django.contrib import admin

from campaigns.serializers import SubscriberSerializer

from .models import Campaign, Subscriber

admin.site.register(Campaign)
admin.site.register(Subscriber)
