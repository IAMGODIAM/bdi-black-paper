import markdown, re, pathlib, datetime

MD = markdown.Markdown(extensions=['tables','attr_list','md_in_html'])

FRONT = """
<section class="titlepage">
  <div class="tp-rule"></div>
  <p class="tp-pub">E5 ENCLAVE INCORPORATED</p>
  <h1 class="tp-title">The Measure<br/>of the Wound</h1>
  <p class="tp-sub">A Sovereign Empirical Record of<br/>Black American Structural Distress</p>
  <p class="tp-dates">1991&#8202;&ndash;&#8202;2024</p>
  <div class="tp-rule"></div>
  <p class="tp-ed">Corrected Print Edition &middot; Black Paper v1.2</p>
  <p class="tp-place">Liberty City &middot; Miami, Florida</p>
</section>

<section class="copyright">
  <p><strong>The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991&ndash;2024</strong></p>
  <p>Corrected Print Edition &middot; Black Paper v1.2<br/>Published {date}</p>
  <p>E5 Enclave Incorporated<br/>820 NW 64th Street, Liberty City, Miami, Florida 33150<br/>EIN 99-3822441 &middot; UEI H8NGXEYE2HH8 &middot; CAGE 07E88<br/>e5enclave.com</p>
  <p class="cc"><strong>CC0 1.0 Universal &mdash; Public Domain Dedication.</strong> To the extent possible under law, E5 Enclave Incorporated has waived all copyright and related or neighboring rights to this work. No permission is required to copy, translate, adapt, excerpt or republish it, in whole or in part, for any purpose. No attribution is required, though it is appreciated.</p>
  <p><strong>Suggested citation.</strong> E5 Enclave Incorporated. (2026). <em>The Measure of the Wound: A Sovereign Empirical Record of Black American Structural Distress, 1991&ndash;2024.</em> Corrected Print Edition. CC0 1.0 Universal. github.com/IAMGODIAM/bdi-black-paper</p>
  <p><strong>Underlying data.</strong> All source data is public and openly licensed. Layer 1 raw evidence: <span class="mono">IAMGODIAM/bdi-raw-data-vault</span>. Layer 2 synthesized instrument: <span class="mono">IAMGODIAM/bdi-sovereign-dataset</span>, sealed on Base Mainnet, ExodusV4 token #2. Layer 3 place-level application: <span class="mono">IAMGODIAM/farmblock-data</span> and <span class="mono">IAMGODIAM/farmblock-dataset</span>.</p>
  <p><strong>On this edition.</strong> Every derived statistic was recomputed from the raw source series rather than carried forward from prior drafts, and flagged figures were re-verified against live federal sources in August 2026. Twenty-seven public claims were put through evidentiary triage; ten further arithmetic errors were found by recomputation; three canonical counts in the project&rsquo;s own governance documents were found stale. This edition then incorporates a second wave of corrections arising from an independent review of the v1.1 print edition (September 1, 2026), which identified a defective price basis in the Chapter 5 wealth series and an unverified denominator in the incarceration series. Both are corrected; several claims are withdrawn. All corrections are enumerated in Appendix H, sections A, B and B2.</p>
  <p class="motto"><em>Nil satis nisi optimum.</em></p>
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
    md=pathlib.Path(b).read_text()
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
    cls="chapter" + (" backmatter" if kind=="back" else "")
    body.append(f'<section class="{cls}" id="{cid}">{html}</section>')
    toc.append(f'<div class="toc-item"><a href="#{cid}"><span class="t">{toctxt}</span><span class="dots"></span></a></div>')

front=FRONT.replace("TOC_ITEMS","\n".join(toc)).replace("{date}", "August 2026")
doc=f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>The Measure of the Wound</title><style>{pathlib.Path('print.css').read_text()}</style></head><body>{front}{''.join(body)}</body></html>"
pathlib.Path('measure_of_the_wound.html').write_text(doc)
print("sections:", n, "| html bytes:", len(doc))
