"""Build the print edition of *The Measure of the Wound*.

Deterministic build: run from any working directory.

    python3 final/build.py            # writes final/measure_of_the_wound.html and final/The_Measure_of_the_Wound.pdf
    python3 final/build.py --no-pdf   # HTML only

Manuscript sources are read from ../drafts/ (manuscript repository; outputs to final/),
else ../manuscript/ (publication package; outputs to the package root), else the
directory containing this script (flat layout).
PDF metadata dates are fixed (BUILD_STAMP) so that identical sources, library
versions and fonts yield a byte-identical PDF; see build/Dockerfile for the
pinned environment and build/REPRODUCING.md for the procedure.
"""
import markdown, re, pathlib, sys, hashlib, os, datetime

HERE   = pathlib.Path(__file__).resolve().parent
ROOT   = HERE.parent
# Two layouts are supported: the manuscript repository (drafts/ -> final/) and the
# publication package (manuscript/ -> package root).
if (ROOT / 'drafts').is_dir():
    DRAFTS, OUT = ROOT / 'drafts', HERE
elif (ROOT / 'manuscript').is_dir():
    DRAFTS, OUT = ROOT / 'manuscript', ROOT
else:
    DRAFTS, OUT = HERE, HERE
EDITION_DATE = "September 2026"
BUILD_STAMP  = "2026-09-03T00:00:00Z"   # fixed for reproducible PDF metadata
# fontTools stamps every subset font with the current time unless SOURCE_DATE_EPOCH is set;
# pin it to BUILD_STAMP so the embedded fonts, and therefore the PDF, are byte-identical across runs.
os.environ.setdefault("SOURCE_DATE_EPOCH", str(int(datetime.datetime.fromisoformat(BUILD_STAMP.replace("Z","+00:00")).timestamp())))

MD = markdown.Markdown(extensions=['tables','attr_list','md_in_html'])

