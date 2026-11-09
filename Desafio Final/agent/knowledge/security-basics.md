# Security Basics — Fundamentos de Cibersegurança

## 1. Objetivo

Este documento estabelece os fundamentos de segurança da informação que devem orientar as análises, recomendações e decisões do agente.

O objetivo é fornecer uma base conceitual para compreender ameaças, vulnerabilidades, riscos, ataques e mecanismos de proteção.

O agente deve utilizar estes conhecimentos para contextualizar problemas de segurança e explicar suas consequências.

## 2. Conceitos fundamentais

### 2.1 Ativo

Um ativo é qualquer recurso que possua valor para uma organização ou indivíduo.

Exemplos:

- Informações e documentos.
- Bancos de dados.
- Aplicações.
- Servidores.
- Infraestrutura de rede.
- Credenciais.
- Propriedade intelectual.
- Serviços digitais.

A proteção deve considerar o valor e a importância de cada ativo.

### 2.2 Ameaça

Uma ameaça é uma circunstância, evento ou agente capaz de provocar danos a um ativo.

Exemplos:

- Atacantes externos.
- Funcionários mal-intencionados.
- Malware.
- Engenharia social.
- Falhas humanas.
- Desastres naturais.
- Interrupções de infraestrutura.

Uma ameaça representa uma possibilidade de dano, não necessariamente uma vulnerabilidade existente.

### 2.3 Vulnerabilidade

Uma vulnerabilidade é uma fraqueza em um sistema, processo, aplicação ou configuração que pode ser explorada por uma ameaça.

Exemplos:

- SQL Injection.
- Cross-Site Scripting (XSS).
- Senhas fracas.
- Sistemas desatualizados.
- Permissões excessivas.
- Configurações inseguras.
- Falhas de validação de entrada.

Uma vulnerabilidade pode existir sem que tenha sido explorada.

### 2.4 Exploração

Exploração é o aproveitamento de uma vulnerabilidade para produzir um efeito não autorizado ou indesejado.

A exploração pode resultar em:

- Acesso não autorizado.
- Exposição de informações.
- Modificação de dados.
- Elevação de privilégios.
- Interrupção de serviços.

A existência de uma vulnerabilidade não significa que sua exploração seja necessariamente simples ou viável.

### 2.5 Risco

Risco é a possibilidade de ocorrência de consequências negativas decorrentes de uma ameaça que possa explorar uma vulnerabilidade.

Sua avaliação deve considerar:

- Probabilidade.
- Impacto.
- Exposição.
- Controles existentes.
- Contexto do ambiente.

Uma vulnerabilidade não deve ser classificada automaticamente como crítica sem considerar esses fatores.

## 3. Tríade CIA

A tríade CIA representa três princípios fundamentais da segurança da informação.

### 3.1 Confidencialidade (Confidentiality)

Garante que informações sejam acessadas somente por pessoas, sistemas ou processos autorizados.

Exemplos de mecanismos:

- Controle de acesso.
- Criptografia.
- Autenticação.
- Gerenciamento de permissões.
- Classificação de informações.

Uma violação de confidencialidade pode resultar no vazamento de dados pessoais, credenciais ou informações comerciais.

### 3.2 Integridade (Integrity)

Garante que informações permaneçam corretas, completas e protegidas contra alterações não autorizadas.

Exemplos de mecanismos:

- Hashes criptográficos.
- Assinaturas digitais.
- Controle de alterações.
- Logs de auditoria.
- Restrições de escrita.
- Validação de dados.

Uma violação de integridade pode provocar alterações indevidas em registros financeiros, configurações ou informações de usuários.

### 3.3 Disponibilidade (Availability)

Garante que sistemas e informações estejam acessíveis quando necessários.

Exemplos de mecanismos:

- Backups.
- Redundância.
- Monitoramento.
- Balanceamento de carga.
- Planos de recuperação.
- Proteção contra negação de serviço.

Uma violação de disponibilidade pode impedir usuários legítimos de utilizar um sistema.

### 3.4 Equilíbrio da tríade

Os três princípios devem ser considerados em conjunto.

Uma solução que prioriza exclusivamente a confidencialidade pode comprometer a disponibilidade se implementar controles excessivamente restritivos.

O agente deve considerar o equilíbrio entre segurança, funcionalidade e necessidades operacionais.

## 4. Autenticidade, autenticação e autorização

### Autenticidade

