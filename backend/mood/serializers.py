"""Serializers for mood app."""
from rest_framework import serializers
from .models import MoodLog


class MoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodLog
        fields = (
            'id', 'mood_score', 'energy_score',
            'note', 'log_date', 'created_at'
        )
        read_only_fields = ('id', 'created_at', 'log_date')

    def validate(self, attrs):
        for field in ('mood_score', 'energy_score'):
            val = attrs.get(field)
            if val is not None and not (1 <= val <= 5):
                raise serializers.ValidationError(
                    {field: 'Skor harus antara 1 dan 5.'}
                )
        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return MoodLog.objects.create(**validated_data)
