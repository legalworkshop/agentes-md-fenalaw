---
name: visual-law
description: Método e ferramenta para transformar um contrato (com anexos) em contrato visual, isto é, o mesmo conteúdo jurídico reorganizado em blocos visuais e linguagem simples, em A4, com remissão à cláusula de origem e equivalência jurídica conferida dispositivo por dispositivo. Use nos agentes visual-law e conferente-equivalencia.
---

# Visual Law: o contrato em forma visual

Visual Law aqui **transforma o documento**: pega o contrato e os anexos e devolve o mesmo
conteúdo, reorganizado em blocos visuais (números-chave, linha do tempo, quem faz o quê, fluxo
dos dados, passos, tabela, glossário) e reescrito em linguagem simples. Não é relatório sobre
o contrato, não é parecer, não é análise de risco, não é cartilha: não opina, não recomenda,
não avalia. Quem lê o contrato visual sabe o que o contrato diz, não o que alguém acha dele.

## 1. A regra que vence todas: mesmo valor jurídico

Cada dispositivo do contrato aparece no contrato visual com **o mesmo efeito jurídico**. Para
cada cláusula, subcláusula, item de anexo ou definição com conteúdo normativo, preserve,
sem acrescentar nem tirar:

| Elemento | O que conferir |
|---|---|
| Sujeito | quem tem o dever ou o direito (Fornecedora, Cliente, ambas, terceiro) |
| Modal | deve, pode, não pode, é facultado; "poderá" não vira "deverá" |
| Objeto | o que se faz, entrega, paga ou se abstém de fazer |
| Prazo e marco | número, unidade (dias úteis ou corridos, horas, meses) e o evento que dispara a contagem |
| Valor e índice | número exato, moeda, base de cálculo, índice, periodicidade |
| Condição | "se", "desde que", "mediante", "salvo", aviso prévio, forma escrita |
| Exceção e ressalva | exclusões, limites, "exceto", "ressalvado" |
| Consequência | multa, crédito, rescisão, responsabilidade, teto |
| Remissão | anexos e cláusulas a que o dispositivo remete |

Proibido: arredondar número, trocar "dias úteis" por "dias", omitir exceção para simplificar,
fundir dois deveres de sujeitos diferentes, transformar faculdade em obrigação, acrescentar
consequência que o contrato não prevê, adjetivar ("prazo curto", "cláusula abusiva").
Cláusula sem efeito normativo (considerandos, títulos) pode ser resumida. Qualificação das
partes (CNPJ, endereço) entra completa na primeira página.

Cada item visual carrega `clausulas` com a remissão exata ("5.5", "A.2", "Aditivo 2.1"). O
conferente usa essa remissão para provar que todo dispositivo foi coberto.

## 2. Linguagem simples, sem perder o direito

ISO 24495-1 aplicada a texto normativo:

