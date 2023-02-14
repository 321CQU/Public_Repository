from micro_services_protobuf.notification_center.apns_pb2 import SetUserApnsRequest, SendApnsNotificationRequest
from micro_services_protobuf.common_pb2 import DefaultResponse


__all__ = ['MockApnStub']


class MockApnStub:
    async def SetUserApns(self, request: SetUserApnsRequest) -> DefaultResponse:
        return DefaultResponse(msg='success')

    async def SendNotificationToUser(self, request: SendApnsNotificationRequest) -> DefaultResponse:
        return DefaultResponse(msg='success')
