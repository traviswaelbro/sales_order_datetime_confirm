# Sales Order Datetime Confirm

_sales_order_datetime_confirm converts the standard ```date_confirm``` field from a simple Date field to a Date time field. 

This allows much more specific tracking of order details and is especially useful when you have quotes being confirmed days or weeks after they were created.

##### To Do:

- Test in default instance
- Rewrite in v8 API?
- Add view changes
  - Display ```date_confirm``` on _sale order_ form (instead of ```date_create```) when ```state = done```
  - Display ```date_confirm``` on _sale order_ tree (instead of ```date_create```)
