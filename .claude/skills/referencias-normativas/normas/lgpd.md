# LGPD — Lei nº 13.709/2018

Fonte conferida: texto compilado no Planalto, `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm`, consultado em 03/09/2026.

Use estes dispositivos como fundamento. Citação por artigo e inciso. Não parafraseie o
texto legal dentro do campo `fundamento`: cite o dispositivo e explique no campo `achado`.

---

## Papéis e responsabilidade

**Art. 5º, VI a VIII** — controlador é a quem competem as decisões referentes ao tratamento;
operador é quem trata em nome do controlador; encarregado é o canal de comunicação entre
controlador, titulares e ANPD.

**Art. 39** — "O operador deverá realizar o tratamento segundo as instruções fornecidas pelo
controlador, que verificará a observância das próprias instruções e das normas sobre a
matéria."

**Art. 42, § 1º** — o operador responde solidariamente quando descumprir as obrigações da
lei ou quando não tiver seguido as instruções lícitas do controlador; nessa hipótese, o
operador equipara-se ao controlador.

> **Regra de leitura que vale ouro nesta demo.** O papel decorre da operação, não da
> etiqueta. Cláusula que declara "operador" enquanto o anexo descreve finalidade própria,
> base própria e decisão sobre meios e fins descreve, na verdade, um controlador, e o
> achado é a incompatibilidade entre a declaração e a operação, fundamentada no art. 5º, VI
> e VII, combinado com o art. 39.


**Nome do órgão.** A MP 1.317/2025, convertida em lei em 2026, transformou a Autoridade Nacional
de Proteção de Dados em **Agência Nacional de Proteção de Dados (ANPD)**, e o texto compilado da
LGPD no Planalto já usa o nome novo (art. 5º, VIII, conferido em 07/10/2026). Redação nova de
contrato usa "Agência Nacional de Proteção de Dados (ANPD)"; texto original de contrato
antigo que use o nome anterior não é achado.

## Princípios

**Art. 6º** — boa-fé e, entre outros: **I finalidade** (propósitos legítimos, específicos,
explícitos e informados ao titular, "sem possibilidade de tratamento posterior de forma
incompatível com essas finalidades"); **II adequação**; **III necessidade** (mínimo
necessário); **IV livre acesso**; **V qualidade**; **VI transparência**; **VII segurança**;
**VIII prevenção**; **IX não discriminação**; **X responsabilização e prestação de contas**.

A finalidade secundária (uso do dado recebido para treinar modelo próprio, alimentar base de
dados do fornecedor, revender análise) faz do fornecedor controlador dessa parte, com base legal
própria, que é dele, e dever de informar o titular. O achado contratual, para a Meridiano, é o
compartilhamento para finalidade incompatível com a informada ao titular, fundado no art. 6º, I
e II; não a falta de base legal nomeada no contrato.

## Bases legais

**Art. 7º** — hipóteses de tratamento de dado pessoal comum, entre elas consentimento (I),
cumprimento de obrigação legal (II), execução de contrato (V), exercício regular de
direitos (VI) e legítimo interesse (IX).

**Art. 11** — dado pessoal **sensível** só pode ser tratado: (I) com consentimento
específico e destacado; ou (II) sem consentimento, quando indispensável para, entre outras,
"a) cumprimento de obrigação legal ou regulatória pelo controlador"; "d) exercício regular
de direitos, inclusive em contrato e em processo judicial"; "e) proteção da vida ou da
incolumidade física do titular ou de terceiro"; "g) garantia da prevenção à fraude e à
segurança do titular, nos processos de identificação e autenticação de cadastro em sistemas
eletrônicos, resguardados os direitos mencionados no art. 9º desta Lei e exceto no caso de
prevalecerem direitos e liberdades fundamentais do titular que exijam a proteção dos dados
pessoais".

**Art. 5º, II** — dado sensível abrange dado biométrico. Biometria usada para liberar acesso
físico é dado sensível, e a alínea "g" do art. 11, II, não é passe livre: ela é excepcional, está
condicionada aos direitos do art. 9º e cede quando prevalecerem direitos e liberdades
fundamentais do titular.

