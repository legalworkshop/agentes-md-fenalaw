---
name: redline-docx
description: Mecânica de produção da entrega final em .docx com revisões nativas do Word (w:ins / w:del) e comentários ancorados a intervalo de texto (w:comment + commentRangeStart/End). Use SEMPRE que for gerar o documento revisado a partir dos achados consolidados, e SEMPRE antes de escrever qualquer código de manipulação de .docx. Só o orquestrador-revisor carrega esta skill. NÃO usar para analisar contrato nem para atribuir severidade.
---

# Redline em `.docx` — como se faz de verdade

## A regra que define esta skill

**Texto tachado ou colorido não é redline.** Redline é revisão nativa do Word: elementos
`w:ins` e `w:del` no XML do documento, com autor e data, que aparecem no painel de revisão e
aceitam "Aceitar alteração". Comentário é `w:comment` ancorado por `w:commentRangeStart` e
`w:commentRangeEnd`, não nota no fim do documento.

A plateia da masterclass é de advogados que abrem `.docx` revisado todos os dias. Redline
falso é identificado em dois segundos e derruba a credibilidade de tudo que veio antes.

## O pacote OOXML, em três minutos

Um `.docx` é um ZIP. O que importa aqui:

```
word/document.xml        corpo do texto
word/comments.xml        conteúdo dos comentários
word/settings.xml        <w:trackChanges/> quando se quer forçar rastreamento de novas edições
[Content_Types].xml      declara a part de comentários
word/_rels/document.xml.rels   relacionamento document → comments
```

Inserir comentário exige as quatro últimas linhas resolvidas, não só a segunda. Biblioteca
que escreve parágrafo não faz isso sozinha.

### Inserção

```xml
<w:ins w:id="101" w:author="Revisão automatizada — Meridiano" w:date="2026-10-27T09:00:00Z">
  <w:r><w:t xml:space="preserve">no prazo de 24 (vinte e quatro) horas</w:t></w:r>
</w:ins>
```

### Exclusão

O texto excluído permanece no arquivo, dentro de `w:del`, e o `w:t` vira `w:delText`:

```xml
<w:del w:id="102" w:author="Revisão automatizada — Meridiano" w:date="2026-10-27T09:00:00Z">
  <w:r><w:delText xml:space="preserve">no prazo de até 5 (cinco) dias úteis</w:delText></w:r>
</w:del>
```

Substituição é `w:del` seguido de `w:ins`, na ordem em que o leitor espera ler.

### Comentário ancorado

Três peças no `document.xml`, na ordem, mais o conteúdo em `comments.xml`:

```xml
<w:commentRangeStart w:id="7"/>
<w:r><w:t>… trecho comentado …</w:t></w:r>
<w:commentRangeEnd w:id="7"/>
<w:r>
  <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>
  <w:commentReference w:id="7"/>
</w:r>
```

```xml
<!-- word/comments.xml -->
<w:comment w:id="7" w:author="Revisão automatizada — Meridiano"
           w:initials="RM" w:date="2026-10-27T09:00:00Z">
  <w:p><w:r><w:t>P-07 · Crítico · …</w:t></w:r></w:p>
</w:comment>
```

Regras que quebram o arquivo quando ignoradas: `w:id` único por espécie e coerente entre as
três peças; `commentRangeEnd` sem `commentRangeStart` correspondente invalida o pacote;
`xml:space="preserve"` em todo `w:t` que tenha espaço nas bordas; data em ISO 8601 com `Z`.

## Anatomia do comentário de risco

Um comentário, um achado. Formato fixo, porque o advogado lê dezenas:

```
[ID] · [SEVERIDADE] · [MATÉRIA]
Achado: uma frase.
Fundamento: dispositivo citado, ou "sem fundamento normativo localizado".
Playbook: aceitável | negociável | linha vermelha, e a posição da casa em meia linha.
Cruzamento: X-N — o que a combinação significa. (só quando houver)
Confiança: alta | média | baixa. (só quando não for alta, com o que falta verificar)
```

Exemplo, com números fictícios que não correspondem a nenhum dos contratos da demonstração:

```
P-07 · Crítico · Privacidade
Achado: prazo de 5 dias úteis para o fornecedor comunicar incidente consome
integralmente o prazo de 3 dias úteis da Meridiano perante a ANPD.
Fundamento: LGPD, art. 48; Res. CD/ANPD 15/2024, art. 6º.
Playbook: linha vermelha — o padrão da casa é 24 horas, com fallback de 2 dias úteis.
Cruzamento: X-2 — combinado com o teto de 2 mensalidades da cláusula 12.4, a sanção
recai sobre a Meridiano e o ressarcimento fica limitado a valor irrisório.
```

## Contrato assinado: o redline é minuta de aditivo

Contrato já assinado e em execução (data de celebração passada, bloco de assinatura, nenhum
indício de minuta), e aditivo já firmado, não se reescrevem: alteram-se por aditivo. Nesse
caso:

- o documento revisado é a **versão consolidada após o aditivo proposto**, e o sumário
  executivo o diz na primeira linha;
- cada alteração vale da assinatura do aditivo em diante. Prazo novo conta dessa assinatura
  (redação típica: "contados da assinatura do aditivo que introduzir esta redação"), e nunca
  da data de celebração ou do início de vigência do contrato original, o que o faria
  retroagir;
