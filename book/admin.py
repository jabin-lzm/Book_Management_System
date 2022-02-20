from django.contrib import admin
from book.models import User, Book, Borrow, Log,EmailVerifyRecord,Request


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','password']
    list_per_page = 20


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'publisher', 'is_available']
    list_per_page = 20


class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'borrow_time', 'return_ddl']
    list_per_page = 20


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'user', 'book', 'request', 'action']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email','send_time']
    search_fields = ['code','email']
    list_filter = ['code','email','send_time']
    list_per_page = 20


class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'author', 'publisher', 'request_time', 'is_available']
    list_editable = ['is_available']
    list_per_page = 20


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Request,RequestAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


admin.site.site_header = "龙氏书院"
admin.site.site_title = "龙氏书院BMS"
admin.site.index_title = "欢迎使用龙氏书院BMS"
