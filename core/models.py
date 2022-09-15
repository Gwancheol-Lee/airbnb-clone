from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    """Meta Class는 기타 Property값 설정 등이 가능함. abstract=True는 해당 모델을 추상화 하여 결론적으로 DB에 등록되지 않으며 코드에만 사용된다."""

    class Meta:
        abstract = True
