# KubeflowAMIConfiguration

# kubeflow
    kubeflow is a free and open-source platform for machine learning on k8s. the kubeflow project has multiple distinct software components which each address specific stages of the machine learning lifecycle, including model development, model training, model serving, and automated machine learning.

# what is kubeflow?
    kubeflow project is dedicated to making deployments of machine learning (ML) workflows on kubernetes simple, portable and scalable. our goal is not to recreate other services, but to provide a straightforward way to deploy best-to-breed open-source systems for ML to diverse infrastructures.

    anywhere you are running k8s, you should be able to run kubeflow.

aws - ami
azure - azure mi
gcp - google images

app + bin + runtime -> container

container engine (CE)

# ml lifecycle
    data prepration
    model development
    model training
    model endpoint/serving

# kubeflow components
    pipelines
        kubeflow pipelines (KFP) is a platform for building then deploying portable and scalable machine learning workflowsusing kubernetes.
    
    notebooks
        kubeflow notebooks let you run web based development environments on your k8s cluster by running them inside pods
    
    dashboards
        kubeflow central dashborad is our hub which connects the authenticated web interfaces of kubeflow and other ecosystem components

dev -> github -> jenkins -> deployment -> EKS (AWS)
yaml (deployment)
python (model development)