> **Não existe base legal "por conveniência operacional".** Controle de acesso biométrico
> pode ser fundamentado, mas a fundamentação é do controlador e se escreve no registro do
> tratamento e no relatório de impacto, com finalidade, necessidade e proporcionalidade
> demonstradas e alternativa menos invasiva considerada. **Quem escolhe a base legal é o
> controlador; contrato com operador não a redige**, porque o operador trata segundo as
> instruções recebidas (art. 39). O que o contrato precisa ter é finalidade delimitada, prazo
> de guarda, segurança reforçada e apoio ao relatório de impacto. Contrato silente sobre esses
> pontos é achado, não é lacuna irrelevante.

**Severidade fixada.** Tratamento de dado sensível (inclusive biometria) que o instrumento
não disciplina por cláusula específica, seja porque entrou por aditivo, anexo ou ordem de
serviço, seja porque só há cláusula genérica de cumprimento da lei, é **crítico**: o
controlador fica sem como demonstrar finalidade, necessidade e segurança do tratamento mais
protegido pela lei (arts. 6º, X, 11 e 46), o que é exposição sancionatória direta. Havendo
cláusula específica, a falta de relatório de impacto ou de regra de guarda é **alto**.

## Término, eliminação e devolução

**Art. 15** — o tratamento termina pela finalidade alcançada, pelo fim do período, por
comunicação do titular ou por determinação da autoridade.

**Art. 16** — "Os dados pessoais serão eliminados após o término de seu tratamento, no
âmbito e nos limites técnicos das atividades", autorizada a conservação apenas para (I)
obrigação legal ou regulatória; (II) estudo por órgão de pesquisa; (III) transferência a
terceiro nos termos da lei; (IV) uso exclusivo do controlador, vedado o acesso por terceiro
e desde que anonimizados.

Contrato sem cláusula de devolução ou eliminação ao término deixa o operador com base viva
e sem gatilho contratual de descarte: achado de nível alto, fundado nos arts. 15 e 16.

## Segurança e incidentes

**Art. 46** — medidas técnicas e administrativas aptas a proteger os dados, observadas
"desde a fase de concepção do produto ou do serviço até a sua execução" (§ 2º).

**Art. 48** — o **controlador** comunica à ANPD e ao titular o incidente que possa acarretar
risco ou dano relevante. Prazo e conteúdo: Resolução CD/ANPD nº 15/2024 (arquivo próprio).

> **A conta que o advogado precisa fazer.** O dever de comunicar é do controlador, mas quem
> descobre o incidente é o operador. Prazo de notificação do vendor maior que o prazo do
> controlador perante a ANPD inviabiliza o cumprimento do art. 48. É achado crítico e é
> aritmética, não opinião.

## Transferência internacional

**Art. 33** — a transferência internacional só é permitida nas hipóteses do rol, entre elas
países com grau adequado de proteção (I); garantias oferecidas pelo controlador na forma de
cláusulas contratuais específicas, **cláusulas-padrão contratuais**, normas corporativas
globais ou selos e códigos de conduta (II); autorização da autoridade nacional (V);
consentimento específico e destacado, com informação prévia sobre o caráter internacional
(VIII).

Detalhamento e prazo de incorporação das cláusulas-padrão: Resolução CD/ANPD nº 19/2024
(arquivo próprio).

## Direitos do titular e governança

**Art. 18** — confirmação de tratamento, acesso, correção, anonimização, portabilidade,
eliminação, informação sobre compartilhamento, revogação do consentimento. O contrato com o
operador precisa prever prazo e forma de auxílio ao controlador no atendimento.

**Art. 41** — o controlador indicará encarregado, com identidade e contato divulgados
publicamente. Atuação detalhada: Resolução CD/ANPD nº 18/2024 (arquivo próprio).

## Lacuna assumida, e que o agente deve declarar

Não há, até 03/09/2026, resolução da ANPD especificamente sobre **relatório de impacto à
proteção de dados (RIPD)** ou sobre **legítimo interesse**. Sobre esses temas existem a
LGPD (arts. 5º, XVII, e 38; o art. 10, § 3º, trata só do tratamento fundado em legítimo interesse e não se cita para dado sensível) e guias orientativos da autoridade, não regulamento. O
agente que tocar nesses pontos deve fundamentar na lei e dizer expressamente que a
orientação da ANPD é guia, não norma. Afirmar que "a ANPD exige RIPD por resolução" é erro
que a plateia da masterclass identifica.

Registre-se, porém, que o art. 8º da Resolução CD/ANPD nº 15/2024 autoriza a autoridade a
**solicitar o RIPD** no contexto de incidente, o que é diferente de obrigar sua elaboração
prévia e genérica.
