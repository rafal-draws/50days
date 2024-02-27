# Services

Services provide discoverable names and load balancing to a set of Pods.
The Service remains agnostic from IP addresses with the help of Kubernetes DNS
control plane component. 

It can be discovered by DNS lookup.


Incoming traffic -> Service with spec.selector: tier:frontend -> Pods with metadata.labels: tier:frontend only


Service Types for CKAD
ClusterIP - exposes cluster internal IP only
NodePort - exposes IP address of the node at static port 
LoadBalancer - Exposes the Service externally by clouds provider LB

