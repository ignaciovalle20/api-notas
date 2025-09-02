#!/bin/bash

echo "🚀 Desplegando API de Notas en Kubernetes..."

# Construir la imagen Docker
echo "📦 Construyendo imagen Docker..."
docker build -t api-notas:latest .

# Si estás usando minikube, cargar la imagen
if command -v minikube &> /dev/null; then
    echo "🔄 Cargando imagen en minikube..."
    minikube image load api-notas:latest
fi

# Aplicar el manifest
echo "☸️ Aplicando manifests de Kubernetes..."
kubectl apply -f api-notas-k8s.yaml

# Esperar a que los pods estén listos
echo "⏳ Esperando a que los pods estén listos..."
kubectl wait --for=condition=ready pod -l app=api-notas --timeout=300s

# Mostrar el estado
echo "📊 Estado del deployment:"
kubectl get deployments -l app=api-notas
kubectl get pods -l app=api-notas

echo ""
echo "✅ Deployment completado!"
echo ""
echo "🔌 Para acceder a cada instancia, usa port-forward:"
echo ""
echo "  # Obtener nombres de los pods:"
echo "  kubectl get pods -l app=api-notas"
echo ""
echo "  # Port-forward a cada instancia:"
echo "  kubectl port-forward pod/api-notas-instance1-XXXXX 8001:8000"
echo "  kubectl port-forward pod/api-notas-instance2-XXXXX 8002:8000"
echo "  kubectl port-forward pod/api-notas-instance3-XXXXX 8003:8000"
echo ""
echo "🧪 Luego probar:"
echo "  curl http://localhost:8001/  # Instancia 1"
echo "  curl http://localhost:8002/  # Instancia 2"
echo "  curl http://localhost:8003/  # Instancia 3"
