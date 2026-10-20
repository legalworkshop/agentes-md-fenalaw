# Agentes em Markdown: revisão contratual multiagente

Material da masterclass **"Como Montar seus Agentes de IA: Arquitetura, Contexto, Fluxo e
Governança"**, Fenalaw 2026, com Anderson Fraiha Machado (FGV Direito SP) e Flávio C. Fujita
(The Legal Workshop).

Aqui está a estrutura de instruções, isto é, os arquivos `.md` que dizem a um agente de IA
quem ele é, o que olhar e como fazer, e o necessário para testá-la: quatro contratos
fictícios, os formatos de saída e dois scripts de apoio. É um time de agentes que revisa
contrato de fornecedor e devolve redline com comentários. O caso é fictício (Meridiano
Alimentos S.A.).

## O mapa

```
├── CLAUDE.md                          a memória do projeto: contexto, regras, fluxo
└── .claude/
    ├── agents/                        quem olha
    │   ├── privacidade-lgpd.md
    │   ├── contratual-comercial.md
    │   ├── consistencia-documental.md
    │   ├── orquestrador-revisor.md    cruza os três e redige a entrega
    │   ├── visual-law.md              o contrato aprovado em forma visual
    │   └── conferente-equivalencia.md confere se o visual diz o mesmo que o contrato
    └── skills/                        como se faz
        ├── analise-risco-contratual/  ordem de leitura, evidência, severidade
        ├── referencias-normativas/    LGPD e resoluções da ANPD, com fonte
        ├── playbook-meridiano/        posições, fallbacks e linhas vermelhas do cliente
        ├── redline-docx/              mecânica do redline e do comentário ancorado
        └── visual-law/                método do contrato em forma visual, com o montador
├── contratos/
│   ├── docx/                          os quatro contratos fictícios, com anexos e aditivo
│   ├── texto/                         o texto extraído, que é o que os agentes leem
│   └── build/docx2txt.py              extrai o texto de um .docx novo
└── schemas/                           formato do achado, da matriz de risco e um exemplo
```

A pasta `.claude` pode aparecer oculta no Mac (no Finder, Cmd + Shift + .).

## Como usar

1. **Leia na ordem:** `CLAUDE.md`, depois um agente (comece por `privacidade-lgpd.md`),
   depois a skill que ele carrega. Repare na divisão: o agente diz o que olhar; a skill diz
   como fazer.
2. **Troque o cliente.** O `playbook-meridiano` é a peça mais pessoal: são as posições de um
   jurídico fictício. Reescreva com as posições do seu escritório ou da sua empresa.
3. **Leve para a sua ferramenta.** A estrutura vale para qualquer IA agêntica. O nome do
   arquivo raiz muda conforme a ferramenta: `CLAUDE.md` no Claude Code, `AGENTS.md` no padrão
   aberto adotado por várias outras, `GEMINI.md` no Gemini CLI. Em ChatGPT, Claude ou Gemini
   na versão de conversa, o conteúdo dos agentes e das skills funciona como instrução de
   projeto ou de GPT personalizado.

## Como testar

Com uma ferramenta agêntica que lê a pasta do projeto (o Claude Code lê `.claude/` como
está; em outra, aponte o arquivo raiz para o `CLAUDE.md`):

1. Abra a pasta do repositório na ferramenta.
2. Peça um especialista só, num contrato só: "rode o agente privacidade-lgpd no contrato
   01-nimbusflow". Ele grava os achados em `saida/achados/`, no formato de
   `schemas/achado.schema.json`. Compare com `schemas/exemplo-achados-ficticio.json`.
3. Rode os outros dois especialistas no mesmo contrato e depois o orquestrador, que cruza os
   três e redige o `.docx` revisado em `saida/revisados/`.
4. Teste o contrato 04 também.

Para usar um contrato seu, ponha o `.docx` em `contratos/docx/<id>/` e rode
`python contratos/build/docx2txt.py --only <id>` (requer `pip install python-docx`). O
Visual Law em PDF precisa de Python e de Chrome ou Edge instalados.

As saídas da demonstração não vêm aqui, de propósito: o teste vale mais quando você não sabe
de antemão o que os agentes vão achar.

## Ressalvas

- **Material didático.** Não é parecer jurídico nem produto. As empresas e os contratos são
  fictícios.
- **A base normativa é real**, conferida em fonte oficial, com a fonte registrada em cada
  arquivo de `referencias-normativas/normas/`. Confira a vigência antes de usar.
- **Agente não substitui revisão.** Todo redline produzido por estes agentes passa por
  advogado antes de sair.

## Licença

CC BY 4.0. Pode copiar, adaptar e usar, inclusive comercialmente, com crédito à The Legal
Workshop. Detalhes em `LICENSE`.
