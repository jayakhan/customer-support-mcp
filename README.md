# Customer Support Agent MCP Server

**Welcome! This project is a fully functional **Model Context Protocol (MCP)** server designed to help build your **Agentic AI**.

Instead of creating a router file to manage your project, this MCP server enabled application gives any MCP compatibale AI client to act as an autonomous Customer Support Agent. It can read databases, check inventory, and even enforce company refund in real time. 

## Architecture: How it Works

```mermaid
sequenceDiagram
    participant U as User (Human)
    participant C as AI Client (Cline / Claude / Cursor)
    participant M as MCP Protocol (stdio)
    participant P as Python MCP Server (Customer Support)
    participant DB as Mock Database

    U->>C: "Can I get a refund for ORD-102?"
    Note over C: AI realizes it needs to check the order.
    C->>M: Request: Call `get_order_details("ORD_102")`
    M->>P: Executes python function
    P->>DB: Reads local dictionary
    DB->>P: Returns order details (Refundable: False)
    P->>M: Returns data to AI
    M->>C: Data received
    Note over C: AI sees the item is past the 30-day window.
    C->>U: "I'm sorry, but ORD_102 is past our 30-day return window."