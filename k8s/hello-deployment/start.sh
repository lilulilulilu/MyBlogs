# deploy in minikube
brew install minikube
brew install kubectl
minikube start
minikube image load hello:v2
kubectl apply -f deployment.yaml 
kubectl get pods
kubectl describe pod hello-5df56cd977-7xm2v
kubectl get pods --show-labels
kubectl get deployments
kubectl describe service hello-svc 
minikube service hello-svc --url