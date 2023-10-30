from news.models import Comment, Rate
from rest_framework import serializers
from . import serializers as ser
from news.serializers import ReviewerSerializer


def add_comment(user, obj, comment):
    comment_obj, is_created = Comment.objects.get_or_create(user=user, new=obj)
    comment_obj.comment = comment
    comment_obj.save()
    if is_created:
        return 'Added comment'
    return 'Updated comment'


def delete_comment(obj, user):
    try:
        Comment.objects.get(new=obj, user=user).delete()
    except Comment.DoesNotExist:
        return 'No comment to delete!'


def is_commented(obj, user):
    try:
        return Comment.objects.filter(user=user, new=obj).exists()
    except TypeError:
        return False


def get_commenters(obj):
    commenters = Comment.objects.filter(new=obj)
    serializer = ser.CommentSerializer(commenters, many=True)
    commenters = [{'user': i['user'], 'comment': i['comment']} for i in serializer.data]
    return commenters


def get_user_comments(user):
    comments = Comment.objects.filter(user=user)
    serializer = ser.CommentSerializer(comments, many=True)
    comments = [{'new': i['new'], 'comment': i['comment']} for i in serializer.data]
    return comments
#-----------------------------------------------


def add_rating(user, obj, rating):
    if 0<= int(rating) <= 5:
        rating_obj, is_created = Rate.objects.get_or_create(user=user, new=obj)
        rating_obj.rating = rating
        rating_obj.save()
        if not is_created:
            return 'Updated rating'
        return 'Added rating'
    raise serializers.ValidationError('Entered an incorrect Rating!')


def delete_rating(user, obj):
    try:
        Rate.objects.filter(new=obj, user=user).delete()
    except Rate.DoesNotExist:
        return 'No rating to delete!'


def is_rater(obj, user):
    try:
        return Rate.objects.filter(user=user, new=obj).exists()
    except TypeError:
        return 'Rate Does Not Exist'


def get_rates(obj):
    users = Rate.objects.filter(new=obj)
    serializer = ReviewerSerializer(users, many=True)
    return serializer.data