- frase curta, voz ativa, sujeito explícito ("A NimbusFlow avisa o Cliente...");
- verbo de dever no presente com valor de obrigação ("A Fornecedora comunica..." ou "deve
  comunicar"), mantendo "pode" para faculdade e "não pode" para proibição;
- palavra comum no lugar do jargão, **salvo quando o termo técnico tem efeito próprio**
  (incidente de segurança, suboperador, dados pessoais sensíveis): nesse caso, o termo fica e
  vai para o glossário;
- termo definido no contrato mantém o mesmo nome em todo o documento visual;
- rótulo antes do valor ("Reajuste: anual, pelo IPCA").

## 3. Catálogo de blocos

| Tipo | Para quê | Campos |
|---|---|---|
| `numeros` | 2 a 4 números-chave (valor, vigência, prazo, teto) | `itens`: `rotulo`, `valor` (uma linha), `detalhe`, `clausulas` |
| `linha_do_tempo` | marcos no tempo; até 6 no eixo | `titulo`, `marcos`: `quando`, `o_que`, `clausulas`, `tipo` |
| `duas_colunas` | quem faz o quê, uma coluna por parte | `titulo`, `colunas`: `cabecalho`, `itens`: `texto`, `clausulas` |
| `fluxo` | para onde vão os dados ou o trabalho (origem e destinos) | `titulo`, `origem`, `destinos`: `rotulo`, `texto`, `clausulas`, `grupo`, `terceiro`; opcionais `via`, `id` |
| `passos` | sequência real (o contrato fixa a ordem) | `titulo`, `passos`: `rotulo`, `texto`, `clausulas` |
| `tabela` | regras com rótulo e conteúdo | `titulo`, `linhas`: `rotulo`, `texto`, `clausulas`, `destaque`; opcionais `introducao`, `variante`, `matriz`, `manter_com_seguinte` |
| `glossario` | termos definidos e técnicos | como `tabela`; a frase de definição geral vai em `introducao` |
| `texto` | o que não cabe em nenhum dos anteriores | `titulo`, `paragrafos`: `texto`, `clausulas` |

Regras de uso, que o gerador confere ou aplica:

- **Linha do tempo:** `tipo: "ponto"` (padrão) é evento datado ou com posição na vigência
  (assinatura, aviso antes do fim, renovação); `tipo: "durante"` é o que vale a qualquer tempo
  ou se repete (reajuste anual, rescisão sem motivo): sai do eixo, numa faixa "Durante toda a
  vigência". Pôr evento recorrente no eixo afirma uma ordem que o contrato não tem. Com mais de
  4 marcos no eixo, o gerador alterna as descrições acima e abaixo dele, o que dobra a largura
  de cada uma; descrição com mais de 5 linhas sai com aviso (não recusa): encurte.
- **Passos:** só quando o contrato estabelece a sequência. Lista de condições sem ordem é
  `tabela`.
- **Fluxo:** `grupo: "brasil"` ou `"exterior"` em cada destino (o gerador agrupa e rotula);
  `terceiro: true` para quem não é a própria parte (barra vazada, seta tracejada). Havendo
  terceiro, o gerador põe sob o bloco a legenda de uma linha "Seta tracejada e barra vazada:
  terceiro, que não é parte do contrato." (precedida de "Seta contínua e barra cheia: parte do
  contrato." quando o mesmo fluxo tem destino que não é terceiro). `via` (índice 0-based em
  `destinos` ou o `id` de outro destino) marca o suboperador de outro destino: a seta sai do
  box daquele destino, não da origem, e o box fica recuado sob ele. O destino apontado vem
  antes na lista, no mesmo `grupo`, sem `via` próprio, e entre os dois só ficam outros
  destinos que saem dele; fora disso o gerador recusa. O `texto` não repete o rótulo nem
  começa com dois-pontos.
- **Tabela:** `destaque` é o número-chave da linha (99,5%; 30 dias), desenhado sob o rótulo;
  tem de ser trecho literal do `texto`, ou o gerador recusa. `variante: "enumeracao"` estreita a
  coluna de rótulo para listas (i), (ii). `manter_com_seguinte: true` faz a regra descer junto
  com a exceção (teto e casos em que ele não se aplica).
- **Matriz:** quando cada linha tem os mesmos campos (severidade, situação, primeira resposta,
  solução; fornecedor, serviço, dados, local), use `matriz`: lista de colunas `{rotulo,
  largura, forte}` cujas larguras, com 0,4 cm entre colunas, somam 17,8 cm, e em cada linha
  `campos` (um texto por coluna) mais `clausulas`. Só redistribui o texto; não resume.

## 4. Páginas

Cada página tem `titulo` que se entende sozinho, em forma de pergunta respondida ou de tema
claro ("Quem são as partes, o que se contrata e por quanto tempo", "Para onde vão os dados").
Ordem recomendada: (1) partes, objeto, números-chave e linha do tempo; (2) quem faz o quê;
(3) dados pessoais e segurança; (4) dinheiro e níveis de serviço; (5) se algo der errado
(incidente, responsabilidade, rescisão, saída); (6) regras gerais e glossário. O gerador
pagina sozinho: um tema começa onde couber; tabela, passos e duas colunas se dividem entre folhas sem deixar órfão. Recusa só bloco que não cabe numa folha inteira e não se divide.
Se a última folha ficar com menos de 30% da altura útil, o gerador tenta um perfil compacto
(menos espaço entre blocos, entre temas e entre linhas de tabela) e só o mantém se ele
economizar folha.

