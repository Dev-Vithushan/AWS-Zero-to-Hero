# AWS EventBridge

`Amazon EventBridge` is a serverless event bus service that enables you to connect different applications using events. It helps build event-driven architectures by allowing you to route, filter, and process events from various sources (such as AWS services, SaaS applications, or custom applications) and trigger actions in target services based on the events.

## Key Features of Amazon EventBridge:


`Event-Driven Architecture:` EventBridge allows your application to respond in real time to events from a variety of sources, such as changes in data, system state, or user activity.

`Event Sources:` EventBridge integrates with a wide range of event sources:

- AWS services (e.g., S3, Lambda, DynamoDB, EC2, etc.)
- Custom applications that publish their own events to EventBridge
- SaaS applications (e.g., Shopify, Zendesk, Datadog, and more)

`Event Buses:` EventBridge uses event buses to route events. There are three types of event buses:

- **Default Event Bus:** Automatically available to route AWS events.
- **Custom Event Buses:** Created for routing custom events from applications.
- **Partner Event Buses:** Integrates with SaaS providers to receive and process their events.