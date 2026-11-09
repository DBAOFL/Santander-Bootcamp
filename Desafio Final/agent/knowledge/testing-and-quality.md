# Testing and Quality — Testes e Qualidade de Software

## 1. Objetivo

Este documento apresenta conceitos, estratégias, metodologias e ferramentas para testes e garantia da qualidade de software.

O objetivo é orientar o agente na criação, execução e avaliação de testes, garantindo que aplicações atendam aos requisitos e apresentem comportamento confiável.

## 2. Fundamentos de testes

Testes de software verificam se um sistema apresenta o comportamento esperado.

Objetivos:

- Identificar defeitos.
- Validar requisitos.
- Prevenir regressões.
- Verificar integrações.
- Avaliar desempenho.
- Identificar problemas de segurança.
- Aumentar a confiabilidade.

Testes reduzem riscos, mas não garantem ausência total de defeitos.

## 3. Pirâmide de testes

A pirâmide de testes representa uma estratégia de distribuição dos testes.

### Testes unitários

Validam pequenas unidades de código isoladamente.

Características:

- Execução rápida.
- Baixo custo.
- Fácil repetição.
- Identificação localizada de problemas.

### Testes de integração

Validam a comunicação entre componentes.

Exemplos:

- Aplicação e banco de dados.
- API e serviços externos.
- Componentes internos.
- Filas de mensagens.

### Testes end-to-end

Validam fluxos completos do ponto de vista do usuário.

Exemplos:

- Cadastro.
- Login.
- Compra.
- Recuperação de senha.

Geralmente possuem maior custo de execução e manutenção.

## 4. Testes unitários

Testes unitários verificam funções, métodos ou componentes individualmente.

Exemplo utilizando Python e pytest:

```python
def calculate_total(price, quantity):
    return price * quantity


def test_calculate_total():
    assert calculate_total(10, 3) == 30
```

Boas práticas:

- Testar uma unidade de comportamento por caso.
- Utilizar nomes descritivos.
- Isolar dependências quando necessário.
- Cobrir casos extremos.
- Testar entradas inválidas.
- Evitar dependência da ordem de execução.

## 5. Testes de integração

Verificam se diferentes componentes funcionam corretamente em conjunto.

Exemplos:

- API conectando ao banco.
- Serviço consumindo mensagens.
- Aplicação utilizando autenticação externa.
- Comunicação entre microsserviços.

Boas práticas:

- Utilizar ambientes controlados.
- Preparar dados de teste.
- Limpar recursos após execução.
- Validar contratos.
- Testar condições de falha.

Ferramentas:

- Testcontainers.
- pytest.
- Supertest.
- JUnit.
- Postman.

## 6. Testes end-to-end

Simulam jornadas completas de utilização.

Exemplo:

1. Acessar a aplicação.
2. Realizar login.
3. Navegar até determinada funcionalidade.
4. Executar uma operação.
5. Verificar o resultado.

Ferramentas:

- Playwright.
- Cypress.
- Selenium.

Boas práticas:

- Testar fluxos críticos.
- Evitar dependência de dados externos instáveis.
- Utilizar seletores confiáveis.
- Evitar excesso de testes redundantes.

## 7. Testes de regressão

Verificam se alterações recentes introduziram problemas em funcionalidades anteriormente existentes.

Boas práticas:

- Manter uma suíte automatizada.
- Testar funcionalidades críticas.
- Reexecutar testes após correções.
- Identificar comportamentos afetados.
- Priorizar fluxos importantes.

## 8. Testes exploratórios

Consistem na investigação ativa de uma aplicação para identificar comportamentos inesperados.

São úteis para descobrir problemas que não foram antecipados nos casos de teste.

Considere:

- Entradas inesperadas.
- Fluxos alternativos.
- Estados inválidos.
- Limites.
- Falhas de integração.
- Comportamentos inesperados.

Registre os passos necessários para reproduzir os problemas encontrados.

## 9. Testes de desempenho

Avaliam o comportamento da aplicação sob diferentes condições de utilização.

### Load Testing

Avalia o comportamento sob carga esperada.

### Stress Testing

Avalia o comportamento além das condições normais de operação.

### Spike Testing

Avalia alterações bruscas de carga.

### Endurance Testing

Avalia o comportamento durante períodos prolongados.

Métricas importantes:

- Latência.
- Throughput.
- Taxa de erros.
- Consumo de CPU.
- Consumo de memória.
- Concorrência.

Ferramentas:

- k6.
- Apache JMeter.
- Locust.
- Gatling.

Os testes devem ser realizados em ambientes autorizados e controlados.

## 10. Testes de segurança

Testes de segurança avaliam se aplicações e sistemas resistem a comportamentos não autorizados.

Áreas importantes:

- Autenticação.
- Autorização.
- Gerenciamento de sessões.
- Validação de entradas.
- Proteção de dados.
- Configurações.
- Dependências.
- Controle de acesso.

Ferramentas:

- OWASP ZAP.
- Burp Suite.
- Semgrep.
- Bandit.
- Trivy.
- Nmap.

A execução de testes deve respeitar escopo e autorização.

## 11. Testes de API

Verificam o comportamento dos endpoints.

Considere:

- Métodos HTTP.
- Códigos de resposta.
- Validação de entradas.
- Autenticação.
- Autorização.
- Tratamento de erros.
- Paginação.
- Limites.
- Concorrência.

Teste também situações negativas, não apenas operações bem-sucedidas.

## 12. Testes de banco de dados

Verificam integridade, consistência e comportamento das operações de persistência.

Considere:

- Constraints.
- Relacionamentos.
- Transações.
- Rollback.
- Concorrência.
- Migrações.
- Consultas.
- Permissões.

Utilize bancos de teste isolados.

Evite executar testes destrutivos em ambientes de produção.

## 13. Testes de propriedades e fuzzing

### Property-Based Testing

Verifica propriedades que devem permanecer verdadeiras para diferentes entradas.

Ferramentas:

- Hypothesis.
- QuickCheck.
- fast-check.

### Fuzz Testing

Utiliza entradas variadas ou inesperadas para identificar comportamentos incorretos.

É especialmente útil para:

- Parsers.
- Processamento de arquivos.
- Protocolos.
- Bibliotecas.
- Interfaces que recebem dados não confiáveis.

Ferramentas:

- AFL++.
- libFuzzer.
- OSS-Fuzz.

Execute fuzzing em ambientes isolados e controlados.

## 14. Cobertura de testes

Cobertura mede quais partes do código foram executadas durante os testes.

Métricas:

- Statement Coverage.
- Branch Coverage.
- Function Coverage.
- Line Coverage.

Ferramentas:

- coverage.py.
- JaCoCo.
- Istanbul.
- c8.
- gcov.

Cobertura elevada não significa necessariamente boa qualidade.

A qualidade dos cenários e das verificações é mais importante do que atingir uma porcentagem arbitrária.

## 15. Testes automatizados em CI/CD

Pipelines podem executar automaticamente:

1. Lint.
2. Formatação.
3. Análise estática.
4. Testes unitários.
5. Testes de integração.
6. Análise de dependências.
7. Verificações de segurança.
8. Build.
9. Testes adicionais.

Exemplos de plataformas:

- GitHub Actions.
- GitLab CI/CD.
- Jenkins.
- Azure Pipelines.
- CircleCI.

Falhas em verificações importantes devem impedir a promoção de alterações quando essa política estiver definida no projeto.

## 16. Qualidade de código

Ferramentas de análise:

### Python

- Ruff.
- Pylint.
- mypy.
- Bandit.

### JavaScript e TypeScript

- ESLint.
- Prettier.
- TypeScript Compiler.

### C e C++

- Clang-Tidy.
- Cppcheck.
- GCC Warnings.
- Clang Static Analyzer.

### Java

- Checkstyle.
- SpotBugs.
- PMD.
- SonarQube.

As ferramentas devem ser configuradas de acordo com a linguagem e os padrões do projeto.

## 17. Testes e desenvolvimento seguro

Os testes devem considerar requisitos de segurança.

Exemplos:

- Usuários não autorizados não acessam recursos protegidos.
- Entradas inválidas são rejeitadas.
- Dados sensíveis não aparecem em respostas indevidas.
- Operações críticas exigem autorização.
- Erros não revelam informações internas.
- Consultas não permitem manipulação por entradas externas.

Quando uma vulnerabilidade for corrigida, crie um teste de regressão sempre que possível.

## 18. Processo de correção de defeitos

Ao identificar um defeito:

1. Reproduza o problema.
2. Registre as condições.
3. Identifique a causa.
4. Avalie o impacto.
5. Implemente a correção.
6. Crie ou atualize testes.
7. Execute a suíte relevante.
8. Verifique possíveis regressões.
9. Documente o resultado.

Evite corrigir apenas o sintoma quando a causa raiz puder ser identificada.

## 19. Diretrizes para o agente

Ao testar ou avaliar um projeto:

1. Identifique os requisitos.
2. Compreenda o comportamento esperado.
3. Analise os testes existentes.
4. Identifique áreas sem cobertura adequada.
5. Recomende cenários relevantes.
6. Teste casos de sucesso.
7. Teste casos de falha.
8. Considere segurança.
9. Avalie resultados.
10. Registre defeitos.
11. Sugira correções.
12. Verifique regressões.

Não invente resultados de testes que não foram executados.

Diferencie testes realizados, testes recomendados e testes impossíveis de executar no ambiente disponível.

## 20. Referências

- ISTQB: https://www.istqb.org/
- pytest: https://docs.pytest.org/
- JUnit: https://junit.org/
- Playwright: https://playwright.dev/
- Cypress: https://www.cypress.io/
- k6: https://grafana.com/docs/k6/latest/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- Google Testing Blog: https://testing.googleblog.com/

