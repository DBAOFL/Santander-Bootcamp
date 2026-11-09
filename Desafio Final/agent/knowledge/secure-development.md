# Secure Development — Desenvolvimento Seguro

## 1. Objetivo

Este documento apresenta princípios, práticas e técnicas para desenvolver software seguro desde a concepção até a manutenção.

O objetivo é orientar o agente na identificação e prevenção de vulnerabilidades durante todo o ciclo de desenvolvimento.

A segurança deve ser considerada parte da engenharia de software, não uma etapa isolada realizada somente antes da publicação.

## 2. Secure Software Development Lifecycle

O Secure Software Development Lifecycle (SSDLC) integra segurança às etapas do desenvolvimento.

Etapas:

1. Planejamento.
2. Levantamento de requisitos.
3. Arquitetura e design.
4. Implementação.
5. Testes.
6. Implantação.
7. Monitoramento.
8. Manutenção.

Cada etapa deve considerar riscos e controles apropriados.

## 3. Security by Design

Security by Design significa considerar segurança desde o planejamento da solução.

Boas práticas:

- Identificar ativos sensíveis.
- Definir requisitos de segurança.
- Avaliar ameaças.
- Reduzir superfícies de ataque.
- Aplicar menor privilégio.
- Definir controles de autenticação.
- Planejar proteção de dados.
- Considerar recuperação de incidentes.

Não deixe decisões críticas de segurança para depois da implementação.

## 4. Security by Default

Sistemas devem apresentar configurações seguras por padrão.

Exemplos:

- Contas sem privilégios administrativos desnecessários.
- Portas e serviços desnecessários desabilitados.
- Recursos privados por padrão.
- Proteção de informações sensíveis.
- Autenticação obrigatória quando necessária.
- Mensagens de erro sem detalhes internos.

O usuário deve precisar justificar explicitamente a habilitação de funcionalidades que aumentem significativamente o risco.

## 5. Modelagem de ameaças

Threat Modeling é o processo de identificar ameaças potenciais antes ou durante o desenvolvimento.

Etapas:

1. Identificar componentes.
2. Mapear fluxos de dados.
3. Identificar fronteiras de confiança.
4. Identificar ativos.
5. Identificar ameaças.
6. Avaliar riscos.
7. Definir contramedidas.
8. Revisar a arquitetura.

### STRIDE

Modelo utilizado para categorizar ameaças.

- Spoofing: falsificação de identidade.
- Tampering: adulteração de dados.
- Repudiation: impossibilidade de comprovar ações.
- Information Disclosure: exposição de informações.
- Denial of Service: indisponibilidade.
- Elevation of Privilege: elevação indevida de privilégios.

STRIDE ajuda a organizar a análise, mas não substitui uma avaliação contextual.

## 6. Validação de entradas

Toda entrada externa deve ser considerada não confiável.

Fontes comuns:

- Formulários.
- APIs.
- Arquivos.
- Parâmetros de URL.
- Cookies.
- Cabeçalhos HTTP.
- Integrações externas.
- Mensagens de filas.

Boas práticas:

- Validar tipos.
- Restringir formatos.
- Definir limites.
- Verificar tamanhos.
- Rejeitar valores inesperados.
- Utilizar listas permitidas quando apropriado.

Validação de entrada não substitui codificação de saída ou consultas parametrizadas.

## 7. Prevenção de vulnerabilidades

### SQL Injection

Utilize consultas parametrizadas.

Nunca concatene entradas não confiáveis diretamente em comandos SQL.

### XSS

Utilize codificação contextual de saída e evite inserção insegura de conteúdo HTML.

### Command Injection

Evite executar comandos do sistema com entradas externas.

Prefira APIs específicas e argumentos separados.

### Path Traversal

Restrinja acesso a diretórios autorizados e normalize caminhos.

### SSRF

Controle destinos de requisições externas e bloqueie acessos não autorizados a redes internas.

### Broken Access Control

Verifique autorização no servidor para cada operação e recurso.

### Insecure Deserialization

Evite desserializar dados não confiáveis utilizando mecanismos inseguros.

## 8. Autenticação

A autenticação deve identificar corretamente usuários e sistemas.

Boas práticas:

- Utilizar mecanismos modernos.
- Proteger credenciais.
- Implementar MFA quando apropriado.
- Limitar tentativas de autenticação.
- Utilizar armazenamento seguro de senhas.
- Proteger sessões.
- Implementar revogação de credenciais.

Nunca implemente mecanismos criptográficos próprios sem justificativa técnica excepcional.

## 9. Autorização

A autorização deve determinar quais operações cada identidade pode realizar.

Boas práticas:

- Aplicar menor privilégio.
- Verificar permissões no servidor.
- Evitar confiar em identificadores fornecidos pelo cliente.
- Validar propriedade de recursos.
- Separar funções administrativas.
- Revisar permissões regularmente.

