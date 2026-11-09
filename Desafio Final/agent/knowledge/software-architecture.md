# Software Architecture — Arquitetura de Software

## 1. Objetivo

Este documento apresenta conceitos, padrões e princípios de arquitetura de software.

O objetivo é orientar o agente no planejamento, estruturação, evolução e avaliação arquitetural de aplicações, considerando requisitos funcionais e não funcionais.

## 2. Conceitos fundamentais

Arquitetura de software define a organização estrutural de um sistema, seus componentes, responsabilidades, dependências e formas de comunicação.

Uma arquitetura deve considerar:

- Requisitos funcionais.
- Requisitos não funcionais.
- Escalabilidade.
- Segurança.
- Desempenho.
- Manutenção.
- Disponibilidade.
- Custos.
- Evolução.

Não existe uma arquitetura universalmente melhor.

A escolha deve considerar o contexto e as necessidades do projeto.

## 3. Requisitos funcionais e não funcionais

### Requisitos funcionais

Definem o que o sistema deve fazer.

Exemplos:

- Cadastrar usuários.
- Realizar autenticação.
- Processar pagamentos.
- Gerenciar produtos.
- Emitir relatórios.

### Requisitos não funcionais

Definem características e restrições do sistema.

Exemplos:

- Desempenho.
- Segurança.
- Disponibilidade.
- Escalabilidade.
- Manutenibilidade.
- Usabilidade.
- Portabilidade.

Ambos devem influenciar as decisões arquiteturais.

## 4. Acoplamento e coesão

### Acoplamento

Representa o grau de dependência entre componentes.

Prefira baixo acoplamento.

Componentes muito dependentes dificultam manutenção, testes e evolução.

### Coesão

Representa o quanto os elementos de um componente estão relacionados à mesma responsabilidade.

Prefira alta coesão.

Cada módulo deve possuir uma finalidade bem definida.

## 5. Arquitetura em camadas

Organiza a aplicação em camadas com responsabilidades distintas.

Exemplo:

- Presentation.
- Application.
- Domain.
- Infrastructure.

Características:

- Separação de responsabilidades.
- Organização lógica.
- Facilidade de compreensão.
- Controle de dependências.

Evite criar camadas desnecessárias em aplicações simples.

## 6. Clean Architecture

Clean Architecture organiza o sistema em torno das regras de negócio.

Princípio central:

As dependências devem apontar para dentro, em direção às regras de negócio.

Camadas comuns:

- Entities.
- Use Cases.
- Interface Adapters.
- Frameworks and Drivers.

Benefícios:

- Independência de frameworks.
- Facilidade de testes.
- Separação de responsabilidades.
- Melhor isolamento das regras de negócio.

Não aplique o padrão mecanicamente quando a complexidade não justificar.

## 7. Arquitetura Hexagonal

Também conhecida como Ports and Adapters.

Separa a lógica central das tecnologias externas.

Componentes:

- Domínio.
- Portas.
- Adaptadores.

Exemplos de adaptadores:

- Banco de dados.
- API HTTP.
- Filas.
- Serviços externos.

A arquitetura facilita substituir implementações externas sem modificar diretamente as regras centrais.

## 8. Monólitos

Um monólito é uma aplicação organizada e implantada como uma unidade principal.

Vantagens:

- Menor complexidade operacional.
- Desenvolvimento inicial simples.
- Comunicação interna direta.
- Facilidade de implantação em determinados cenários.

Desvantagens possíveis:

- Crescimento de acoplamento.
- Dificuldade de escalar partes isoladamente.
- Maior impacto de alterações mal planejadas.

Um monólito modular pode ser uma excelente escolha para muitos projetos.

## 9. Microsserviços

Microsserviços dividem um sistema em serviços menores e relativamente independentes.

Características:

- Responsabilidades delimitadas.
- Comunicação por contratos.
- Implantação independente.
- Possibilidade de escalabilidade individual.

Desafios:

- Complexidade distribuída.
- Observabilidade.
- Consistência de dados.
- Comunicação entre serviços.
- Segurança.
- Gerenciamento de falhas.
- Operação e infraestrutura.

Não recomende microsserviços apenas por serem uma tendência.

Avalie se os benefícios compensam os custos operacionais.

## 10. Event-Driven Architecture

