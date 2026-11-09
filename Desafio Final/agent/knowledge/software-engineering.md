# Software Engineering — Engenharia de Software

## 1. Objetivo

Este documento apresenta fundamentos, processos, metodologias e práticas de engenharia de software.

O objetivo é orientar o agente no planejamento, desenvolvimento, manutenção e evolução de sistemas, considerando qualidade, organização, colaboração e eficiência.

## 2. Conceitos fundamentais

Engenharia de software aplica princípios sistemáticos ao desenvolvimento e manutenção de sistemas.

Seu objetivo é produzir software que atenda aos requisitos, seja confiável e possa evoluir de maneira sustentável.

Áreas importantes:

- Levantamento de requisitos.
- Arquitetura.
- Desenvolvimento.
- Testes.
- Qualidade.
- Segurança.
- Gerenciamento de projetos.
- Manutenção.
- Documentação.

## 3. Ciclo de vida do software

O ciclo de vida de desenvolvimento de software (SDLC) organiza as etapas necessárias para criar e manter um sistema.

Etapas comuns:

1. Planejamento.
2. Levantamento de requisitos.
3. Análise.
4. Projeto.
5. Implementação.
6. Testes.
7. Implantação.
8. Operação.
9. Manutenção.

O processo pode ser iterativo ou sequencial.

## 4. Engenharia de requisitos

Requisitos definem as necessidades e expectativas do sistema.

### Requisitos funcionais

Descrevem funcionalidades.

Exemplos:

- Cadastro de usuários.
- Login.
- Gerenciamento de produtos.
- Processamento de pagamentos.

### Requisitos não funcionais

Descrevem características e restrições.

Exemplos:

- Segurança.
- Desempenho.
- Disponibilidade.
- Escalabilidade.
- Usabilidade.
- Manutenibilidade.

### Boas práticas

- Identifique stakeholders.
- Faça perguntas quando houver ambiguidades.
- Documente requisitos.
- Defina critérios de aceitação.
- Identifique dependências.
- Registre restrições.
- Valide expectativas.

Não comece uma implementação complexa quando requisitos essenciais ainda estiverem indefinidos.

## 5. Metodologias de desenvolvimento

### Waterfall

Modelo sequencial em etapas.

Características:

- Planejamento antecipado.
- Fases definidas.
- Documentação.
- Controle formal de mudanças.

Pode ser adequado quando requisitos e restrições são relativamente estáveis.

### Agile

Abordagem iterativa e incremental.

Princípios:

- Colaboração.
- Entregas frequentes.
- Adaptação.
- Feedback.
- Melhoria contínua.

### Scrum

Framework ágil baseado em ciclos chamados Sprints.

Elementos:

- Product Backlog.
- Sprint Backlog.
- Sprint.
- Product Owner.
- Scrum Master.
- Developers.

### Kanban

Método de gestão visual do fluxo de trabalho.

Conceitos:

- Backlog.
- To Do.
- In Progress.
- Review.
- Done.
- Work in Progress Limits.

Escolha práticas conforme as necessidades da equipe.

## 6. Planejamento de projetos

Um planejamento adequado deve considerar:

- Objetivo.
- Escopo.
- Requisitos.
- Entregáveis.
- Dependências.
- Recursos.
- Riscos.
- Prazos.
- Critérios de conclusão.

Divida objetivos grandes em tarefas menores e verificáveis.

Evite estimativas excessivamente precisas quando houver muitas incertezas.

## 7. Controle de versão

Git é uma ferramenta amplamente utilizada para controle de versão.

Conceitos:

- Repository.
- Commit.
- Branch.
- Merge.
- Pull Request.
- Rebase.
- Tag.

Boas práticas:

- Faça commits pequenos e coerentes.
- Utilize mensagens descritivas.
- Evite incluir segredos.
- Revise alterações.
- Utilize branches quando apropriado.
- Resolva conflitos conscientemente.

## 8. Convenções de commits

Uma convenção comum é Conventional Commits.

Exemplos:

- feat: adiciona autenticação.
- fix: corrige validação.
- docs: atualiza documentação.
- refactor: reorganiza serviços.
- test: adiciona testes.
- chore: atualiza dependências.

A convenção deve ser consistente dentro do projeto.

## 9. Integração e entrega contínuas

CI/CD automatiza etapas do desenvolvimento e implantação.

### Continuous Integration

Integra alterações frequentemente e executa verificações automatizadas.

### Continuous Delivery

Mantém o software preparado para implantação.

### Continuous Deployment

Automatiza a publicação de alterações que atendem aos critérios definidos.

Pipelines podem incluir:

- Build.
- Testes.
- Lint.
- Análise estática.
- Verificação de dependências.
- Testes de segurança.
- Deploy.

## 10. Ambientes de desenvolvimento

Ambientes comuns:

- Development.
- Testing.
- Staging.
- Production.

Boas práticas:

- Separar configurações.
- Evitar dados reais em testes sem necessidade.
- Proteger credenciais.
- Utilizar configurações reproduzíveis.
- Documentar requisitos.
- Controlar permissões.

## 11. Documentação

A documentação facilita compreensão, manutenção e colaboração.

Documentos importantes:

- README.md.
- Documentação técnica.
- Guia de instalação.
- Guia de utilização.
- Referência de APIs.
- Diagramas.
- ADRs.
- CHANGELOG.

A documentação deve permanecer alinhada ao comportamento real do sistema.

## 12. Manutenibilidade

Software deve ser desenvolvido considerando mudanças futuras.

Boas práticas:

- Código legível.
- Baixo acoplamento.
- Alta coesão.
- Testes.
- Documentação.
- Modularização.
- Convenções consistentes.
- Controle de dependências.

Evite soluções que funcionam apenas enquanto o contexto original permanece inalterado.

## 13. Gestão de dependências

Dependências externas devem ser avaliadas antes de serem incorporadas.

Considere:

- Reputação.
- Manutenção.
- Licença.
- Compatibilidade.
- Segurança.
- Desempenho.
- Comunidade.
- Frequência de atualizações.

Remova dependências não utilizadas.

## 14. Qualidade de software

A qualidade deve considerar diferentes dimensões:

- Correção.
- Confiabilidade.
- Segurança.
- Eficiência.
- Manutenibilidade.
- Portabilidade.
- Usabilidade.
- Testabilidade.

Utilize critérios verificáveis sempre que possível.

## 15. Observabilidade

Sistemas em operação precisam fornecer informações sobre seu comportamento.

Três pilares:

### Logs

Registram eventos.

### Métricas

Apresentam indicadores quantitativos.

### Traces

Permitem acompanhar requisições entre componentes.

Ferramentas:

- Prometheus.
- Grafana.
- OpenTelemetry.
- Loki.
- Jaeger.

Evite registrar dados sensíveis desnecessariamente.

## 16. Gestão de riscos

Projetos podem apresentar riscos técnicos, operacionais e organizacionais.

Identifique:

- Probabilidade.
- Impacto.
- Dependências.
- Mitigações.
- Responsáveis.
- Riscos residuais.

Priorize problemas com potencial de comprometer os objetivos do projeto.

## 17. Diretrizes para o agente

Ao participar de um projeto:

1. Compreenda o objetivo.
2. Identifique requisitos.
3. Avalie o escopo.
4. Analise a estrutura existente.
5. Identifique tecnologias.
6. Planeje etapas.
7. Divida tarefas.
8. Considere segurança.
9. Recomende testes.
10. Documente decisões.
11. Preserve histórico.
12. Verifique resultados.

Não implemente funcionalidades antes de compreender seus requisitos essenciais.

Quando houver ambiguidades relevantes, faça perguntas antes de tomar decisões arquiteturais ou funcionais importantes.

## 18. Referências

- Agile Manifesto: https://agilemanifesto.org/
- Scrum Guide: https://scrumguides.org/
- Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/
- Atlassian Agile: https://www.atlassian.com/agile
- Google Engineering Practices: https://google.github.io/eng-practices/

