# Security Basics — Fundamentos de Segurança da Informação

## 1. Objetivo

Este documento apresenta os fundamentos de segurança da informação, conceitos de vulnerabilidades, ameaças, riscos, impactos e boas práticas.

O objetivo é orientar o agente na identificação, compreensão e avaliação de problemas de segurança em aplicações, sistemas, redes e infraestrutura.

## 2. Segurança da informação

Segurança da informação busca proteger dados e sistemas contra acessos, modificações, destruição e indisponibilidade não autorizados.

Seus principais objetivos são representados pela tríade CIA:

- Confidentiality (Confidencialidade).
- Integrity (Integridade).
- Availability (Disponibilidade).

## 3. Tríade CIA

### 3.1. Confidencialidade

Garante que informações sejam acessadas apenas por pessoas ou sistemas autorizados.

Exemplos de controles:

- Criptografia.
- Controle de acesso.
- Autenticação.
- Gerenciamento de permissões.
- Proteção de credenciais.

Exemplo de violação:

Um usuário consegue visualizar dados pessoais de outros usuários sem autorização.

### 3.2. Integridade

Garante que informações não sejam modificadas indevidamente.

Exemplos de controles:

- Hashes.
- Assinaturas digitais.
- Controle de alterações.
- Logs.
- Validação de dados.
- Controle de acesso à escrita.

Exemplo de violação:

Um usuário modifica registros financeiros sem possuir autorização.

### 3.3. Disponibilidade

Garante que sistemas e informações estejam acessíveis quando necessários.

Exemplos de controles:

- Backups.
- Redundância.
- Monitoramento.
- Balanceamento de carga.
- Proteção contra DoS.
- Planos de recuperação.

Exemplo de violação:

Um serviço fica indisponível devido a um ataque ou falha de infraestrutura.

## 4. Conceitos fundamentais

### 4.1. Ativo

Qualquer recurso que possua valor para uma organização.

Exemplos:

- Dados.
- Aplicações.
- Servidores.
- Redes.
- Credenciais.
- Infraestrutura.
- Propriedade intelectual.

### 4.2. Ameaça

Qualquer circunstância ou agente capaz de causar danos a um ativo.

Exemplos:

- Atacantes.
- Malware.
- Erros humanos.
- Falhas de hardware.
- Desastres naturais.
- Ameaças internas.

### 4.3. Vulnerabilidade

Fraqueza em um sistema, processo, configuração ou controle que pode ser explorada.

Exemplos:

- Software desatualizado.
- Senhas fracas.
- SQL Injection.
- Permissões excessivas.
- Configurações inseguras.
- Falta de validação.

### 4.4. Exploração

Aproveitamento de uma vulnerabilidade para produzir um comportamento não autorizado ou prejudicial.

### 4.5. Risco

Representa a possibilidade de um evento de segurança causar determinado impacto.

Uma avaliação simplificada considera:

- Probabilidade.
- Impacto.

A fórmula Probabilidade × Impacto pode ser utilizada como modelo qualitativo ou quantitativo, desde que os critérios sejam definidos.

### 4.6. Impacto

Consequência potencial de um incidente.

Pode envolver:

- Perda financeira.
- Exposição de dados.
- Interrupção de serviços.
- Danos reputacionais.
- Consequências legais.
- Comprometimento de sistemas.

## 5. Avaliação de riscos

A avaliação de riscos deve considerar:

1. Ativos envolvidos.
2. Ameaças relevantes.
3. Vulnerabilidades identificadas.
4. Probabilidade de ocorrência.
5. Impacto potencial.
6. Controles existentes.
7. Risco residual.

### Classificação de severidade

Uma classificação simplificada:

- Crítica: possibilidade de comprometimento grave de ativos ou operações essenciais.
- Alta: impacto significativo sobre segurança ou funcionamento.
- Média: impacto moderado e limitado.
- Baixa: impacto reduzido.
- Informativa: observação sem risco relevante identificado.

A classificação deve ser justificada por evidências e contexto.

Não classifique automaticamente uma vulnerabilidade como crítica apenas pelo nome da técnica envolvida.

## 6. Vulnerabilidades comuns

### SQL Injection

Ocorre quando entradas não confiáveis interferem na estrutura de consultas SQL.

Prevenção:

- Consultas parametrizadas.
- Validação de entradas.
- Menor privilégio.
- Revisão de consultas.

### Cross-Site Scripting (XSS)

Ocorre quando conteúdo não confiável é interpretado como código executável pelo navegador.

Prevenção:

- Codificação contextual de saída.
- Sanitização quando apropriada.
- Content Security Policy.
- Evitar inserção insegura de HTML.

### Cross-Site Request Forgery (CSRF)

Ocorre quando um navegador autenticado é induzido a realizar ações não desejadas.

Prevenção:

- Tokens CSRF.
- Cookies SameSite.
- Verificação de origem.
- Proteção de operações sensíveis.

### Broken Access Control

Ocorre quando controles de autorização são insuficientes.

Prevenção:

- Verificação de permissões no servidor.
- Menor privilégio.
- Controle de acesso por recurso.
- Testes de autorização.

### Command Injection

