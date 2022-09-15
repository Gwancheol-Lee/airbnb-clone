from django.db import models


class TimeStampedModel(models.Model):

    """
    auto_now_add=True -> 새로운 Model을 만들면 장고가 현재 날짜랑 시간값을 created에 업데이트
    auto_now=True -> Model을 매 번 저장할 때마다 장고가 현재 날짜랑 시간값을 updated에 업데이트
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """Meta Class는 기타 Property값 설정 등이 가능함. abstract=True는 해당 모델을 추상화 하여 결론적으로 DB에 등록되지 않으며 코드에만 사용된다."""

    class Meta:
        abstract = True
