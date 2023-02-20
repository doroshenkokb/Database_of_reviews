from rest_framework import serializers

from reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        user = self.context['request'].user
        title_id = self.context['view'].kwargs['title_id']
        if Review.objects.filter(author=user, title_id=title_id).exists():
            raise serializers.ValidationError(
                'Отзыв уже оставлен!'
            )
        return data

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date'
        )
        model = Review


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comments."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'pub_date'
        )
        model = Comments
