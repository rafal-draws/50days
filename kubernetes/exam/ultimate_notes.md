# CKAD Exam Excersies

- **20% Application Design and Build** (*Containers, Pods and Namespaces, Jobs and CronJobs, Volumes, Multi-Container Pods, Labels and Annotations*)

- **20% Application Deployment** (*Deployments, Deployment Strategies*)

- **15% Application Observability and Maintenance** (*API Deprecations, Container Probes, Troubleshooting Pods*)

- **25% Application Environment, Configuration and Security** (*Custom Resource Definitions, Authentication & Authorization, Resource Requirements, Limits&Quotas, ConfigMaps & Secrets, Security Contexts*)

- **20% Services & Networking** (*Services, Ingresses Network Policies*)

### General useful commands

echo "alias k=kubectl" >> ~./bashrc && source ~/.bashrc
k config --set-context --current --namespace=<nspcName>|default
k config view --minify

k get pods,pv,pvc,hpa


# 

## Pods

### useful commands
k describe pods <pod-name>
k logs <pod-name>
k exec -it <pod-name> -- /bin/sh


Pods statuses Pending -> Running -> Succeeded (terminated succesfully) | Failed (terminated, at least one with an error)

#### Pod advanced commands
k exec <pod-name> -- env *renders env variables*
k run <pod-name> --image=busybox:1.36.1 --rm -it --restart=Never -- env *runs a pod, --rm flag automatically deletes the Pod after running the command*
k run <pod-name> --image=busybox:1.36.1 --rm -it --restart=Never -- wget 172.17.0.4:80 *runs a pod, wget, removes*

#### Pod minimal manifest
apiVersion: v1
kind: Pod
metadata:
  name: <podName>
spec:
  containers:
  - image: busybox:1.36.1
    name: container-one

#### Pod maximal manifest
apiVersion: v1
kind: Pod
metadata:
  name: <podName>
spec:
