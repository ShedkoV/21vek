

redis: Redis: docker run --name redis -e ALLOW_EMPTY_PASSWORD=yes -p 6379:6379 bitnami/redis:latest
docker compose -f src/tools/docker-compose.yaml up -d