FRONT = """
<section class="titlepage">
  <div class="tp-rule"></div>
  <p class="tp-pub">E5 ENCLAVE INCORPORATED</p>
  <h1 class="tp-title">The Measure<br/>of the Wound</h1>
  <p class="tp-sub">A Sovereign Empirical Record of<br/>Black American Structural Distress</p>
  <p class="tp-dates">1991&#8202;&ndash;&#8202;2024</p>
  <div class="tp-rule"></div>
  <p class="tp-author">Israel Lee Armstead</p>
  <p class="tp-affil">E5 Enclave Incorporated &middot; Liberty City, Miami, Florida</p>
  <p class="tp-ed">Corrected Print Edition &middot; Black Paper v1.4 &middot; Submission Edition</p>
</section>

<section class="copyright">
  <p><strong>The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991&ndash;2024</strong></p>
  <p>Corrected Print Edition &middot; Black Paper v1.4 &middot; Submission Edition<br/>Published {date}</p>
  <p>E5 Enclave Incorporated<br/>820 NW 64th Street, Liberty City, Miami, Florida 33150<br/>EIN 99-3822441 &middot; UEI H8NGXEYE2HH8 &middot; CAGE 07E88<br/>e5enclave.com</p>
  <p class="cc"><strong>CC0 1.0 Universal &mdash; Public Domain Dedication.</strong> To the extent possible under law, E5 Enclave Incorporated has waived all copyright and related or neighboring rights to this work. No permission is required to copy, translate, adapt, excerpt or republish it, in whole or in part, for any purpose. No attribution is required, though it is appreciated.</p>
  <p><strong>Suggested citation.</strong> Armstead, Israel Lee. (2026). <em>The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991&ndash;2024.</em> Corrected Print Edition v1.4. E5 Enclave Incorporated. CC0 1.0 Universal. github.com/IAMGODIAM/measure-of-the-wound</p>
  <p><strong>Underlying data.</strong> All source data is public and openly licensed. Layer 1 raw evidence: <span class="mono">IAMGODIAM/bdi-raw-data-vault</span>. Layer 2 synthesized instrument: <span class="mono">IAMGODIAM/bdi-sovereign-dataset</span>, sealed on Base Mainnet, ExodusV4 token #2. Layer 3 place-level application: <span class="mono">IAMGODIAM/farmblock-data</span> and <span class="mono">IAMGODIAM/farmblock-dataset</span>.</p>
  <p><strong>On this edition.</strong> Every derived statistic was recomputed from the raw source series rather than carried forward from prior drafts, and flagged figures were re-verified against live federal sources in August 2026. Twenty-seven public claims were put through evidentiary triage; ten further arithmetic errors were found by recomputation; three canonical counts in the project&rsquo;s own governance documents were found stale. This edition then incorporates a second wave of corrections arising from an independent review of the v1.1 print edition (September 1, 2026), which identified a defective price basis in the Chapter 5 wealth series and an unverified denominator in the incarceration series. Both are corrected; several claims are withdrawn. All corrections are enumerated in Appendix H, sections A, B and B2. The Submission Edition (v1.3) added an abstract, an author of record, an AI-assistance disclosure, keywords and JEL codes, and a consolidated References section. This edition (v1.4) states the FarmBlock reproducibility limit in Chapter 7 where the index is introduced rather than in the appendix alone, and rewrites the AI disclosure to describe the division of labor exactly rather than approximately. Neither edition changes any finding.</p>
  <p class="motto"><em>Nil satis nisi optimum.</em></p>
</section>


<section class="dedication">
  <p class="ded-label">Dedication</p>
  <p class="ded-open">I dedicate this work to the countless love warriors, wounded healers and freedom fighters who trod this path before me, in this moment in the movement for Black American Lives, Liberty, and Economic Parity.</p>
  <p>The work, the scholarship and the brotherhood of Professor Cornel &ldquo;Brother&rdquo; West provided invaluable wisdom and a wellspring of inspiration in this endeavor.</p>
  <p>To my late grand-uncle, Ralph C. McCartney &mdash; thank you for your instruction and your guidance. I carry forth the mantle of your work and your legacy in the struggle for Black Upliftment, and I carry it proudly.</p>
  <p>To my brilliant wife and willing editor, Elvia G. Brazil&#8209;Armstead &mdash; thank you for your heart, your hand and your pen.</p>
  <p>To the descendants of chattel-enslaved persons &mdash; the village, our community &mdash; may the record set down here bring nearer the repair that is owed you for the vestiges and the harms you have so long endured.</p>
  <p class="ded-close">I love you, All.</p>
  <p class="ded-sign"><span class="nm">&mdash; Israel Lee Armstead</span><span class="pl">Liberty City, Miami</span></p>
</section>

<section class="abstract-page">
  <h1 class="toc-h">Abstract</h1>
  <p class="abs">This paper assembles an eight-pillar empirical record of Black American structural disparity across the era of formal legal equality, 1991&ndash;2024, nested within federal series that reach to 1900 (health), 1925 (criminal justice), 1940 (housing), 1964 (political participation), 1972 (labor) and 1514 (the historical architecture). Drawing on approximately 14,811 raw observations from the Bureau of Labor Statistics, the Census Bureau, the National Center for Health Statistics, the Bureau of Justice Statistics, the Federal Reserve, the National Center for Education Statistics, the Consumer Financial Protection Bureau, the Department of Agriculture and the Slave Voyages Database, synthesized into 1,574 verified observations and applied to 15,507 census tracts in 49 cities, it documents a consistent pattern: absolute conditions improve while the ratio between Black and white outcomes holds or widens. In constant 2022 dollars, Black median family wealth rose 388 percent while the absolute wealth gap reached its widest point in the survey&rsquo;s history. The Black/white unemployment ratio has never inverted in fifty-four years. The maternal mortality ratio is higher in 2022 (2.61) than in 1930 (1.48). The imprisonment ratio moved 0.14 points across ninety-seven years. The homeownership gap is wider than when the Fair Housing Act was signed. The paper contributes a place-level composite index, prints its full corrections ledger as an appendix, publishes an independent verification review and the author&rsquo;s reply alongside the release, and places all data and code in the public domain under CC0.</p>
  <p class="abs-meta"><strong>Keywords:</strong> racial inequality; wealth gap; structural racism; Black Americans; longitudinal federal data; composite index; maternal mortality; incarceration; homeownership; open data</p>
  <p class="abs-meta"><strong>JEL codes:</strong> J15, D63, I14, I24, K42, R21, N32</p>
  <p class="abs-meta"><strong>Author of record.</strong> Israel Lee Armstead, Founder and Chairman of the Board, E5 Enclave Incorporated (EIN 99-3822441), 820 NW 64th Street, Miami, FL 33150. israel@e5enclave.com. The organization is the institutional publisher; responsibility for the content rests with the author.</p>
  <p class="abs-meta"><strong>Disclosure of AI assistance.</strong> This work used generative AI. Here is exactly where. The author wrote the prose. A human editor, Elvia G. Brazil&#8209;Armstead, read the draft and returned handwritten notes; Claude (Anthropic) then applied line edits against those notes and the author&rsquo;s instructions. Claude also did the arithmetic &mdash; pulling the series from federal sources the author had chosen, recomputing every derived statistic, and compiling the corrections ledger &mdash; and it built the typesetting pipeline. It originated no research question, selected no source, drew no conclusion and made no claim. The author specified each computation and checked each figure it returned against the primary series; where the two disagreed, the correction is printed in Appendix H. Manus AI performed an independent verification review of the v1.1 edition; that review and the author&rsquo;s reply are published in the project repository. No AI system is an author of this work and none is credited as one. Every numeric claim traces to a named federal or archival source in the References and in Appendix A.</p>
  <p class="abs-meta"><strong>Data and code availability.</strong> All source data, manuscript sources, the build pipeline, the recomputation log and the corrections ledger are public under CC0 1.0 in the publication package at github.com/IAMGODIAM/measure-of-the-wound, in the working repository at github.com/IAMGODIAM/bdi-black-paper, and in the four data repositories cited in Appendix F. The package carries a frozen snapshot of every source file the tables are computed from, with a SHA&#8209;256 manifest, and rebuilds the paper byte-for-byte from a pinned container. The FarmBlock Distress Index outputs are published but not yet independently reproducible from the released package; see Appendix E.4a.</p>
</section>

<section class="toc-page">
  <h1 class="toc-h">Contents</h1>
  <div class="toc">TOC_ITEMS</div>
</section>
"""

