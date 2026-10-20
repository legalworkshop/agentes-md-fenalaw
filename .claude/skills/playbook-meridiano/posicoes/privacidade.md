# Playbook Meridiano — proteção de dados

Somos controladores. Cada fornecedor que trata dado por nossa conta é operador, e é a nossa
exposição que está em jogo quando ele erra.

## 1. Papéis

**Padrão.** O contrato declara os papéis expressamente e a declaração tem que bater com a
operação descrita nos anexos. O fornecedor trata os dados exclusivamente segundo instruções
documentadas nossas e para as finalidades do contrato.

**Fallback.** Controladoria conjunta é admissível quando a operação realmente a caracterizar,
desde que o contrato reparta as responsabilidades e defina quem atende o titular.

**Linha vermelha.** Fornecedor que usa dado nosso para finalidade própria (treinar modelo,
alimentar base de dados dele, gerar produto vendido a terceiros, enriquecer cadastro dele)
sob a etiqueta de operador. Não assinamos. Ou o uso próprio sai do contrato, ou o contrato assume
o papel real: a finalidade própria do fornecedor delimitada no contrato, a responsabilidade
dele como controlador dessa parte e a informação ao titular.

## 2. Incidente de segurança

**Padrão.** Notificação em até **24 horas** contadas do momento em que o fornecedor tomar
conhecimento do incidente, ainda que preliminar, com dever de complementar à medida da
apuração. Conteúdo: as informações do art. 6º, § 2º, da Res. CD/ANPD 15/2024 **de que o
fornecedor disponha ou que lhe caiba apurar** (parte delas, como a identificação do
controlador e do encarregado, só a Meridiano tem; exigir "no mínimo" o rol inteiro do
operador cria obrigação que ele nunca cumpre). Dever de cooperar com a nossa comunicação à
ANPD e aos titulares, e de não comunicar **titulares** por conta própria sem nossa
autorização prévia. Requisição da ANPD ou de outra autoridade dirigida ao fornecedor não se
veda nem se condiciona a alinhamento: o fornecedor informa a Meridiano de imediato, salvo
vedação legal.

**Quando o fornecedor é controlador** de parte dos dados (os dos próprios empregados, por
exemplo), ele tem dever próprio de comunicar a autoridade e os titulares desses dados, e o
contrato não o condiciona ao nosso alinhamento. A restrição acima vale só para os dados de
que a Meridiano é controladora.

**Fallback.** Até 2 dias úteis, desde que a notificação preliminar seja imediata.

**Linha vermelha.** Prazo igual ou superior a 3 dias úteis; prazo que só começa a correr
após "confirmação", "validação" ou "conclusão da apuração" pelo fornecedor; ou ausência de
dever de notificar. Qualquer dos três inviabiliza o nosso prazo legal.

## 3. Subcontratação

**Padrão.** Autorização prévia, específica e por escrito para cada suboperador, e o silêncio
da Meridiano não importa autorização. Os suboperadores já autorizados ficam relacionados no
corpo do contrato ou em anexo efetivamente entregue, e a relação inclui **todo** suboperador
que o próprio conjunto contratual já descreve (provedor de infraestrutura, ferramenta de
terceiro, empresa do grupo): redline que exige autorização e deixa de fora suboperador
já em uso faz o fornecedor nascer inadimplente. Obrigações não menos protetivas repassadas a
cada suboperador por contrato escrito; responsabilidade do fornecedor perante a Meridiano
pelos atos e omissões dos suboperadores como se fossem seus.

**Fallback.** Autorização geral com lista no contrato ou em anexo efetivamente entregue,
direito de objeção fundamentada em 15 dias, com efeito definido (objeção impede a inclusão
ou autoriza a rescisão sem ônus), e comunicação prévia de 30 dias para inclusão de novo
suboperador.

**Padrão e fallback não se misturam.** O redline adota um regime ou o outro. Autorização
prévia seguida de "comunicação com direito de objeção" no mesmo dispositivo deixa sem
resposta qual dos dois vale.

**Linha vermelha.** Subcontratação livre; ou dever de informar a cadeia apenas mediante
pedido nosso, que é o mesmo que não informar; ou silêncio sobre cadeia de responsabilidade.

## 4. Transferência internacional

**Padrão.** Tratamento em território nacional. Havendo transferência, ela é declarada no
corpo do contrato, com país de destino, importador identificado e finalidade, para cada
transferência. O fornecedor se obriga a adotar as cláusulas-padrão da Res. CD/ANPD 19/2024,
na íntegra e sem alteração, em instrumento firmado **por ele com cada importador** no
exterior, em prazo certo; a comprovar a adoção à Meridiano, por cópia do instrumento ou por
declaração que o identifique (com cópia sempre que precisarmos dela para atender titular ou
autoridade); e a responder perante a Meridiano pela cadeia. Nova transferência só com nossa
autorização prévia e com o mesmo mecanismo.

**As cláusulas-padrão não vão anexas ao contrato com o fornecedor.** O importador é agente no
exterior e o contrato conosco não é o instrumento da transferência: anexadas a ele, entre
duas partes no Brasil, elas não vinculam importador nenhum (`referencias-normativas`,
`normas/res-19-2024.md`).

**Fallback.** Transferência limitada a componentes acessórios (telemetria, monitoramento,
backup), desde que declarada e amparada da mesma forma, com compromisso de migração para
região nacional em prazo definido, sem custo para a Meridiano, quando ela o pedir. Acesso
remoto a partir do exterior não se resolve com migração de armazenamento: pede plano próprio
de eliminação ou restrição do acesso.

