---
name: referencias-normativas
description: Base normativa versionada e conferida em fonte para os agentes de revisão contratual. Use SEMPRE que um achado precisar de fundamento legal ou regulamentar, e SEMPRE antes de escrever qualquer coisa no campo `fundamento` de um achado. Cobre LGPD, Resoluções CD/ANPD nº 15, 18 e 19 de 2024 e nº 32 de 2026 (adequação da União Europeia). NÃO usar como fonte de direito tributário, societário ou concorrencial, que estão fora do levantamento.
---

# Referências normativas

Esta skill existe para uma regra só: **nenhum agente inventa norma.**

## Como usar

1. Antes de preencher `fundamento`, abra o arquivo da matéria em `normas/`.
2. Cite o dispositivo pelo número, na forma "LGPD, art. 33" ou "Res. CD/ANPD 15/2024, art.
   6º".
3. Não estando o ponto coberto por estes arquivos, e dependendo o achado de norma para
   existir, o achado sai assim:
   - `fundamento`: `null`
   - `confianca`: `"baixa"`
   - `evidencia_faltante`: o que precisaria ser verificado, em uma frase

   Achado que se sustenta no texto do contrato e no playbook, sem afirmar ilicitude nem
   dever legal, sai com `fundamento: null` e mantém a confiança da evidência textual
   (`analise-risco-contratual`, seção 4). É o caso típico do agente contratual-comercial.

Achado sem fundamento é legítimo e útil. Achado com fundamento inventado destrói a revisão
inteira, porque um advogado na plateia confere.

## Arquivos

| Arquivo | Cobre |
|---|---|
| `normas/lgpd.md` | Papéis, princípios, bases legais, dado sensível, término e eliminação, segurança, incidentes, transferência internacional, direitos do titular, encarregado |
| `normas/res-15-2024.md` | Comunicação de incidente: prazos, conteúdo, registro. Traz a tabela de leitura do prazo do vendor |
| `normas/res-18-2024.md` | Encarregado. **Contém a regra que evita o falso positivo mais comum:** indicação por operador é facultativa |
| `normas/res-19-2024.md` | Transferência internacional e cláusulas-padrão. Prazo encerrado em 23/08/2025. Quem é exportador e importador, e por que as cláusulas-padrão se firmam entre o fornecedor e cada importador, não no contrato com a Meridiano |
| `normas/res-32-2026.md` | Decisão de adequação: União Europeia e Espaço Econômico Europeu. Importador coberto dispensa cláusulas-padrão (art. 33, I); a transferência continua tendo de ser declarada |

## Dois erros que esta skill existe para impedir

1. **Afirmar que existe resolução onde há guia orientativo.** Sobre relatório de impacto e
   legítimo interesse a ANPD publicou orientação, não regulamento. Diga isso no achado.
2. **Cobrar do operador dever que é do controlador**, e vice-versa. A distinção governa
   quase todo achado de privacidade.

## Data do levantamento

03/09/2026, complementado em 07/10/2026 com a Res. CD/ANPD 32/2026, de janeiro, que o
levantamento original perdeu. Cada arquivo registra a fonte consultada. Antes de qualquer
demonstração pública, reconfira as Resoluções da ANPD do ano inteiro, e não só as posteriores
ao levantamento.