ORDER = [
 ("front",  None,          "00_PREFACE.md",   "Preface"),
 ("front",  None,          "01_INTRODUCTION.md","Introduction: The Wound"),
 ("part",   "Part One",    "The Tradition and the Gap", None),
 ("ch",     None,          "02_CHAPTERS_1_2.md", None),
 ("part",   "Part Two",    "The Data Architecture", None),
 ("ch",     None,          "03_CHAPTER_3_METHODOLOGY.md", None),
 ("ch",     None,          "04_CHAPTER_4_MEASURE.md", None),
 ("part",   "Part Three",  "The Findings", None),
 ("ch",     None,          "05_CHAPTER_5_ECONOMIC.md", None),
 ("ch",     None,          "06_CHAPTER_6_HEALTH_JUSTICE_EDUCATION.md", None),
 ("ch",     None,          "07_CHAPTER_7_COMPOUND.md", None),
 ("part",   "Part Four",   "The Argument", None),
 ("ch",     None,          "08_CHAPTER_8_POLICY.md", None),
 ("front",  None,          "09_CONCLUSION.md", "Conclusion"),
 ("back",   None,          "11_REFERENCES.md", "References"),
 ("back",   None,          "10_APPENDICES.md", "Appendices"),
]

body=[]; toc=[]; n=0
SMALL={'a','an','the','and','but','or','nor','of','in','on','at','to','for','from',
       'by','with','as','it','its','that','than','over','into'}
def tcase(s):
    w=s.strip().split(); out=[]
    for i,x in enumerate(w):
        core=re.sub(r'[^A-Za-z]','',x)
        # preserve genuine acronyms (short, all-caps in source, not common words)
        if core and core.isupper() and len(core)<=4 and core.lower() not in SMALL and core not in ('WOUND','DATA','WHAT','WHY','THE','HOW','GETS','AND','THIS','WAS','WHO','ALL','ITS','ONE','TWO','OUR'):
            out.append(x); continue
        low=x.lower()
        if i not in (0,len(w)-1) and low.strip(':,;.') in SMALL:
            out.append(low)
        else:
            out.append(low[:1].upper()+low[1:])
    return ' '.join(out)