**Linha vermelha.** Transferência que aparece só no anexo técnico e não no corpo. Não é
questão de forma: um contrato que não declara a transferência não permite que a controladora
informe o titular nem demonstre o mecanismo à autoridade. Também é linha vermelha a falta de
obrigação do fornecedor de adotar mecanismo válido com importador em país sem decisão de
adequação: depois de 23/08/2025, é descumprimento presente, e o mecanismo não se negocia.

## 5. Retenção, devolução e eliminação

**Padrão.** No término, devolução em formato estruturado em até 30 dias contados do término e
eliminação comprovada das cópias em até 60 dias contados da devolução ou do fim da transição
assistida, ressalvada conservação por obrigação legal, com acesso restrito e pelo prazo dessa
obrigação. Cada prazo tem termo inicial que corre sozinho: prazo que só começa depois de ato
da Meridiano sem prazo (uma "confirmação de recebimento", por exemplo) pode nunca começar.
Havendo transição assistida, a devolução conta do fim da transição, não do término do
contrato, e alcança o que se gerar durante ela; devolução no meio da transição deixa sem
devolver o que vem depois, e esse resto cai na eliminação.

**Coerência entre retenção e devolução.** Regra de eliminação de dados durante a vigência ou
"no término" não pode tornar impossível a devolução e a transição que dependem desses dados;
a eliminação remete aos prazos da cláusula de término. Dado já incorporado a base ou usado no
treino de modelo não se "elimina como cópia": o remédio é eliminar a base e descartar o
modelo afetado, e o redline diz isso.

**Fallback.** Janela de exportação de 30 dias seguida de eliminação automática, desde que
haja comprovação documental da eliminação.

**Linha vermelha.** Retenção por prazo indeterminado; retenção "para fins de melhoria do
serviço"; ou eliminação sem comprovação.

## 6. Segurança e auditoria

**Padrão.** Medidas descritas no próprio contrato ou em anexo efetivamente entregue, não
apenas remissão genérica a boas práticas: controle de acesso individualizado, criptografia em
trânsito e em repouso, registro de auditoria, segregação por cliente, gestão de
vulnerabilidades. Direito de auditoria anual mediante aviso prévio de prazo expresso, e a
qualquer tempo em caso de incidente. Podemos aceitar, **a nosso critério**, relatório de
terceiro independente (SOC 2 Tipo II, ISO 27001 com escopo aderente) em substituição à
auditoria presencial; a redação nunca transforma essa faculdade em dever de aceitar.

**Medida de quem controla o sistema.** Medida técnica do sistema (criptografia, segregação,
rotina de descarte) cabe a quem o mantém. Quando o fornecedor opera sistema ou base da
Meridiano, o que se exige dele é o que está ao alcance dele: credencial individual, sigilo,
treinamento, cumprimento da nossa política de segurança comunicada por escrito, vedação de
extrair ou copiar dados para fora do sistema.

**Fallback.** Questionário anual respondido pelo fornecedor mais evidência documental dos
controles críticos.

**Linha vermelha.** Ausência de qualquer direito de verificação; ou cláusula que condiciona a
auditoria à concordância do fornecedor caso a caso.

## 7. Direitos do titular e encarregado

**Padrão.** Auxílio no atendimento a requisição de titular em até 5 dias úteis; canal de
contato nominado no contrato; repasse imediato de requisição recebida diretamente pelo
fornecedor.

**Observação que evita achado errado.** Não exigimos que o fornecedor **indique encarregado**:
para operador isso é boa prática, não dever (Res. CD/ANPD 18/2024, art. 6º). Exigimos canal
de interlocução, que é outra coisa.

## 8. Dado sensível

**Padrão.** Tratamento de dado sensível por fornecedor exige cláusula específica, com papéis
declarados, finalidade delimitada, prazo de guarda, medidas reforçadas de segurança e apoio do
fornecedor ao relatório de impacto. Não existe dado sensível "por arrasto" de cláusula
genérica, nem por remissão a anexo que não existe: papéis, finalidade e prazo ficam redigidos
no próprio dispositivo ou em item novo redigido no mesmo ato.

**A base legal não se redige no contrato.** Ela é determinação do controlador, que a registra
no próprio inventário e no relatório de impacto. Em contrato com operador, o operador não tem
o que escolher, e cobrar base legal no texto é erro. Quando o fornecedor for controlador de
parte dos dados (os dos próprios empregados, por exemplo), o contrato pode delimitar a
finalidade dele e vedar hipóteses legais, mas não as escolhe por ele.

**Linha vermelha.** Introdução de tratamento de dado sensível por aditivo, ordem de serviço
ou anexo técnico, sem que a cláusula de proteção de dados do contrato-base seja revista no
mesmo ato.

## 9. Responsabilidade por sanção administrativa

**Padrão.** As perdas decorrentes de sanção administrativa aplicada à Meridiano por fato
imputável ao fornecedor não se sujeitam ao teto de responsabilidade, e ficam expressamente
ressalvadas.

**Fallback.** Teto específico e majorado para esta hipótese, nunca inferior a doze
mensalidades.

**Linha vermelha.** Teto único que engloba sanção administrativa e limita o ressarcimento a
poucas mensalidades. Ver `comercial.md`, item 1, e o cruzamento X-2.