Arquitetura orientada a eventos utiliza eventos para comunicar mudanças e estimular processamento.

Conceitos:

- Producers.
- Consumers.
- Events.
- Brokers.
- Event Handlers.

Tecnologias:

- RabbitMQ.
- Apache Kafka.
- NATS.
- Redis Streams.

Benefícios:

- Desacoplamento.
- Processamento assíncrono.
- Escalabilidade.
- Integração entre serviços.

Cuidados:

- Duplicação de mensagens.
- Idempotência.
- Ordenação.
- Consistência eventual.
- Reprocessamento.
- Observabilidade.

## 11. CQRS

Command Query Responsibility Segregation separa operações de escrita e leitura.

Commands modificam o estado.

Queries consultam informações.

Pode ser útil quando existem necessidades diferentes de escalabilidade ou organização entre leitura e escrita.

Não é necessário para todos os sistemas.

## 12. Design Patterns

Padrões de projeto representam soluções recorrentes para problemas de estrutura e organização.

### Criacionais

- Factory.
- Abstract Factory.
- Builder.
- Singleton.
- Prototype.

### Estruturais

- Adapter.
- Decorator.
- Facade.
- Composite.
- Proxy.

### Comportamentais

- Strategy.
- Observer.
- Command.
- State.
- Iterator.
- Template Method.

Utilize padrões quando resolverem problemas reais.

Evite introduzir abstrações apenas para utilizar um padrão conhecido.

## 13. Domain-Driven Design

DDD é uma abordagem que prioriza a compreensão e modelagem do domínio do negócio.

Conceitos:

- Domain.
- Entity.
- Value Object.
- Aggregate.
- Repository.
- Domain Service.
- Bounded Context.
- Ubiquitous Language.

É especialmente útil em domínios complexos.

## 14. Escalabilidade

### Escalabilidade vertical

Aumenta os recursos de uma máquina.

Exemplos:

- CPU.
- RAM.
- Armazenamento.

### Escalabilidade horizontal

Adiciona novas instâncias de processamento.

Exemplos:

- Múltiplos servidores.
- Containers.
- Réplicas.
- Balanceadores de carga.

A escolha depende da arquitetura, infraestrutura e requisitos.

## 15. Disponibilidade e resiliência

Considere:

- Redundância.
- Health checks.
- Load balancing.
- Replicação.
- Backups.
- Circuit breakers.
- Timeouts.
- Retries controlados.
- Disaster recovery.

Evite retries ilimitados e estratégias que possam amplificar falhas.

## 16. Segurança arquitetural

A arquitetura deve considerar:

- Fronteiras de confiança.
- Segmentação.
- Autenticação.
- Autorização.
- Criptografia.
- Gerenciamento de segredos.
- Auditoria.
- Isolamento.
- Menor privilégio.

A segurança deve ser considerada entre componentes e nas comunicações externas.

## 17. Documentação arquitetural

Ferramentas e métodos:

- Diagramas C4.
- UML.
- ADR.
- Mermaid.
- PlantUML.

Documente:

- Contexto.
- Containers.
- Componentes.
- Fluxos de dados.
- Integrações.
- Decisões arquiteturais.
- Restrições.

### ADR

Architecture Decision Record registra decisões importantes.

Uma ADR pode conter:

- Contexto.
- Problema.
- Decisão.
- Alternativas.
- Consequências.

## 18. Diretrizes para o agente

Ao planejar ou revisar uma arquitetura:

1. Compreenda o problema.
2. Identifique requisitos.
3. Avalie restrições.
4. Identifique componentes.
5. Analise dependências.
6. Considere segurança.
7. Avalie escalabilidade.
8. Considere custos operacionais.
9. Compare alternativas.
10. Justifique decisões.
11. Documente consequências.
12. Evite complexidade prematura.

Sempre considere o tamanho e a maturidade do projeto antes de recomendar arquiteturas complexas.

## 19. Referências

- Martin Fowler: https://martinfowler.com/
- C4 Model: https://c4model.com/
- Microsoft Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/
- AWS Architecture Center: https://aws.amazon.com/architecture/
- Google Cloud Architecture: https://cloud.google.com/architecture
- Clean Architecture — Robert C. Martin.
- Domain-Driven Design — Eric Evans.

