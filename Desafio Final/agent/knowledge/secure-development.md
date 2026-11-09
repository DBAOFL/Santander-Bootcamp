# Secure Development — Desenvolvimento Seguro

## 1. Objetivo

Este documento estabelece princípios e práticas para incorporar segurança durante todo o ciclo de desenvolvimento de software.

O objetivo é reduzir vulnerabilidades desde a concepção até a implantação e manutenção das aplicações.

Segurança não deve ser tratada como uma etapa isolada ou realizada somente depois que o software estiver pronto.

## 2. Secure Software Development Lifecycle

O Secure Software Development Lifecycle (SSDLC) incorpora atividades de segurança em todas as fases do desenvolvimento.

### 2.1 Planejamento

Identificar:

- Requisitos de segurança.
- Dados sensíveis.
- Usuários e perfis de acesso.
- Dependências externas.
- Restrições regulatórias.
- Riscos do projeto.

### 2.2 Projeto

Considerar:

- Arquitetura segura.
- Separação de responsabilidades.
- Autenticação.
- Autorização.
- Proteção de dados.
- Superfície de ataque.
- Modelagem de ameaças.

### 2.3 Implementação

Aplicar:

- Validação de entradas.
- Codificação segura.
- Tratamento de erros.
- Controle de acesso.
- Gerenciamento de segredos.
- Dependências confiáveis.

### 2.4 Testes

Realizar:

- Revisão de código.
- Testes unitários.
- Testes de integração.
- Análise estática.
- Análise de dependências.
- Testes de segurança autorizados.

### 2.5 Implantação

Verificar:

- Configurações seguras.
- Segredos fora do código.
- HTTPS.
- Permissões.
- Atualizações.
- Logs.
- Monitoramento.

### 2.6 Manutenção

Manter:

- Atualizações de dependências.
- Correções de vulnerabilidades.
- Monitoramento.
- Revisões periódicas.
- Gestão de incidentes.

## 3. Validação de entradas

Toda entrada externa deve ser considerada não confiável.

Fontes comuns:

- Formulários.
- Parâmetros de URL.
- Cabeçalhos HTTP.
- Cookies.
- Arquivos enviados.
- APIs externas.
- Mensagens.
- Dados armazenados anteriormente.

Práticas recomendadas:

- Validar formato.
- Validar tipo.
- Limitar tamanho.
- Verificar intervalos.
- Aplicar listas de valores permitidos quando apropriado.
- Rejeitar entradas incompatíveis com o contrato esperado.

Validação não substitui consultas parametrizadas ou codificação contextual de saída.

## 4. Principais vulnerabilidades de aplicações

### 4.1 SQL Injection

Ocorre quando dados não confiáveis são incorporados indevidamente a comandos SQL.

Prevenção:

- Utilizar consultas parametrizadas.
- Evitar concatenação de entradas em consultas.
- Aplicar privilégios mínimos no banco.
- Validar entradas conforme o contexto.

### 4.2 Cross-Site Scripting (XSS)

Ocorre quando conteúdo não confiável é interpretado como código executável pelo navegador.

Prevenção:

- Codificação contextual de saída.
- Sanitização quando HTML permitido for necessário.
- Content Security Policy.
- Evitar APIs inseguras de manipulação do DOM.

### 4.3 Cross-Site Request Forgery (CSRF)

Ocorre quando um usuário autenticado é induzido a realizar uma ação sem intenção.

Prevenção:

- Tokens anti-CSRF.
- Cookies SameSite.
- Verificação de origem quando apropriada.
- Proteção de operações sensíveis.

### 4.4 Broken Access Control

Ocorre quando usuários conseguem executar ações ou acessar recursos fora das permissões concedidas.

Prevenção:

- Verificação de autorização no servidor.
- Controle de acesso por recurso.
- Princípio do menor privilégio.
- Testes entre diferentes perfis de usuário.

### 4.5 Server-Side Request Forgery (SSRF)

Ocorre quando uma aplicação realiza requisições a destinos não autorizados a partir de entradas controladas externamente.

Prevenção:

- Restringir destinos permitidos.
- Validar endereços e esquemas.
- Controlar redirecionamentos.
- Restringir acesso a redes internas.
- Aplicar controles de saída na infraestrutura.

### 4.6 Path Traversal

Ocorre quando entradas permitem acessar caminhos fora dos diretórios autorizados.

Prevenção:

- Restringir diretórios.
- Canonicalizar caminhos.
- Evitar confiar em nomes de arquivos fornecidos pelo usuário.
- Aplicar permissões mínimas.

### 4.7 Desserialização insegura

Pode permitir execução de comportamentos não esperados quando dados não confiáveis são desserializados de maneira insegura.

