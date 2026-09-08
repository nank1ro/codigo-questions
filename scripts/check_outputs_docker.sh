#!/bin/sh
# Run scripts/check_outputs.py inside the production-version codecompiler container.
# usage: scripts/check_outputs_docker.sh 'en/python/sets/*.md' [...]
set -e
C=${CODECOMPILER_CONTAINER:-codecompiler-8081}
D=$(docker exec "$C" mktemp -d /tmp/co.XXXXXX)
trap 'docker exec "$C" rm -rf "$D"' EXIT
docker exec "$C" mkdir -p "$D/scripts"
docker cp scripts/check_outputs.py "$C:$D/scripts/"
for p in "$@"; do
  d=$(dirname "$p")
  docker exec "$C" mkdir -p "$D/$d"
  docker cp "$d/." "$C:$D/$d"
done
docker exec -w "$D" "$C" python3 scripts/check_outputs.py "$@"
