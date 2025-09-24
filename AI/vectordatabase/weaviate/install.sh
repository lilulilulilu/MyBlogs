# [install weaviate in kubernetes](https://docs.weaviate.io/deploy/installation-guides/k8s-installation)

helm show values weaviate/weaviate > values.yaml

helm upgrade --install "weaviate" weaviate/weaviate --namespace "weaviate" --values ./values.yaml

kubectl get pods -n weaviate
kubectl get svc -n weaviate
kubectl get pvc -n weaviate
kubectl get svc weaviate -n weaviate -o jsonpath='{.spec.ports[0].nodePort}'

curl http://localhost:31803/v1/meta


kubectl port-forward svc/weaviate 8080:80 -n weaviate
nohup kubectl port-forward svc/weaviate 8080:80 -n weaviate > port-forward.log 2>&1 &
curl http://localhost:8080/v1/meta


# 启动weaviate-ui (使用社区维护的UI镜像)
docker pull naaive/weaviate-ui:latest
docker run -e WEAVIATE_URL=http://host.docker.internal:8080 -p 3000:7777 -itd --name weaviate-ui naaive/weaviate-ui:latest

# 访问UI: http://localhost:3000