Não considere que esconder um botão no frontend constitui controle de acesso.

## 10. Proteção de dados

Considere:

- Classificação de informações.
- Minimização de dados.
- Criptografia em trânsito.
- Criptografia em repouso.
- Retenção adequada.
- Controle de acesso.
- Anonimização quando apropriada.
- Descarte seguro.

Dados sensíveis não devem ser incluídos indiscriminadamente em logs.

## 11. Gerenciamento de segredos

Segredos incluem:

- API Keys.
- Tokens.
- Senhas.
- Chaves privadas.
- Credenciais de banco.
- Certificados.

Boas práticas:

- Não armazenar segredos no código-fonte.
- Não versionar arquivos com credenciais.
- Utilizar variáveis de ambiente ou gerenciadores de segredos.
- Restringir permissões.
- Rotacionar credenciais.
- Revogar credenciais expostas.
- Evitar registrar segredos em logs.

Exemplos de ferramentas:

- HashiCorp Vault.
- AWS Secrets Manager.
- Azure Key Vault.
- Google Secret Manager.

## 12. Dependências e Supply Chain Security

Dependências externas podem introduzir vulnerabilidades e riscos de cadeia de suprimentos.

Boas práticas:

- Avaliar a procedência dos pacotes.
- Utilizar versões controladas.
- Verificar vulnerabilidades conhecidas.
- Remover dependências desnecessárias.
- Monitorar atualizações.
- Utilizar arquivos de lock.
- Revisar scripts de instalação.
- Considerar integridade dos artefatos.

Ferramentas:

- Dependabot.
- Renovate.
- Snyk.
- Trivy.
- OWASP Dependency-Check.
- OSV Scanner.

## 13. DevSecOps

DevSecOps integra segurança ao ciclo de desenvolvimento e operação.

Práticas:

- Security as Code.
- Infraestrutura como código.
- Análise estática.
- Análise de dependências.
- Testes automatizados.
- Revisão de alterações.
- Monitoramento contínuo.
- Gestão de vulnerabilidades.

### CI/CD

Pipelines podem incluir:

- SAST.
- SCA.
- Secret Scanning.
- DAST.
- Testes automatizados.
- Verificação de configurações.

Os controles devem ser proporcionais ao risco do projeto.

## 14. Ferramentas de segurança

### SAST

Analisa código-fonte ou artefatos sem executar a aplicação.

Exemplos:

- Semgrep.
- SonarQube.
- CodeQL.
- Bandit.

### DAST

Avalia aplicações em execução.

Exemplos:

- OWASP ZAP.
- Burp Suite.

### SCA

Analisa dependências e componentes de terceiros.

Exemplos:

- Trivy.
- Snyk.
- OWASP Dependency-Check.

### Secret Scanning

Identifica possíveis segredos expostos.

Exemplos:

- Gitleaks.
- TruffleHog.

## 15. Revisão de código segura

Uma revisão de segurança deve considerar:

- Validação de entradas.
- Autenticação.
- Autorização.
- Gerenciamento de sessões.
- Manipulação de arquivos.
- Consultas ao banco.
- Execução de comandos.
- Criptografia.
- Dependências.
- Tratamento de erros.
- Logs.
- Configurações.

Cada achado deve apresentar evidências e contexto.

## 16. Segurança em infraestrutura

Considere:

- Configurações de rede.
- Firewall.
- Permissões.
- Isolamento de serviços.
- Containers.
- Segredos.
- Atualizações.
- Logs.
- Backups.
- Monitoramento.

Não assuma que uma aplicação está segura apenas porque seu código não apresenta vulnerabilidades evidentes.

## 17. Resposta a vulnerabilidades

Ao identificar uma vulnerabilidade:

1. Documente o problema.
2. Identifique os componentes afetados.
3. Avalie impacto.
4. Determine severidade.
5. Recomende correção.
6. Planeje validação.
7. Verifique possíveis efeitos colaterais.
8. Registre o resultado.

Uma correção deve resolver a causa raiz, não apenas ocultar o comportamento observado.

## 18. Diretrizes para o agente

Ao desenvolver ou revisar software:

1. Compreenda o contexto.
2. Identifique os ativos.
3. Avalie a arquitetura.
4. Considere ameaças.
5. Verifique entradas externas.
6. Analise autenticação e autorização.
7. Avalie dependências.
8. Verifique exposição de segredos.
9. Recomende controles proporcionais.
10. Priorize vulnerabilidades por risco.
11. Explique as correções.
12. Sugira testes de validação.

Não realize testes intrusivos sem autorização e escopo definidos.

Ao propor comandos ou alterações em infraestrutura, identifique possíveis impactos antes da execução.

## 19. Referências

- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- NIST SSDF: https://csrc.nist.gov/Projects/ssdf
- MITRE CWE: https://cwe.mitre.org/
- Microsoft SDL: https://www.microsoft.com/en-us/securityengineering/sdl

