# Networking Basic For Cloud Computing

## Virtual Private Cloud (VPC)

- A VPC is a logically isolated section of a cloud provider's network where you can deploy cloud resources like servers and databases.
- It allows you to control network settings such as IP address ranges, subnets, route tables, and internet gateways.

 ## Subnets
A subnet is a segmented part of the VPC network where you can deploy cloud resources.
Subnets can be public (accessible from the internet) or private (isolated from public internet traffic).
## Internet Gateway (IGW)
An Internet Gateway allows resources within your VPC to access the internet and enables internet-based communication with your cloud infrastructure.
## Network Address Translation (NAT) Gateway
NAT Gateway allows instances in a private subnet to access the internet while preventing the internet from initiating connections back to those instances.
## Security Groups
Security Groups act as virtual firewalls for your cloud resources. They control inbound and outbound traffic at the instance level by allowing or denying specific types of traffic.
## Network Access Control List (ACL)
Network ACLs are another layer of security for VPC subnets. They control traffic entering and leaving a subnet, providing a broader scope of network traffic filtering than security groups.
## Elastic Load Balancer (ELB)
Load Balancers distribute incoming traffic across multiple instances to ensure high availability and fault tolerance.
## PrivateLink / VPC Peering
- `PrivateLink` enables secure communication between VPCs or with on-premise systems without traversing the public internet.
- `VPC Peering` allows communication between VPCs across regions or within the same region by creating a direct network link.
## Route Tables
Route Tables define how traffic is directed within your VPC. They are used to route traffic between subnets, the internet gateway, and NAT devices.
## DNS (Domain Name System)
DNS is responsible for translating domain names into IP addresses. In cloud environments, services like Amazon Route 53 manage DNS for your applications.
## Elastic IP
Elastic IP is a static public IP address that you can associate with your cloud resources, ensuring consistent IPs even if the instance is stopped or restarted.
## Direct Connect
Direct Connect establishes a dedicated network connection from your on-premise infrastructure to the cloud provider, providing more reliable and secure connectivity than standard internet connections.
## Virtual Network Interface (ENI)
An Elastic Network Interface (ENI) is a logical network interface that you can attach to an instance in your VPC, allowing you to manage network interfaces separately from the lifecycle of instances.
