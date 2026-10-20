# Revisão contratual multiagente — Meridiano Alimentos

Contexto do projeto, lido pelo agente toda vez que a pasta é aberta. Material da masterclass
"Como Montar seus Agentes de IA" (Fenalaw 2026), por Anderson Fraiha Machado e Flávio C.
Fujita / The Legal Workshop.

## O que este projeto faz

Recebe contratos de fornecedor, roda três agentes especialistas em paralelo, cada um com
contexto isolado, e devolve, por contrato, um `.docx` com alterações marcadas e comentários
ancorados, mais um JSON de achados que alimenta um painel de risco.

O cliente é fictício: a **Meridiano Alimentos S.A.**, indústria de alimentos, ~2.400
empregados, com jurídico interno de três advogados.

## Arquitetura em uma frase

**Agente é quem olha; skill é como se faz.** Três especialistas, quais sejam,
`privacidade-lgpd` (a única matéria de direito material), `contratual-comercial` e
`consistencia-documental`, e um orquestrador que cruza as saídas e redige a entrega. As
skills carregam o método, a base normativa, o playbook do cliente e a mecânica de redline, e
são compartilhadas.

**Escopo: sem matéria trabalhista.** Ponto trabalhista não vira achado nem redline, e nenhum
agente fundamenta em norma trabalhista.

```
contrato.docx ─┬─> privacidade-lgpd ──────┐
               ├─> contratual-comercial ──┼─> orquestrador-revisor ─> revisado.docx
               └─> consistencia-documental┘                        └─> matriz-risco.json
```

**Visual Law.** Depois da revisão aprovada, o orquestrador oferece o contrato em forma
visual; aceito, o agente `visual-law` transforma a versão aprovada no próprio contrato
reorganizado em blocos visuais e linguagem simples, com o mesmo efeito jurídico, e o
`conferente-equivalencia` confere dispositivo por dispositivo. Não é relatório nem análise de
risco.

## Regras que não se quebram

1. **Nenhum agente inventa norma.** Fundamento só sai de `.claude/skills/referencias-normativas/normas/`. Não estando lá, o achado é reportado sem fundamento e, se a tese dele depende de norma, com `confianca: "baixa"`.
2. **Nenhum agente inventa trecho.** O campo `trecho` é citação literal do documento. Não sendo possível citar, o achado não existe.
3. **Severidade sai de critério, não de sensibilidade.** O critério está em `analise-risco-contratual`.
4. **Divergência entre agentes é informação.** O orquestrador registra, não silencia.
5. **Contrato bem redigido não gera achado.** Posição dentro do padrão ou do fallback do playbook não é achado; nenhum agente procura defeito para justificar a própria existência.
6. **PT-BR em tudo**, inclusive nomes de campo de JSON e de pasta.

## Árvore

```
├── CLAUDE.md                    este arquivo
├── .claude/agents/              os seis agentes
├── .claude/skills/              método, normas, playbook, redline, Visual Law
├── contratos/docx/              os contratos em .docx (documento de referência)
├── contratos/texto/             o texto extraído do .docx, que é o que os agentes leem
├── contratos/build/             docx2txt.py, o extrator
├── schemas/                     formato do achado e da matriz de risco
└── saida/                       o que os agentes gravam
```

## Ordem de execução de uma rodada

1. Contrato novo: `python contratos/build/docx2txt.py --only <id>` gera o texto em
   `contratos/texto/<id>/` (Read não abre `.docx`).
2. Os três especialistas rodam sobre o mesmo contrato, sem se ver.
3. Cada um grava `saida/achados/<contrato>-<agente>.json`.
4. O orquestrador lê os três, cruza, confronta com o playbook, grava `saida/matriz-risco.json`
   e `saida/revisados/<contrato>-revisado.docx`.
5. Revisão humana do redline antes de qualquer uso.