def slug(s):
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

for kind,a,b,c in ORDER:
    if kind=="part":
        pid=slug(a)
        body.append(f'<section class="partpage" id="{pid}"><p class="part-label">{a}</p><h1 class="part-title">{b}</h1></section>')
        toc.append(f'<div class="toc-part"><span class="t">{a} &middot; {b}</span></div>')
        continue
    md=(DRAFTS / b).read_text(encoding='utf-8')
    html=MD.convert(md); MD.reset()
    # epigraph attribution onto its own line
    html=re.sub(r'(<blockquote>\s*<p>.*?)\n?\s*—\s*(.*?)</p>',
                r'\1</p><p class="attrib">— \2</p>', html, flags=re.S)
    # first h1 becomes the chapter opener; capture title
    m=re.search(r'<h1>(.*?)</h1>', html, re.S)
    title=re.sub('<[^>]+>','',m.group(1)) if m else (c or "")
    n+=1; cid=f"sec{n}"
    # split "CHAPTER 5 — TITLE" into label + title
    mm=re.match(r'^\s*(CHAPTER\s+\d+|APPENDICES|CONCLUSION[^—]*|INTRODUCTION[^—]*|PREFACE)\s*—\s*(.+)$', title, re.I)
    if mm:
        lab, rest = mm.group(1).strip(), mm.group(2).strip()
        opener=f'<p class="ch-label">{lab}</p><h1 class="ch-title">{rest}</h1>'
        toctxt=f'{tcase(lab)} &middot; {tcase(rest)}'
    else:
        opener=f'<h1 class="ch-title solo">{title}</h1>'
        toctxt=tcase(title)
    html=re.sub(r'<h1>.*?</h1>', opener, html, count=1, flags=re.S)
    html=html.replace('<h1>','<h1 class="ch-title mid">')
    if b=="02_CHAPTERS_1_2.md":
        toctxt="Chapters 1&ndash;2 &middot; The Tradition, and the Data Gap"
    if kind=="back":
        html=html.replace('<table>','<table class="srctable">',1)
        if b=="11_REFERENCES.md":
            html='<div class="refs">'+html+'</div>' 
    cls="chapter" + (" backmatter" if kind=="back" else "")
    body.append(f'<section class="{cls}" id="{cid}">{html}</section>')
    toc.append(f'<div class="toc-item"><a href="#{cid}"><span class="t">{toctxt}</span><span class="dots"></span></a></div>')

front=FRONT.replace("TOC_ITEMS","\n".join(toc)).replace("{date}", EDITION_DATE)
head=("<meta charset='utf-8'><title>The Measure of the Wound</title>"
      "<meta name='author' content='Israel Lee Armstead'>"
      "<meta name='description' content='The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991-2024. Corrected Print Edition, Black Paper v1.4, Submission Edition. E5 Enclave Incorporated. CC0 1.0.'>"
      "<meta name='keywords' content='racial inequality, wealth gap, structural racism, Black Americans, longitudinal federal data, composite index, maternal mortality, incarceration, homeownership, open data'>"
      "<meta name='generator' content='bdi-black-paper build.py; python-markdown; WeasyPrint'>"
      f"<meta name='dcterms.created' content='{BUILD_STAMP}'>"
      f"<meta name='dcterms.modified' content='{BUILD_STAMP}'>")
doc=f"<!DOCTYPE html><html lang='en'><head>{head}<style>{(HERE / 'print.css').read_text(encoding='utf-8')}</style></head><body>{front}{''.join(body)}</body></html>"
(OUT / 'measure_of_the_wound.html').write_text(doc, encoding='utf-8')
print("sections:", n, "| html bytes:", len(doc))

if '--no-pdf' not in sys.argv:
    from weasyprint import HTML
    rendered = HTML(string=doc, base_url=str(OUT)).render()
    pdf_path = OUT / 'The_Measure_of_the_Wound.pdf'
    rendered.write_pdf(pdf_path)
    digest = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    print("pages:", len(rendered.pages), "| pdf bytes:", pdf_path.stat().st_size)
    print("sha256:", digest)
    (OUT / 'The_Measure_of_the_Wound.pdf.sha256').write_text(f"{digest}  The_Measure_of_the_Wound.pdf\n")
