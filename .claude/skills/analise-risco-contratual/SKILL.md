---
name: analise-risco-contratual
description: Método comum de leitura de contrato e de produção de achado para os agentes de revisão. Use SEMPRE que for analisar um contrato, anexo ou aditivo e produzir achados, e SEMPRE antes de atribuir severidade ou confiança. Define a ordem de leitura, a regra de evidência, o critério objetivo de severidade, o schema de saída e o que NÃO é achado. NÃO usar para redigir a entrega final em .docx, que é da skill redline-docx.
---

# Análise de risco contratual — o método

O que muda entre os agentes é o que se enxerga. O **como** é este arquivo, e é igual para
todos.

## 1. Ordem de leitura, que não é a ordem do documento

**Onde ler.** O documento de referência é o `.docx` em `contratos/docx/<contrato>/`. Como
Read, Grep e Glob não abrem `.docx`, leia o texto extraído em `contratos/texto/<contrato>/`,
um `.txt` por documento, gerado por `contratos/build/docx2txt.py`: um parágrafo por linha,
tabela no lugar em que aparece, células separadas por " | ". Cite `trecho` copiando dali,
dentro de um único parágrafo ou célula, e liste em `documentos_lidos` o nome do `.docx`.

1. **Qualificação e datas.** Quem são as partes, quem é contratante, qual a data de
   assinatura, qual a vigência, o que já foi aditado.
2. **Anexos e aditivos primeiro, corpo depois.** O anexo técnico e o aditivo descrevem a
   operação real; o corpo descreve a operação imaginada. Quando divergem, a operação real
   prevalece na análise de risco — e a divergência em si é achado.
3. **Cláusulas da sua especialidade**, na ordem do checklist do seu arquivo de agente.
4. **Releitura cruzada:** o que o corpo promete que o anexo desmente, e o que o aditivo mudou
   sem atualizar o contrato-base.

Contrato antigo pede uma pergunta a mais: **o que mudou na operação desde a assinatura, e o
contrato acompanhou?** Cláusula que só manda cumprir a lei, escrita antes de a lei entrar em
vigor, não opera nada.

## 2. Regra de evidência, que é inegociável

Todo achado carrega:

- `localizacao` — cláusula, item, anexo, página. Precisa permitir que o leitor abra o
  documento e confira em cinco segundos.
- `trecho` — **citação literal**, entre 10 e 400 caracteres, copiada do documento. Sem
  reescrever, sem "conforme se depreende", sem resumo.

Não conseguindo citar literalmente, você não tem achado: tem impressão. Descarte.

**Evidência que mora em tabela.** Célula de tabela não é texto corrido, e citar uma linha
inteira com separadores não é citação literal. Cite o conteúdo da célula, ou a frase de prosa
mais próxima que sustente o mesmo ponto, e identifique a linha em `localizacao`, na forma
"Anexo 2, item 2.3, linha '<conteúdo da primeira célula da linha>'".

**Ausência de cláusula é achado legítimo**, e nesse caso `trecho` cita o trecho que deveria
tê-la e não tem — o cabeçalho da cláusula de proteção de dados, o final da seção onde a
matéria caberia — e `localizacao` indica onde a lacuna está. Nunca invente um `trecho` para
preencher o campo.

## 3. Severidade — critério, não sensibilidade

| Severidade | Definição operacional | Teste |
|---|---|---|
| `critico` | Exposição sancionatória direta, ou dever legal do cliente inviabilizado pelo contrato | "Se ninguém mexer nisso, a Meridiano pode ser autuada, ou fica impedida de cumprir um dever legal dela?" |
| `alto` | Amplia materialmente a exposição sem inviabilizar dever legal; ou transfere risco relevante ao cliente | "Isso aumenta a conta em caso de problema, ou tira uma defesa que a empresa teria?" |
| `medio` | Falha de governança contratual: ausência de controle, de prazo, de auditoria, de gatilho | "Isso vai doer no dia em que houver litígio ou fiscalização, mas não hoje" |
| `baixo` | Higiene: redação ambígua sem consequência prática imediata, remissão imprecisa, prazo indeterminado sem impacto | "Isso incomoda um advogado cuidadoso" |

Duas regras de calibragem:

- **Não infle.** Contrato bem redigido produz poucos achados, ou nenhum crítico. Achado
  crítico em contrato limpo significa que o método falhou, não que o contrato é ruim.
- **Não some severidades.** Dois achados médios não viram um alto. Quem compõe risco é o
  orquestrador, pela regra de cruzamento.

## 4. Confiança e evidência faltante

`confianca` é obrigatório e tem três valores:

- `alta` — o trecho citado sustenta o achado sozinho.
- `media` — o achado depende de interpretação defensável, ou de leitura combinada de dois
  dispositivos, e você aponta quais.
- `baixa` — falta informação. Nesse caso `evidencia_faltante` é obrigatório e diz, em uma
  frase, o que precisaria ser verificado: um anexo ausente, a política de segurança
  referenciada, a região de hospedagem, o instrumento de indicação do encarregado.

Um achado de confiança baixa bem escrito vale mais que uma afirmação categórica errada. Este
é o campo que separa ferramenta de apoio de gerador de opinião.

