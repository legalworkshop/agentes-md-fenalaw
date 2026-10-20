# -*- coding: utf-8 -*-
"""
Extrai o texto dos .docx de contratos/docx/ para contratos/texto/, um .txt por documento.

Existe porque os agentes especialistas leem com Read, Grep e Glob, e nenhuma dessas
ferramentas abre .docx. O .txt é a entrada de leitura; o .docx continua sendo o documento
de referência, e é contra ele que o campo `trecho` é conferido.

Formato, que a regra do trecho literal pressupõe:
  - um parágrafo do Word por linha, na ordem do documento;
  - tabela no lugar em que aparece, uma linha por linha da tabela, células separadas por " | ";
  - texto sem alteração nenhuma: numeração literal, aspas, acentos e maiúsculas preservados.

Um trecho citado deve caber dentro de um único parágrafo ou de uma única célula.

Uso:
  python docx2txt.py            todos os contratos
  python docx2txt.py --only 01  só o contrato 01
"""

import os
import argparse
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

AQUI = os.path.dirname(os.path.abspath(__file__))
CONTRATOS = os.path.dirname(AQUI)
ENTRADA = os.path.join(CONTRATOS, "docx")
SAIDA = os.path.join(CONTRATOS, "texto")


def linhas(documento):
    corpo = documento.element.body
    for filho in corpo.iterchildren():
        nome = filho.tag.split("}")[-1]
        if nome == "p":
            yield Paragraph(filho, documento).text
        elif nome == "tbl":
            for linha in Table(filho, documento).rows:
                yield " | ".join(celula.text for celula in linha.cells)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="prefixo do contrato, ex.: 01")
    args = ap.parse_args()

    for contrato in sorted(os.listdir(ENTRADA)):
        pasta = os.path.join(ENTRADA, contrato)
        if not os.path.isdir(pasta) or (args.only and not contrato.startswith(args.only)):
            continue
        destino = os.path.join(SAIDA, contrato)
        os.makedirs(destino, exist_ok=True)
        for nome in sorted(os.listdir(pasta)):
            if not nome.endswith(".docx") or nome.startswith("~$"):
                continue
            texto = "\n".join(linhas(docx.Document(os.path.join(pasta, nome))))
            alvo = os.path.join(destino, nome[:-5] + ".txt")
            with open(alvo, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto + "\n")
            print("ok  " + contrato + "/" + nome[:-5] + ".txt")


if __name__ == "__main__":
    main()