Propriedade que permite verificar se uma entidade, informação ou comunicação corresponde à origem declarada.

### Autenticação

Processo de verificar a identidade de um usuário ou sistema.

Fatores de autenticação:

- Algo que você sabe: senha ou PIN.
- Algo que você possui: token ou dispositivo.
- Algo que você é: característica biométrica.

A autenticação multifator combina fatores de categorias diferentes.

### Autorização

Processo de determinar quais recursos e operações uma identidade autenticada pode utilizar.

Autenticação responde quem é você.

Autorização responde o que você pode fazer.

Um sistema pode autenticar corretamente um usuário e ainda apresentar falhas de autorização.

## 5. Princípios de segurança

### Princípio do menor privilégio

Cada usuário, processo ou serviço deve possuir somente as permissões necessárias para executar suas funções.

### Defesa em profundidade

Utilizar múltiplas camadas de proteção, evitando depender de um único mecanismo de segurança.

### Segurança por padrão

Configurações iniciais devem priorizar opções seguras.

### Segurança desde o projeto

A segurança deve ser considerada desde as primeiras etapas do desenvolvimento.

### Redução da superfície de ataque

Desabilitar serviços, funcionalidades e acessos desnecessários.

### Fail Secure

Quando ocorre uma falha, o sistema deve evitar conceder acesso indevido.

O comportamento seguro deve ser definido considerando os requisitos de disponibilidade e operação.

## 6. Classificação de informações

Informações podem ser classificadas conforme sua sensibilidade.

Exemplo:

- Pública: pode ser divulgada livremente.
- Interna: destinada ao uso interno.
- Confidencial: acesso restrito.
- Sensível: exige controles reforçados.

A classificação deve orientar armazenamento, compartilhamento, transmissão e descarte.

## 7. Principais categorias de ameaças

### Malware

Software desenvolvido para executar atividades maliciosas.

Categorias:

- Vírus.
- Worms.
- Trojans.
- Ransomware.
- Spyware.
- Rootkits.
- Keyloggers.

### Engenharia social

Manipulação de pessoas para obter informações ou induzir ações.

Exemplos:

- Phishing.
- Spear phishing.
- Pretexting.
- Baiting.

### Ataques a aplicações

Exploram falhas no desenvolvimento ou na configuração de aplicações.

Exemplos:

- SQL Injection.
- XSS.
- CSRF.
- SSRF.
- Path Traversal.
- Broken Access Control.

### Ataques à disponibilidade

Procuram comprometer o funcionamento de serviços.

Exemplos:

- DoS.
- DDoS.
- Exaustão de recursos.

## 8. Avaliação de riscos

Uma avaliação de riscos deve considerar pelo menos:

- Ativo afetado.
- Ameaça relevante.
- Vulnerabilidade.
- Probabilidade.
- Impacto.
- Controles existentes.
- Risco residual.

Uma matriz qualitativa pode utilizar:

| Probabilidade | Impacto | Prioridade indicativa |
|---|---|---|
| Alta | Alto | Crítica |
| Alta | Médio | Alta |
| Média | Alto | Alta |
| Média | Médio | Média |
| Baixa | Baixo | Baixa |

Essa matriz é apenas uma referência inicial. A classificação deve considerar o contexto e não substituir uma metodologia formal.

## 9. Referências técnicas

O agente deve considerar, quando pertinente:

- ISO/IEC 27001: Sistema de Gestão de Segurança da Informação.
- ISO/IEC 27002: Controles de segurança da informação.
- NIST Cybersecurity Framework.
- NIST SP 800-53: Controles de segurança e privacidade.
- OWASP: Segurança de aplicações.
- MITRE ATT&CK: Táticas e técnicas de adversários.
- CWE: Classificação de fraquezas de software.
- CVE: Identificação de vulnerabilidades conhecidas.
- CVSS: Avaliação da severidade de vulnerabilidades.

## 10. Diretrizes para o agente

Ao analisar um problema:

1. Identifique os ativos envolvidos.
2. Determine quais propriedades de segurança podem ser afetadas.
3. Diferencie ameaça, vulnerabilidade e risco.
4. Identifique os controles existentes.
5. Avalie impacto e probabilidade.
6. Justifique a classificação.
7. Recomende medidas proporcionais ao risco.

Não confunda vulnerabilidade com incidente de segurança.

Não presuma que toda falha representa uma exploração confirmada.

Diferencie claramente fatos observados, hipóteses e possibilidades.
