from django.contrib import admin

from orders_app.models import Device, Customer, DeviceInField, Order


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


@admin.register(DeviceInField)
class DeviceInFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'customer', 'analyzer', 'owner_status')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')
