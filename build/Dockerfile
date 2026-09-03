# Reproducible build environment for The Measure of the Wound (print edition).
#
# Pins the environment in which the v1.4 Submission Edition PDF was produced:
#   Ubuntu 24.04  |  Pango 1.52  |  HarfBuzz 8.3  |  fontconfig 2.15
#   Bitstream Charter (xfonts-scalable)  |  DejaVu Sans (fonts-dejavu-core, fonts-dejavu-extra)
#   WeasyPrint 69.0  |  Python-Markdown 3.10.2  |  see build/requirements.txt for every wheel
#
# Build the image from the repository root, then run it with the repository mounted at /work:
#   docker build -f build/Dockerfile -t mow-build .
#   docker run --rm -v "$PWD:/work" mow-build
# Outputs (manuscript repo): final/measure_of_the_wound.html, final/The_Measure_of_the_Wound.pdf, final/The_Measure_of_the_Wound.pdf.sha256
# Outputs (publication package, build/build.py + manuscript/): the same three files at the package root
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip \
      libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libharfbuzz-subset0 libffi8 fontconfig \
      fonts-dejavu-core fonts-dejavu-extra xfonts-scalable ca-certificates \
    && rm -rf /var/lib/apt/lists/* && fc-cache -f
COPY build/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir --break-system-packages -r /tmp/requirements.txt
RUN printf '#!/bin/sh\nset -e\nfor f in final/build.py build/build.py; do [ -f "$f" ] && exec python3 "$f" "$@"; done\necho "build.py not found under /work" >&2; exit 1\n' > /usr/local/bin/mow-build && chmod +x /usr/local/bin/mow-build
WORKDIR /work
ENTRYPOINT ["/usr/local/bin/mow-build"]
