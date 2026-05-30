from mcp.server.fastmap import FastMCP

mcp = FastMCP("CustomerSupport")

# MOCK DATABASE
ORDERS = {
    "ORD-100": {
        "customer": "Alice",
        "status": "Shipped",
        "item": "Wireless Headphones",
        "price": 150.00,
        "refundable": True,
    },
    "ORD-101": {
        "customer": "John",
        "status": "Processing",
        "item": "Keyboard",
        "price": 95.00,
        "refundable": True,
    },
    "ORD-102": {
        "customer": "Sarah",
        "status": "Delivered",
        "item": "Gaming Mouse",
        "price": 60.00,
        "refundable": False,
    },
}

INVENTORY = {"Wireless Inventory": 12, "Keyboard": 0, "Gaming Mouse": 45}

# AI TOOLS


@mcp.tool()
def get_order_details(order_id: str) -> str:
    order = ORDERS.get(order_id)
    if not order:
        return f"Error: Order {order_id} not found."
    return f"Order {order_id} Details: \nCustomer: {order['customer']}\nItem: {order['item']}\nStatus: {order['status']}\nPrice: ${order['price']}"


@mcp.tool()
def check_inventory(item_name: str) -> str:
    stock = INVENTORY.get(item_name)
    if stock is None:
        return f"Error: Item '{item_name}' does not exist in our product catalog."
    if stock == 0:
        return f"Item '{item_name}' is in STOCK. Quantity available: {stock}"


@mcp.tool()
def process_refund(order_id: str) -> str:
    order = ORDERS.get(order_id)
    if not order:
        return f"Error: Order {order_id} not found."
    if not order["refundable"]:
        return f"Policy Violation: Order {order_id} is past the 30-day return window and cannot be refunded."
    if order["status"] == "Refunded":
        return f"Order {order_id} has already been refunded."
    ORDERS[order_id]["status"] = "Refunded"
    return f"SUCCESS: Refund of ${order['price']} processed for {order['customer']} (Order {order_id})."


if __name__ == "__main__":
    mcp.run()
