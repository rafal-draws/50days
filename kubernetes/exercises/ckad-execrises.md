# Exersises from @dgkanatsios on github
### https://github.com/dgkanatsios/CKAD-exercises/blob/main/a.core_concepts.md
## Core concepts - 13%


###Create a namespace called 'mynamespace' and a pod with image nginx called nginx on this namespace

### Create the pod that was just described using YAML

### Create a busybox pod (using kubectl command) that runs the command "env". Run it and see the output

### Create a busybox pod (using YAML) that runs the command "env". Run it and see the output

### Get the YAML for a new namespace called 'myns' without creating it

### Create the YAML for a new ResourceQuota called 'myrq' with hard limits of 1 CPU, 1G memory and 2 pods without creating it

### Get pods on all namespaces

### Create a pod with image nginx called nginx and expose traffic on port 80

### Change pod's image to nginx:1.7.1. Observe that the container will be restarted as soon as the image gets pulled

### Get nginx pod's ip created in previous step, use a temp busybox image to wget its '/'

###Get pod's YAML

###Get information about the pod, including details about potential issues (e.g. pod hasn't started)

###Get pod logs

### If pod crashed and restarted, get logs about the previous instance

### Execute a simple shell on the nginx pod

### Create a busybox pod that echoes 'hello world' and then exits

### Do the same, but have the pod deleted automatically when it's completed


### Create an nginx pod and set an env value as 'var1=val1'. Check the env value existence within the pod

## Multi-Container Pods - 10%

### Create a Pod with two containers, both with image busybox and command "echo hello; sleep 3600". Connect to the second container and run 'ls'

### Create a pod with an nginx container exposed on port 80. Add a busybox init container which downloads a page using "wget -O /work-dir/index.html http://neverssl.com/online". Make a volume of type emptyDir and mount it in both containers. For the nginx container, mount it on "/usr/share/nginx/html" and for the initcontainer, mount it on "/work-dir". When done, get the IP of the created pod and create a busybox pod and run "wget -O- IP"


## Pod Design - 20%

### Create 3 pods with names nginx1,nginx2,nginx3. All of them should have the label app=v1

###Show all labels of the pods

### Change the labels of pod 'nginx2' to be app=v2

### Get the label 'app' for the pods (show a column with APP labels)

### Get only the 'app=v2' pods

### Add a new label tier=web to all pods having 'app=v2' or 'app=v1' labels

### Add an annotation 'owner: marketing' to all pods having 'app=v2' label

### Remove the 'app' label from the pods we created before

### Annotate pods nginx1, nginx2, nginx3 with "description='my description'" value

### Check the annotations for pod nginx1

### Remove the annotations for these three pods

### Remove these pods to have a clean state in your cluster

### Create a pod that will be deployed to a Node that has the label 'accelerator=nvidia-tesla-p100'

### Taint a node with key tier and value frontend with the effect NoSchedule. Then, create a pod that tolerates this taint.

### Create a pod that will be placed on node controlplane. Use nodeSelector and tolerations.

### Create a deployment with image nginx:1.18.0, called nginx, having 2 replicas, defining port 80 as the port that this container exposes (don't create a service for this deployment)

### View the YAML of this deployment

### View the YAML of the replica set that was created by this deployment

### Get the YAML for one of the pods

### Check how the deployment rollout is going

### Update the nginx image to nginx:1.19.8

### Check the rollout history and confirm that the replicas are OK

### Undo the latest rollout and verify that new pods have the old image (nginx:1.18.0)

### Do an on purpose update of the deployment with a wrong image nginx:1.91

### Verify that something's wrong with the rollout

### Return the deployment to the second revision (number 2) and verify the image is nginx:1.19.8

### Check the details of the fourth revision (number 4)

### Scale the deployment to 5 replicas

### Autoscale the deployment, pods between 5 and 10, targetting CPU utilization at 80%

### Pause the rollout of the deployment

### Update the image to nginx:1.19.9 and check that there's nothing going on, since we paused the rollout

### Resume the rollout and check that the nginx:1.19.9 image has been applied

### Delete the deployment and the horizontal pod autoscaler you created

### Implement canary deployment by running two instances of nginx marked as version=v1 and version=v2 so that the load is balanced at 75%-25% ratio


### Create a job named pi with image perl:5.34 that runs the command with arguments "perl -Mbignum=bpi -wle 'print bpi(2000)'"

#### Wait till it's done, get the output

### Create a job with the image busybox that executes the command 'echo hello;sleep 30;echo world'

### Follow the logs for the pod (you'll wait for 30 seconds)

### See the status of the job, describe it and see the logs

### Delete the job

### Create a job but ensure that it will be automatically terminated by kubernetes if it takes more than 30 seconds to execute

### Create the same job, make it run 5 times, one after the other. Verify its status and delete it

### Create the same job, but make it run 5 parallel times


### Create a cron job with image busybox that runs on a schedule of "*/1 * * * *" and writes 'date; echo Hello from the Kubernetes cluster' to standard output

### See its logs and delete it

### Create the same cron job again, and watch the status. Once it ran, check which job ran by the created cron job. Check the log, and delete the cron job

### Create a cron job with image busybox that runs every minute and writes 'date; echo Hello from the Kubernetes cluster' to standard output. The cron job should be terminated if it takes more than 17 seconds to start execution after its scheduled time (i.e. the job missed its scheduled time).

### Create a cron job with image busybox that runs every minute and writes 'date; echo Hello from the Kubernetes cluster' to standard output. The cron job should be terminated if it successfully starts but takes more than 12 seconds to complete execution.


### Create a job from cronjob.
