#!/usr/bin/env sh
# Rebuild the print edition inside the pinned container. Run from anywhere; needs Docker.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
docker build -q -f "$ROOT/build/Dockerfile" -t mow-build "$ROOT"
docker run --rm -v "$ROOT:/work" mow-build "$@"
cat "$ROOT/final/The_Measure_of_the_Wound.pdf.sha256" 2>/dev/null || cat "$ROOT/The_Measure_of_the_Wound.pdf.sha256"