Prevenção:

- Preferir formatos simples e seguros.
- Evitar desserialização de objetos arbitrários.
- Validar estruturas.
- Restringir tipos aceitos.

## 5. Autenticação e gerenciamento de sessões

Boas práticas:

- Armazenar senhas utilizando algoritmos apropriados de hashing, como Argon2id.
- Utilizar bibliotecas confiáveis.
- Aplicar políticas adequadas de autenticação.
- Considerar MFA.
- Proteger cookies.
- Renovar identificadores de sessão após autenticação ou mudança de privilégio.
- Encerrar sessões corretamente.
- Aplicar mecanismos de recuperação de conta seguros.

Nunca armazenar senhas em texto puro.

Não utilizar criptografia reversível como substituto de hashing de senhas.

## 6. Gerenciamento de segredos

Segredos incluem:

- Senhas.
- Tokens.
- Chaves de API.
- Chaves privadas.
- Credenciais de banco.
- Certificados.

Boas práticas:

- Não inserir segredos no código-fonte.
- Utilizar variáveis de ambiente ou gerenciadores de segredos.
- Restringir acesso.
- Rotacionar credenciais.
- Evitar registrar segredos em logs.
- Remover credenciais expostas.
- Utilizar arquivos de exemplo sem valores reais.

Arquivos `.env` com credenciais não devem ser publicados em repositórios.

## 7. Criptografia

A criptografia deve ser aplicada conforme o objetivo.

### Dados em trânsito

Utilizar TLS para proteger comunicações.

### Dados armazenados

Avaliar criptografia em repouso para informações sensíveis.

### Senhas

Utilizar algoritmos de hashing específicos para senhas.

### Integridade

Utilizar hashes criptográficos e assinaturas digitais quando apropriado.

Não desenvolver algoritmos criptográficos próprios.

Utilizar bibliotecas reconhecidas e configurações atualizadas.

## 8. Dependências e cadeia de suprimentos

Dependências externas também podem introduzir vulnerabilidades.

Boas práticas:

- Utilizar fontes confiáveis.
- Avaliar a reputação dos pacotes.
- Fixar versões quando apropriado.
- Manter arquivos de lock.
- Monitorar vulnerabilidades conhecidas.
- Remover dependências desnecessárias.
- Verificar integridade e origem dos componentes.
- Atualizar bibliotecas de maneira controlada.

Referências:

- OWASP Software Component Verification Standard.
- OWASP Dependency-Check.
- GitHub Dependabot.
- OSV.

## 9. Configurações seguras

Verificar:

- Serviços desnecessários desabilitados.
- Mensagens de erro sem informações sensíveis.
- Diretórios protegidos.
- Permissões adequadas.
- Interfaces administrativas restritas.
- HTTPS obrigatório quando aplicável.
- Headers de segurança.
- Configurações de produção sem modo debug.

Nunca utilizar configurações de desenvolvimento diretamente em produção sem revisão.

## 10. Logs e monitoramento

Registrar eventos relevantes:

- Falhas de autenticação.
- Alterações de permissões.
- Ações administrativas.
- Erros relevantes.
- Eventos de segurança.
- Alterações em dados críticos.

Evitar registrar:

- Senhas.
- Tokens.
- Chaves privadas.
- Dados pessoais desnecessários.
- Informações confidenciais.

Logs devem possuir controles de acesso, integridade e retenção adequados.

## 11. Segurança no pipeline CI/CD

Integrar verificações de segurança ao processo de desenvolvimento.

Exemplos:

- SAST: análise estática.
- DAST: análise dinâmica.
- SCA: análise de dependências.
- Secret Scanning.
- Testes automatizados.
- Verificação de configurações.
- Revisão de alterações.

Ferramentas devem ser selecionadas conforme o contexto e não substituir revisão técnica.

## 12. Referências

- OWASP Top 10.
- OWASP ASVS.
- OWASP Cheat Sheet Series.
- NIST Secure Software Development Framework (SSDF).
- CWE.
- MITRE ATT&CK.
- SLSA.
- NIST Cryptographic Standards.

## 13. Diretrizes para o agente

Ao revisar um código:

1. Identifique entradas externas.
2. Localize operações sensíveis.
3. Verifique autenticação e autorização.
4. Examine o tratamento de dados.
5. Avalie dependências.
6. Identifique configurações inseguras.
7. Priorize vulnerabilidades.
8. Recomende correções.
9. Explique como validar as alterações.

Não considere a utilização de uma biblioteca como garantia automática de segurança.

Avalie como ela é utilizada e configurada.

Considere sempre a linguagem, o framework, a arquitetura e o ambiente de execução.
