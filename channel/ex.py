from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification
from .serializers import NotificationSerialidzer


def get_notification():
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return serializer.data


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.center_name = self.scope['url_route']['kwargs']['center_name']  # notification/routing.py에 있는 center_name

        async_to_sync(self.channel_layer.group_add)(  # group 참여
            self.group_name,
            self.channel_name
        )
        self.accept()  # websocket 연결

        # notification이 있으면 알람 전송
        notifications = get_notification()
        if notifications:
            async_to_sync(self.channel_layer.group_send)(
                "center_name", {
                    "type": "notify",
                    "data": notifications
                }
            )

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def notify(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))



# DB model에 관련해서 save가 작동하면, 저장이 완료된 이후에 지정한 동작을 수행
@receiver(post_save, sender=Notification)
def send_update(sender, instance, created, **kwargs):
    print("New reading in DB")
    serializer = NotificationSerializer(instance)

    if created:
        print("New saving in DB")
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "center_name", {
                "type": "notify",
                "data": serializer.data
            }
        )