- nada vira **"condição de eficácia"** do contrato que já vigora. Condicionar a eficácia a
  anexo futuro, lido à letra, suspende o contrato inteiro, inclusive as obrigações do
  fornecedor. O que falta vira obrigação do fornecedor, com prazo e consequência do
  descumprimento (inadimplemento, direito de rescisão da Meridiano sem ônus).

## Como a alteração entra no texto

**Substitui a frase ou o dispositivo inteiro.** A alteração é `w:del` da frase (ou do
dispositivo) original seguida de `w:ins` da frase (ou do dispositivo) nova. Nunca se enxerta
fragmento no meio da frase original: o enxerto desloca orações, deixa vírgula dupla e liga a
finalidade de uma frase a outra. Quando a sugestão consolidada é frase inteira, aplica-se
frase inteira. Teste: aceitas todas as alterações, cada frase alterada se lê sozinha e
coincide, palavra por palavra, com o texto aprovado na matriz.

**Nunca remete a anexo que não existe e nunca cria anexo sem redigi-lo.** O redline não
introduz remissão a anexo, item, lista ou documento ausente do conjunto ("conforme anexo",
"lista anexa", "constarão do anexo", "a ser firmado"). Se o achado é justamente a falta de um
anexo, a alteração traz o conteúdo mínimo no próprio corpo, ou como item novo inteiramente
redigido no mesmo ato; o que depender de documento que só o fornecedor pode produzir vira
obrigação dele, com conteúdo mínimo, prazo e consequência. Remissão vazia é o mesmo defeito
que o sistema acusa como linha vermelha, e o leitor nota a contradição.

## Estrutura do documento entregue

1. **Sumário executivo**, uma página, inserido antes do texto do contrato: natureza do
   documento (versão consolidada após o aditivo proposto, ou redline de minuta), contagem
   por severidade, os cruzamentos identificados, as três ações prioritárias e a lista de
   documentos analisados. O sumário é texto normal, não revisão marcada.
2. **O contrato**, com as alterações marcadas e os comentários ancorados.
3. **Rodapé de proveniência** ao final: quais agentes rodaram, data e hora, versão da base
   normativa, e o aviso de que a revisão é apoio e não substitui a análise do advogado
   responsável.

## Autoria e data

Autor único: `Revisão automatizada — Meridiano`. Data: a da execução, em UTC. Autor único
permite filtrar por revisor no Word e é o que o `--author` do validador confere.

Não use nome de pessoa. Revisão assinada por gente que não revisou é problema, não recurso.

## Ordem de aplicação

1. Consolide os achados e resolva conflitos **antes** de tocar no arquivo.
2. Ordene as intervenções pela posição no documento, **de trás para frente**. Editar do fim
   para o começo evita que cada inserção desloque os offsets das seguintes.
3. Aplique primeiro os `w:del`/`w:ins`, depois as âncoras de comentário.
4. Valide e só então grave.

## Validação obrigatória antes de entregar

- O arquivo abre no Word sem aviso de conteúdo ilegível.
- O painel de revisão lista as alterações, e "Aceitar todas" produz um documento coerente:
  sem fragmento enxertado, sem vírgula dupla, sem remissão a anexo inexistente, e com o
  texto de cada dispositivo igual ao aprovado na matriz.
- "Rejeitar todas" devolve o contrato original, caractere a caractere.
- Cada comentário está ancorado ao trecho certo, não ao parágrafo inteiro nem ao fim.
- Todo achado `critico`, `alto` ou em `linha_vermelha` da matriz tem comentário
  correspondente no documento.
- Nenhum comentário cita fundamento que não está em `referencias-normativas`.

Falhando qualquer item, o arquivo não sai. É preferível entregar menos alterações e um
arquivo íntegro.

### Como validar com o `validate.py` da skill `docx`

O sumário executivo e o rodapé de proveniência entram como texto normal, por isso a
comparação com o `.docx` original acusa alteração não rastreada. O procedimento, testado na
rodada de 23/09/2026:

1. Monte primeiro a **base sem revisões**: o mesmo arquivo final (sumário, documentos do
   conjunto e proveniência), sem nenhum `w:ins`, `w:del` nem comentário.
2. Valide o revisado contra ela:
   `python validate.py <revisado.docx> --author "Revisão automatizada — Meridiano" --original <base-sem-revisoes.docx>`.
   O `--author` exige o `--original`.
3. No Windows, rode com `PYTHONIOENCODING=utf-8`, sem o qual o validador quebra ao imprimir
   o próprio relatório.
4. Erros de XSD que também aparecem no `.docx` de entrada (ordem de `w:pBdr`, `w:zoom` sem
   `w:percent`) vêm do gerador dos contratos, não do redline.

## Nota de implementação

Bibliotecas usuais de `.docx` escrevem parágrafo e formatação, não revisão nativa. Quem gera
redline de verdade manipula o XML do pacote, via biblioteca que exponha o XML subjacente ou
via edição direta do ZIP. Verifique antes de escolher: escrever `w:ins` costuma exigir
descer ao XML mesmo quando a biblioteca tem API de alto nível.
