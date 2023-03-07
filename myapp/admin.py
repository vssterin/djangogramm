from django.contrib import admin
from imagekit.admin import AdminThumbnail

from myapp.models import UserProfile, Post, Tag, Photo, Like
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False


class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInLine]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Photo)