source ./.env
service_path=$(pwd)
cd ../../
root_path=$(pwd)
echo "build ${REGISTRY}/${NAMESPACE}/${SERVICE}:${VERSION}"
service="."${service_path#${root_path}}
docker build -t ${REGISTRY}/${NAMESPACE}/${SERVICE}:${VERSION} --build-arg MAIN=${service} -f ./Dockerfile .
