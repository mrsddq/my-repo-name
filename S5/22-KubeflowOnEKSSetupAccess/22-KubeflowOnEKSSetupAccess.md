# KubeflowOnEKSSetupAccess

    EKS: Elastic Kubernetes Service

wget -0 - https://github.com/kubeflow/kfp-tekton/tarball/64bf7dba3601a8e8f2f16c4fef169d796ab1428d | tar zxf - && cd kubeflow-kfp-tekton-64bf7db

kubectl apply -k "manifests/kustomize/cluster-scoped-resources"
kubectl wait "crd/applications.app.k8s.io" -- for "condition=established" -- timeout "60s"
kubectl apply -k "manifests/kustomize/env/platform-agnostic-kind"
kubectl wait pods -1 "application-crd-id=kubeflow-pipelines" -n kubeflow -- for "condition=Ready" -- timeout "1800s"
