k8s , is an open source system for automating, deployment, scaling and management of containerized applications.

container app:
    scaled
    automate
    health
    deploy

architecture of kubernetes
==========================
    kubernetes master
        api server: 
            kube API sever interacts with API, it is a frontend of the kubernetes control panel.
        control manager:
            controller manager runs the controllers in background which runs different tasks in cluster
        scheduler:
            scheduler watches the pods and assigns the pod to run on specific hosts.
        etcd:
            a simple distribute key value database to store kubernetes cluster data.
            ex:
                job scheduling information, pods, state information and etc.
        webUI:
            web based k8s user interface. you can use dashboard to deploy containerized applications to a kubernetes cluster, troubleshoot your containerized applications, and manage the cluster itself along with its attendant resources.
        kubectl:
            kubectl is a command line configuration(CLI) for k8s used to interact with master node of k8s. k8s has a config file called kubeconfig, this file has the information about server and authentication information to access the API server
        kubelet:
            kubelet is the primary node agent runs on each nodes adn reads the container manifest which ensures that containers are running and healthy
        nodes:

        pods:
            it's a logical collection of containers that belong to an applications
            a pod is the smallest deployable unit
            it can be created, scheduled, and managed
            each resource in k8s is defined using a configuration file
        deployments
        services