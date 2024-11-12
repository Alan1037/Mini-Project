from django.contrib import admin
from .models import *

# class auction(admin.ModelAdmin):
#     list_display = ("id" , "user", "active_bool","title" , "desc" , "starting_bid" , "image_url" , "category")

# class watchl(admin.ModelAdmin):
#     list_display = ("id", "watch_list" , "user")

# class bds(admin.ModelAdmin):
#     list_display = ("id","user","listingid","bid")

# class comme(admin.ModelAdmin):
#     list_display = ("id","user", "comment", "listingid")

# class win(admin.ModelAdmin):
#     list_display = ("id","user", "bid_win_list")

# Register your models here.
admin.site.register(auctionlist, )
admin.site.register(bids, )
admin.site.register(comments, )
admin.site.register(watchlist, )
admin.site.register(winner, )