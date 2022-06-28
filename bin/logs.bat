@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

docker-compose -f bin/docker/docker-compose.yml logs --follow --tail 250 assessment_a7_django assessment_a7_celery