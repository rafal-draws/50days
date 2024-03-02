# CKAD Exam Excersies

- **20% Application Design and Build** (*Containers, Pods and Namespaces, Jobs and CronJobs, Volumes, Multi-Container Pods, Labels and Annotations*)

- **20% Application Deployment** (*Deployments, Deployment Strategies*)

- **15% Application Observability and Maintenance** (*API Deprecations, Container Probes, Troubleshooting Pods*)

- **25% Application Environment, Configuration and Security** (*Custom Resource Definitions, Authentication & Authorization, Resource Requirements, Limits&Quotas, ConfigMaps & Secrets, Security Contexts*)

- **20% Services & Networking** (*Services, Ingresses Network Policies*)

### General useful commands

echo "alias k=kubectl" >> ~./bashrc && source ~/.bashrc
k config --set-context --current --namespace=*namespace*|default
k config view --minify

k get pods,pv,pvc,hpa [-n *namespace*]

# Application Design and Build

## Pods

### Useful commands
k describe pod *pod-name*
k logs *pod-name* [-f]
k exec -it *pod-name* -- /bin/sh


Pods statuses Pending - Running - Succeeded (terminated succesfully) | Failed (terminated, at least one with an error)

#### Pod advanced commands
> k exec *pod-name* -- env renders env variables
> k run *pod-name* --image=busybox:1.36.1 --rm -it --restart=Never -- env **runs a pod, --rm flag automatically deletes the Pod after running the command**
> k run *pod-name* --image=busybox:1.36.1 --rm -it --restart=Never -- wget 172.17.0.4:80 **runs a pod, wget, removes the pod**
> k run *pod-name* --image=busybox:1.36.1 -o yaml --dry-run=client > pod.yaml -- /bin/sh -c "while true; do date; sleep 10; done" **-o yaml --dry-run=client outputs a yaml without provisioning to the cluster. The /bin/sh -c "command" replaces ENTRYPOINT in the image** 
> k run *pod-name* --image=busybox:1.36.1 -o yaml --dry-run=client > pod.yaml 

#### Pod minimal manifest
```
apiVersion: v1
kind: Pod
metadata:
  name: *pod-name*
spec:
  containers:
  - image: busybox:1.36.1
    name: container-one
```

#### Pod maximal manifest
```
apiVersion: v1
kind: Pod
metadata:
  name: *pod-name*
spec:
  containers:
  - image: *image*
    name: *container-name*
    env:
    - name: *ENVIRONMENT_NAME*
      value: *env-value*
    - name: *ANOTHER_ENV_NAME*
      value: *another.env.value*
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo $RANDOM; sleep 10; done"]

```

## Jobs and CronJobs

spec.completions 
spec.parallelism
spec.backoffLimit - number of retries a Job attempts until finishes with exit code 0 (default 6)
spec.template.spec.restartPolicy: Pod has Always, Job has OnFailure or Never
if OnFailure, one container is reset until Exit 0
if Never, uses new containers every time until Exit 0


### Useful commands

> kubectl create job counter --image=nginx:1.25.1 -- /bin/sh -c 'counter=0; while [ $counter -lt 3 ]; do counter=$((counter+1)); echo "$counter"; sleep 3; done;' **creates a job - job.batch/counter created**

> kubectl create cronjob current-date --schedule="* * * * *" --image=nginx:1.25.1 -- /bin/sh -c 'echo "Current date: $(date)"'

### Job Minimal manifest
```
apiVersion: batch/v1
kind: Job
metadata:
  name: counter
spec:
  template:
    spec:
      containers:
      - name: <container-name>
        image:  <image-name:version>
        command:
        - /bin/sh
        - -c
        - counter=0; while [ $counter -lt 3]; do counter=$((counter+1)); \
          echo "$counter"; sleep 3; done;
      restartPolicy: Never 
```

### CronJob 



