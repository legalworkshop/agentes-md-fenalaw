# Agentes em Markdown: revisão contratual multiagente

Material da masterclass **"Como Montar seus Agentes de IA: Arquitetura, Contexto, Fluxo e
Governança"**, Fenalaw 2026, com Anderson Fraiha Machado (FGV Direito SP) e Flávio C. Fujita
(The Legal Workshop).

Aqui está só a estrutura de instruções: os arquivos `.md` que dizem a um agente de IA quem
ele é, o que olhar e como fazer. É o esqueleto de um time de agentes que revisa contrato de
fornecedor e devolve redline com comentários. O caso é fictício (Meridiano Alimentos S.A.).

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
        └── visual-law/                método do contrato em forma visual
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

## O que não vem aqui

Os contratos fictícios, os schemas de JSON, os scripts de apoio (extração de texto, montagem
do Visual Law) e as saídas da demonstração ficam fora. Os arquivos citam essas pastas
(`contratos/`, `schemas/`, `saida/`) porque descrevem o projeto completo: ajuste os caminhos
ao seu.

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