**Fundamento nulo não rebaixa a confiança sozinho.** A confiança mede a evidência do
achado, não a existência de norma. O rebaixamento para `baixa` por falta de fundamento
(`referencias-normativas`) vale para o achado **cuja tese depende de norma**, isto é, que
afirma ilicitude ou dever legal. Achado que se sustenta no texto do contrato e no playbook
(teto sem exclusão, reajuste sem índice, anexo ausente, remissão quebrada) sai com
`fundamento: null` e a confiança que a evidência textual justificar.

## 5. O que NÃO é achado

- Preferência de redação sem consequência jurídica.
- Cláusula que apenas repete a lei, quando a repetição não induz erro.
- Posição contratual **mais** protetiva que o mínimo legal. Isso é bom; se merecer registro,
  registre como `severidade: "baixo"` e diga que é favorável, ou não registre.
- Risco de outra especialidade. Achou algo fora do seu escopo, não opine: escreva no campo
  `achado` a observação e marque `agente` como o seu, com `severidade: "baixo"` e menção de
  que o ponto pertence a outra matéria. O orquestrador reencaminha.
- Ausência de cláusula cujo tema não pertence ao objeto do contrato.

## 6. Formato de saída

Um arquivo JSON por agente por contrato, em `saida/achados/<contrato_id>-<agente>.json`,
conforme `schemas/achado.schema.json`. `executado_em` é o horário real da gravação, em UTC
(obtenha-o do sistema, não estime nem arredonde): é o único carimbo de proveniência da
rodada. Estrutura:

```json
{
  "contrato_id": "00-exemplo-ficticio",
  "agente": "privacidade-lgpd",
  "documentos_lidos": ["contrato-exemplo.docx", "anexo-1-especificacao.docx"],
  "achados": [ { …schema de achado… } ],
  "observacoes": "Política de segurança citada no corpo e não fornecida; a análise de segurança ficou limitada ao texto do contrato."
}
```

Campos de cada achado: `id`, `contrato_id`, `agente`, `achado`, `localizacao`, `trecho`,
`severidade`, `fundamento`, `posicao_playbook`, `confianca`, `evidencia_faltante`,
`redline_sugerido`, `cruzamentos`.

Sobre `id`: use o prefixo da sua matéria e numeração sequencial dentro do contrato: `P-`
privacidade, `C-` comercial, `D-` consistência documental. O id é local à
sua rodada e serve para referência interna e para o cruzamento. **Ele não precisa coincidir
com o id do gabarito**, que é rótulo de teste: a correspondência entre achado e defeito
plantado se faz por localização e conteúdo, nunca por número.

Sobre `redline_sugerido`: texto de cláusula pronto para substituir ou inserir, redigido no
estilo do contrato analisado, sem marcação e sem comentário. Não sabendo redigir a solução,
deixe `null`, e o orquestrador redige. Regras de redação que valem para todo redline:

- **Dispositivo inteiro.** O texto proposto é a frase ou o dispositivo inteiro que
  substitui o original, nunca um fragmento a enxertar no meio dele.
- **Contrato assinado é aditivo.** Contrato com data de celebração passada e bloco de
  assinatura, sem indício de minuta, está em execução: a alteração vale dali em diante, o
  termo inicial de prazo novo é a assinatura do aditivo, nada retroage à data original e
  nada vira "condição de eficácia" do que já vigora (ver `redline-docx`).
- **Nenhuma remissão vazia.** Não remeta a anexo, item ou termo definido que não exista no
  conjunto, nem a anexo novo que você não redigiu. Faltando anexo, o conteúdo mínimo vai no
  próprio dispositivo.
- **Sujeito, faculdade e prazo.** Toda faculdade diz de quem é ("a critério da Meridiano",
  "autoriza a Meridiano a rescindir"); todo prazo tem número e termo inicial; nenhum prazo
  depende de ato sem prazo da outra parte.
- **Quem executa é quem pode executar.** Não atribua ao fornecedor medida de sistema que é
  da Meridiano, nem à Meridiano dever que a lei põe no fornecedor, nem condição que a
  Meridiano imponha a si mesma num contrato com o fornecedor.
- **Correção proporcional.** O redline corrige o defeito apontado sem retirar da Meridiano
  um poder que ela tinha e sem criar exposição nova em outra matéria. Vedação que impede o
  próprio serviço contratado de funcionar não é correção.
- **Mesmos termos do instrumento.** Use os termos definidos e a grafia das partes do
  documento alterado, inclusive a caixa e o nome definido de cada parte.

Sobre `cruzamentos`: preencha apenas se você **enxergar** o cruzamento; a composição
definitiva é do orquestrador.

## 7. Como escrever o campo `achado`

Uma frase, afirmativa, que diga o problema e a consequência. Sem adjetivo, sem alarme, sem
"é importante ressaltar".

- Ruim: "A cláusula de incidente é preocupante e deveria ser revista com urgência."
- Bom: "Prazo de 5 dias úteis para o vendor comunicar incidente ao contratante consome
  integralmente o prazo de 3 dias úteis do controlador perante a ANPD."

A segunda versão cabe em um comentário do Word e um advogado a lê sem traduzir.
