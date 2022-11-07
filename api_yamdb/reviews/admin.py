from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'score', 'title', 'author', 'pub_date', )
    search_fields = ('text', 'author', )
    list_filter = ('pub_date', 'score', 'author', 'title', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'review', 'author', 'pub_date', )
    search_fields = ('text', 'author', )
    list_filter = ('pub_date', 'author', )


class GenreTitleInline(admin.TabularInline):
    model = Title.genre.through


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category', )
    search_fields = ('name', )
    list_filter = ('id', )
    inlines = [GenreTitleInline]


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    list_filter = ('id', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    list_filter = ('id', )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
