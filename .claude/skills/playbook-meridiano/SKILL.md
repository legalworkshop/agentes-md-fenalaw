---
name: playbook-meridiano
description: Posições contratuais padrão, fallbacks e linhas vermelhas da Meridiano Alimentos S.A. na contratação de fornecedores. Use SEMPRE que for classificar um achado como aceitável, negociável ou linha vermelha, e SEMPRE antes de propor redline, para que a redação proposta reflita a posição da casa e não a preferência do modelo. Cobre privacidade e contratual-comercial. NÃO usar como fonte de norma (isso é referencias-normativas) nem para contratos com a Administração Pública, fora do escopo.
---

# Playbook da Meridiano Alimentos

Documento interno fictício, para a demonstração. Escrito na primeira pessoa do plural
porque é assim que playbook de departamento jurídico se escreve: é a voz da casa.

## Para que serve

Norma diz o que é obrigatório. Playbook diz **o que esta empresa aceita assinar**. São
coisas diferentes, e a diferença é metade do valor de uma revisão contratual: sem playbook,
o revisor devolve uma lista de tudo que poderia ser melhor; com playbook, devolve o que
precisa mudar antes de assinar.

## Como classificar

Todo achado recebe `posicao_playbook`:

| Valor | Significado | O que o orquestrador faz |
|---|---|---|
| `aceitavel` | A posição do contrato está dentro do que aceitamos | Registra sem propor alteração; comentário informativo, se houver |
| `negociavel` | Fora do padrão e do fallback, mas abaixo da linha vermelha. (Posição dentro do fallback é `aceitavel`: não é achado) | Propõe redline no padrão da casa, e o comentário diz qual fallback é aceitável na negociação. O redline nunca abre no fallback, salvo quando o defeito é só a condição que falta para a posição ficar no fallback: aí o redline acrescenta a condição e conserva o resto. No corpo do documento, só nos casos da seção 7 de `orquestrador-revisor`. Achado crítico por dever legal não é `negociavel`: é `linha_vermelha` |
| `linha_vermelha` | Não assinamos assim | Redline obrigatório, comentário com a linha vermelha explícita e escalonamento à diretoria jurídica |
| `sem_posicao` | O playbook não trata do ponto | Registra o achado com fundamento normativo apenas, e sinaliza a lacuna do playbook |

`sem_posicao` é resposta legítima e precisa aparecer. Playbook que finge cobrir tudo produz
revisão que inventa política da casa.

## Contexto que explica as posições

Meridiano Alimentos S.A., indústria de alimentos, ~2.400 empregados, e-commerce próprio e
programa de fidelidade com base de consumidores na casa dos milhões. Jurídico interno de
três advogados, sem CLM, revisando contratos no fluxo de compras. Controladora dos dados de
clientes, empregados e candidatos. Sem operação internacional própria.

Duas consequências que atravessam o playbook inteiro: **somos controladores em quase tudo**,
e portanto herdamos o dever de comunicar incidente e responder perante a ANPD; e **temos
volume de fornecedores maior que capacidade de fiscalização**, o que nos obriga a converter
fiscalização em obrigação contratual documentada.

## Arquivos

- `posicoes/privacidade.md`
- `posicoes/comercial.md`

## Regra de ouro do playbook

**Se a posição da casa for mais protetiva que a lei, é a posição da casa que vale para o
redline; se for menos protetiva que a lei, vale a lei, e o achado é da lei.** Playbook não
derroga norma, e o agente que usar o playbook para relaxar exigência legal cometeu o erro
mais grave possível nesta arquitetura.