Tipografia aplicada pelo gerador, sem o agente precisar escrever: espaço inseparável depois
de "R$", "nº", "§" e "cl." e entre os itens de uma remissão ("cl. 2.2, 2.4"), hífen
inseparável entre algarismos (CNPJ, CEP) e aspas retas convertidas em curvas (“ ” ‘ ’, e
apóstrofo em ’).

## 5. Campos do documento

`contrato_id`, `titulo_curto` ("NimbusFlow e Meridiano"), `versao` (`tipo`: `aprovada` ou
`original`; `rotulo`: "Versão aprovada em 07/10/2026" ou "Versão original, sem revisão";
quando o aprovado abre com "Versão consolidada após o aditivo proposto", o rótulo repete essa
expressão, porque contrato assinado não se reescreve, adita-se),
`paginas` e `rodape`:

> Contrato em forma visual. Cada bloco reproduz, em linguagem simples e com o mesmo efeito
> jurídico, as cláusulas indicadas entre parênteses. Documento de demonstração: empresas e
> contrato fictícios, criados para a Fenalaw 2026.

## 6. Gerar

**Forma padrão desde 08/10/2026: infográfico.** O contrato visual em blocos de documento
(seções 3 a 5 e o gerador `contrato_visual.py`) foi reprovado como "90% texto". O padrão é o
infográfico em HTML, renderizado em PDF A4 pelo Chrome sem interface. As regras jurídicas
(seções 1 e 2) e os nove elementos não mudam; muda a forma:

- **Um objeto dominante por folha**, que conta a regra sem o texto: hub das partes com os
  fluxos de entrega e pagamento, régua de prazo em escala, escada de severidade com relógios,
  medidor de disponibilidade, escudo do operador com portão de autorização, mapa das
  transferências com arcos e selo do mecanismo, teto de responsabilidade com as exceções
  atravessando, esteira de saída com os prazos no eixo. O texto vira rótulo, legenda ou
  anotação presa à figura, com a remissão "cl. X".
- **A figura também afirma.** Seta, posição, escala, selo e cor não podem dizer o que o
  contrato não diz: fluxo no sentido certo; barra contada do marco certo; escala proporcional
  ou quebra de eixo explícita, uma escala por figura; numa figura que mistura dias úteis e
  corridos, um dia útil vale 1,4 dia corrido (10 dias úteis equivalem a no mínimo 14
  corridos); hipótese não vira dever; faculdade não vira dever ("pode indicar", nunca
  "indica"); aditivo proposto no futuro do subjuntivo ("que introduzir"); símbolo de vedação
  (X, cadeado) só onde o contrato veda; nada que pareça assinatura.
- **Código de cor fixo:** laranja só para consequência (crédito, desconto, justa causa,
  exceção ao teto, descumprimento); numeral azul-escuro para prazo; legenda numa linha do
  rodapé.
- **Glossário e regras gerais** podem ser página de leitura, sem distribuir vazio.
- **Mapa de cobertura** `<id>-cobertura.json`: para cada dispositivo, folha, figura e texto
  exato. É o que o `conferente-equivalencia` usa, junto com o texto do PDF.

Ferramenta, em `infografico/`: `base.html` (tokens de cor e tipografia, peças repetidas,
biblioteca de ícones e marcadores em `<symbol>`), `mapa.py` (contornos das Américas e da
Europa) e `montar.py`, que junta a base com uma folha por arquivo (`f1.html`, `f2.html`...),
aplica cabeçalho, rodapé e a tipografia brasileira, e gera HTML, PDF e PNG:

```
python .claude/skills/visual-law/infografico/montar.py --folhas <pasta com f1.html...> \
  --saida saida/visual-law/infografico/<id> --titulo "<partes>: contrato em forma visual" \
  --partes "<Parte A> e <Parte B>" --versao "<rótulo da versão>" --png <pasta dos PNG>
```

Confira cada folha em PNG a 200 dpi antes da conferência: o lint não mede texto encostado em
traço de SVG.

O gerador antigo, em blocos (`contrato_visual.py`, que usa o PowerPoint por COM), continua
disponível para quem precisar de `.pptx` editável.
