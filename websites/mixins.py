from websites.models import Website


# mixins
class PermissionQuerySetMixin:
    def get_website_queryset(self):
        queryset = self.model.objects.filter(
            is_active=True, created_by=self.request.user
        )
        return queryset
