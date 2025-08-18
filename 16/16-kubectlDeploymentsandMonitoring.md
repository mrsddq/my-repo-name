# prerequesite
kind --version
kubectl --version

# create cluster
kind create cluster --name main-k8s-cluster

# to get nodes
kubectl get nodes

# to get pods
kubectl get pods

# to get deployments
kubectl get deployments

# to describe the pods
kubectl describe pod <pod-id>

# to delete services
kubectl delete svc <service-name>

# interactive shell access to a running pod (1 container case)
kubectl exec --stdin --tty my-pod -- /bin/sh        
