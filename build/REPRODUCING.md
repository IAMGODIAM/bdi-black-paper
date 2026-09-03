# Reproducing the print edition

The PDF in `final/` is a deterministic function of the manuscript sources in `drafts/`,
the stylesheet `final/print.css`, the build script `final/build.py`, and the pinned
toolchain in `build/Dockerfile`. Two independent runs of the container on the same
commit produce byte-identical PDFs, so the SHA-256 recorded in
`final/The_Measure_of_the_Wound.pdf.sha256` is a verifiable property of the commit,
not of the machine that happened to build it.

## Procedure

    git clone https://github.com/IAMGODIAM/bdi-black-paper.git
    cd bdi-black-paper
    ./build/rebuild.sh            # Linux / macOS
    .\build\rebuild.ps1           # Windows (Docker Desktop)

or, without the wrapper:

    docker build -f build/Dockerfile -t mow-build .
    docker run --rm -v "$PWD:/work" mow-build

Expected console output ends with `pages: 90` and a `sha256:` line equal to the
contents of `final/The_Measure_of_the_Wound.pdf.sha256`. Pass `--no-pdf` to produce
the HTML only.

## What makes the build deterministic

* PDF `/CreationDate` and `/ModDate` come from `<meta name="dcterms.created|modified">`
  tags that `build.py` sets to the fixed `BUILD_STAMP`.
* fontTools stamps every subset font with the current time unless `SOURCE_DATE_EPOCH`
  is set; `build.py` pins it to `BUILD_STAMP`.
* The PDF trailer `/ID` is an MD5 of the file content (pydyf), so it follows from the above.
* Fonts are taken from Debian/Ubuntu packages at pinned distribution versions
  (Bitstream Charter from `xfonts-scalable`; DejaVu Sans from `fonts-dejavu-core` and
  `fonts-dejavu-extra`), and every Python wheel is pinned in `build/requirements.txt`.

## Without Docker

Any Ubuntu 24.04 host with the packages named in the Dockerfile and
`pip install -r build/requirements.txt` will reproduce the same bytes. Other platforms
will produce a visually identical document whose hash may differ, because Pango,
HarfBuzz and the font files differ; the page count (90) and text content should not.

## Scope of the guarantee

The image installs its distribution packages by name, not by pinned version, so an image
built much later may pull newer Pango, HarfBuzz or font builds and produce a different
hash. The guarantee is therefore precise but bounded: any two builds from the *same*
image are byte-identical — verified by two independent runs on the machine that produced
this edition — and the hash in `final/The_Measure_of_the_Wound.pdf.sha256` is the one the
image produced as built on 2026-09-03. A later rebuild that yields a different hash is
evidence of a changed toolchain, not of changed content; confirm by comparing the page
count (90) and the extracted text, both of which are fixed by the sources.