Ocorre quando entradas não confiáveis influenciam a execução de comandos do sistema.

Prevenção:

- Evitar execução de comandos externos quando possível.
- Utilizar APIs específicas.
- Validar entradas.
- Separar argumentos de comandos.
- Aplicar menor privilégio.

### Path Traversal

Ocorre quando entradas permitem acessar arquivos fora do diretório autorizado.

Prevenção:

- Normalização de caminhos.
- Restrições de diretório.
- Validação de nomes.
- Controle de permissões.

### SSRF

Server-Side Request Forgery ocorre quando um sistema é induzido a realizar requisições para destinos não autorizados.

Prevenção:

- Restringir destinos.
- Validar URLs.
- Bloquear endereços internos quando não necessários.
- Controlar redirecionamentos.
- Aplicar políticas de saída de rede.

## 7. Autenticação e autorização

### Autenticação

Verifica a identidade de um usuário ou sistema.

Mecanismos:

- Senhas.
- MFA.
- Certificados.
- Tokens.
- Biometria.

### Autorização

Define o que uma identidade autenticada pode realizar.

Modelos:

- RBAC.
- ABAC.
- ACL.

Boas práticas:

- Menor privilégio.
- Separação de funções.
- Revisão periódica de permissões.
- Revogação de acessos desnecessários.
- Proteção de sessões.

## 8. Criptografia

Criptografia protege informações por meio de transformações matemáticas.

Categorias:

### Criptografia simétrica

Utiliza uma chave compartilhada.

Exemplo:

- AES.

### Criptografia assimétrica

Utiliza pares de chaves.

Exemplos:

- RSA.
- Ed25519.
- ECDSA.

### Hashing

Transforma dados em representações de tamanho definido.

Exemplos:

- SHA-256.
- SHA-3.

Hashing não é equivalente a criptografia reversível.

### Armazenamento de senhas

Utilize algoritmos específicos para hashing de senhas:

- Argon2id.
- bcrypt.
- scrypt.

Utilize salt adequado e parâmetros atualizados.

Nunca armazene senhas em texto puro.

## 9. Segurança de redes

Conceitos importantes:

- TCP/IP.
- DNS.
- HTTP/HTTPS.
- TLS.
- Firewall.
- VPN.
- IDS.
- IPS.
- Segmentação de rede.
- Proxy.

Boas práticas:

- Restringir portas.
- Minimizar serviços expostos.
- Utilizar criptografia.
- Monitorar tráfego.
- Segmentar ambientes.
- Atualizar equipamentos.
- Restringir acesso administrativo.

## 10. Gestão de vulnerabilidades

Um processo de gestão de vulnerabilidades inclui:

1. Identificação de ativos.
2. Descoberta de vulnerabilidades.
3. Validação.
4. Avaliação de impacto.
5. Priorização.
6. Correção.
7. Verificação.
8. Registro.

Ferramentas comuns:

- OWASP ZAP.
- Nmap.
- Trivy.
- Semgrep.
- Bandit.
- Dependabot.
- OpenVAS.

A utilização deve respeitar autorização e escopo.

## 11. Defesa em profundidade

Defesa em profundidade utiliza múltiplas camadas de proteção.

Exemplos:

- Firewall.
- Autenticação multifator.
- Segmentação.
- Criptografia.
- Monitoramento.
- Backups.
- Controle de acesso.
- Atualizações.
- Treinamento.

Uma única medida de segurança não deve ser considerada suficiente para proteger sistemas importantes.

## 12. Princípios de segurança

### Least Privilege

Conceda apenas as permissões necessárias.

### Defense in Depth

Utilize múltiplas camadas de proteção.

### Secure by Default

Adote configurações seguras como padrão.

### Fail Securely

Falhas não devem conceder acesso indevido.

### Zero Trust

Não confie automaticamente em usuários, dispositivos ou redes apenas por sua localização.

Verifique identidade, contexto e autorização continuamente conforme o risco.

## 13. Resposta a incidentes

Etapas comuns:

1. Preparação.
2. Identificação.
3. Contenção.
4. Erradicação.
5. Recuperação.
6. Lições aprendidas.

Registre evidências e preserve informações relevantes.

Evite alterações desnecessárias em sistemas comprometidos antes da coleta adequada de evidências.

## 14. Diretrizes para o agente

Ao analisar problemas de segurança:

1. Identifique os ativos envolvidos.
2. Compreenda o contexto.
3. Identifique ameaças.
4. Identifique vulnerabilidades.
5. Avalie probabilidade.
6. Avalie impacto.
7. Determine severidade.
8. Identifique controles existentes.
9. Recomende correções.
10. Sugira validação.
11. Explique riscos residuais.

Não confunda vulnerabilidade, ameaça, impacto e risco.

Diferencie fatos comprovados de hipóteses.

Nunca execute testes em sistemas de terceiros sem autorização explícita.

## 15. Referências

- OWASP: https://owasp.org/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- MITRE ATT&CK: https://attack.mitre.org/
- CWE: https://cwe.mitre.org/
- CVE: https://www.cve.org/
- CVSS: https://www.first.org/cvss/
- CIS Controls: https://www.cisecurity.org/controls

