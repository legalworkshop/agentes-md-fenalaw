"""Monta o contrato visual em forma de infográfico: base (CSS e ícones) mais uma folha por arquivo,
cabeçalho e rodapé, tipografia brasileira, PDF pelo Chrome sem interface e, opcionalmente, PNG.

Uso:
  python montar.py --folhas pasta_com_f1.html_f2.html... --saida saida/visual-law/infografico/<id>
                   --titulo "Áureo e Meridiano: contrato em forma visual"
                   --partes "Áureo e Meridiano" --versao "Versão aprovada em 07/10/2026" [--png pasta]

Cada folha é um <section class="folha"> com os marcadores <!--HDR--> e <!--FTR--> onde vão o
cabeçalho e o rodapé. O mapa de contornos (mapa.py) substitui os marcadores {MAPA_...} se houver.
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
NBSP, NBH = "\u00a0", "\u2011"
UNID = r"(minutos?|horas?|dias|dia|meses|mês|anos?|segundos|vezes|vias)"

HDR = ('<div class="hdr"><span><b>Contrato em forma visual</b> | {partes}</span>'
       '<span>{versao}</span></div>')
FTR = ('<div class="ftr"><div><span class="cor"><b>Laranja:</b> consequência. <i>Numeral azul-escuro:</i> '
       'prazo. Barras em escala dentro de cada figura.</span> Cada elemento '
       'reproduz, em linguagem simples e com o mesmo efeito jurídico, as cláusulas indicadas (cl.).<br>'
       '{nota}</div><div class="pn">{n} de {m}</div></div>')


def tipografia(t):
    """Espaço inseparável depois de R$, nº, §, cl. e entre número e unidade; hífen inseparável entre
    algarismos (CNPJ, CEP); remissões em lista sem quebra entre os itens."""
    t = re.sub(r"R\$ ", "R$" + NBSP, t)
    t = re.sub(r"nº ", "nº" + NBSP, t)
    t = re.sub(r"§ ", "§" + NBSP, t)
    t = re.sub(r"\bcl\. ", "cl." + NBSP, t)
    t = re.sub(r"(cl\.\u00a0[0-9A-C.()ivx]+(?:,\u00a0[0-9A-C.()ivx]+)*), (?=[0-9A-C])", r"\1," + NBSP, t)
    t = re.sub(r"(\d) " + UNID, lambda m: m.group(1) + NBSP + m.group(2), t)
    t = t.replace("dias úteis", "dias" + NBSP + "úteis")
    t = re.sub(r"(\d)-(\d)", r"\1" + NBH + r"\2", t)
    return t


def processa(html):
    partes = re.split(r"(<style.*?</style>|<[^>]+>)", html, flags=re.S)
    return "".join(p if p.startswith("<") else tipografia(p) for p in partes)


def chrome():
    candidatos = [os.environ.get("CHROME", ""),
                  r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                  shutil.which("google-chrome") or "", shutil.which("chromium") or ""]
    for c in candidatos:
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome ou Edge não encontrado; defina a variável CHROME")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folhas", required=True)
    ap.add_argument("--saida", required=True, help="caminho sem extensão")
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--partes", required=True)
    ap.add_argument("--versao", required=True)
    ap.add_argument("--nota", default="Documento de demonstração: empresas e contrato fictícios.")
    ap.add_argument("--png", help="pasta para PNG por folha (precisa do PyMuPDF)")
    a = ap.parse_args()

    base = open(os.path.join(AQUI, "base.html"), encoding="utf-8").read().replace("{TITULO}", a.titulo)
    folhas = sorted(glob.glob(os.path.join(a.folhas, "f*.html")),
                    key=lambda f: int(re.search(r"f(\d+)\.html$", f).group(1)))
    src = base + "\n" + "\n".join(open(f, encoding="utf-8").read() for f in folhas) + "\n</body></html>\n"
    try:
        sys.path.insert(0, AQUI)
        import mapa
        for k, v in getattr(mapa, "PATHS", {}).items():
            src = src.replace(k, v)
    except ImportError:
        pass
    m = src.count("<!--FTR-->")
    contador = iter(range(1, m + 1))
    src = src.replace("<!--HDR-->", HDR.format(partes=a.partes, versao=a.versao))
    src = re.sub(r"<!--FTR-->", lambda _: FTR.format(nota=a.nota, n=next(contador), m=m), src)
    html = a.saida + ".html"
    os.makedirs(os.path.dirname(os.path.abspath(html)), exist_ok=True)
    open(html, "w", encoding="utf-8").write(processa(src))

    tmp = tempfile.mkdtemp(prefix="infografico-")
    pdf_tmp = os.path.join(tmp, "saida.pdf")
    subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--user-data-dir=" + os.path.join(tmp, "perfil"), "--print-to-pdf=" + pdf_tmp,
                    "file:///" + os.path.abspath(html).replace("\\", "/")],
                   capture_output=True, text=True, timeout=180)
    if not os.path.exists(pdf_tmp):
        sys.exit("PDF não gerado")
    shutil.copyfile(pdf_tmp, a.saida + ".pdf")
    if a.png:
        import pymupdf as fitz
        os.makedirs(a.png, exist_ok=True)
        doc = fitz.open(pdf_tmp)
        nome = os.path.basename(a.saida)
        for i, p in enumerate(doc, 1):
            p.get_pixmap(dpi=200).save(os.path.join(a.png, f"{nome}-s{i:02d}.png"))
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"ok: {m} folhas; {a.saida}.html e .pdf")


if __name__ == "__main__":
    main()
