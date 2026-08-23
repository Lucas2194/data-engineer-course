from json_utils import normalize_status

def count_values(values):
    new_dict = {}

    for value in values:
        current_value = new_dict.get(value, 0)
        new_dict[value] = current_value + 1

    return new_dict

def count_orders_by_status(orders):

    new_dict = {}

    for order in orders:
        status = normalize_status(order.get("status", "unknown"))
        if not status:
            status = "unknown"           
        current_value = new_dict.get(status, 0)
        new_dict[status] = current_value + 1 

    return new_dict 

def sum_orders_by_status(orders):

    sum_by_status = {}
    
    for order in orders:
        status = normalize_status(order.get("status", "unknown"))
        total_amount = order.get("total_amount", 0)
        if not status:
            status = "unknown"
        current_value = sum_by_status.get(status, 0)
        sum_by_status[status] = current_value + total_amount

    return sum_by_status

def count_delivery_methods(orders):
    methods = {}

    for order in orders:
        delivery = order.get("delivery")

        if delivery is None:
            method = "missing"
        else:
            method = normalize_status(delivery.get("method", "missing"))

        if not method:
            method = "missing"
        current_value = methods.get(method, 0)
        methods[method] = current_value + 1

    return methods

def counts_tags(orders):

    tag_counts = {}

    for order in orders:
        order_tags = order.get("tags", [])
        for tag in order_tags:
            current_value = tag_counts.get(tag, 0)
            tag_counts[tag] = current_value + 1
    return tag_counts

    