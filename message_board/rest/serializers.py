from rest_framework import serializers

from message_board.models import MessageBoard


class MessageBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBoard
        fields = "__all__"
        extra_kwargs = {
            'publish_time': {'format': "%Y-%m-%d %H:%M:%S"},
            'annex': {'require': False, 'allow_null': True},
        }
