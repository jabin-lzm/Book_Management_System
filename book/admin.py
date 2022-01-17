from django.contrib import admin
from book.models import User, Book, Borrow, Log,EmailVerifyRecord


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','password']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'publisher', 'is_available']


class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'borrow_time', 'return_ddl']


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'user', 'book', 'action']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email','send_time']
    search_fields = ['code','email']
    list_filter = ['code','email','send_time']


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
