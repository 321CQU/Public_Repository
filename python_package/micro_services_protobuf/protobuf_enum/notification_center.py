from enum import Enum

from ..notification_center.event_pb2 import NOTIFICATION_EVENT_SCORE


__all__ = ['NotificationEvent']


class NotificationEvent(Enum):
    """
    通知中心订阅类
    """
    ScoreQuery = NOTIFICATION_EVENT_SCORE

    @property
    def event_id(self) -> str:
        if self == NotificationEvent.ScoreQuery:
            return "score_query"

        raise RuntimeError("事件ID未定义")

    @staticmethod
    def from_event_id(event_id: str) -> 'NotificationEvent':
        if event_id == 'score_query':
            return NotificationEvent.ScoreQuery

        raise RuntimeError("未知event id")

    @property
    def description(self) -> str:
        if self == NotificationEvent.ScoreQuery:
            return "定时查询成绩，比较数据库以获取新出的成绩并发送通知"

        raise RuntimeError("事件描述未定义")

    @staticmethod
    def get_all_events_description():
        return "".join([f"{event.value}: {event.description}; \n" for event in NotificationEvent])

