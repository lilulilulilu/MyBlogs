# build docker image
docker build -t mcp-server .
docker run -d -p 8002:8002 mcp-server
docker ps