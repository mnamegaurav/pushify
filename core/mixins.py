from core.models import Notification


# mixins
class QuerySetMixin:
    def get_notification_queryset(self):
        queryset = self.model.objects.filter(created_by=self.request.user)
        return queryset
