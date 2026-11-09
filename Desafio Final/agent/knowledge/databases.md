# Databases — Bancos de Dados

## 1. Objetivo

Este documento apresenta fundamentos de bancos de dados, modelagem, armazenamento, consultas, integridade e segurança.

O objetivo é orientar a escolha, implementação e manutenção de soluções de persistência de dados.

## 2. Conceitos fundamentais

Um banco de dados é uma coleção organizada de informações que podem ser armazenadas, consultadas e modificadas.

Um SGBD (Sistema Gerenciador de Banco de Dados) administra o armazenamento e acesso aos dados.

Exemplos:

- PostgreSQL.
- MySQL.
- MariaDB.
- SQLite.
- Microsoft SQL Server.
- Oracle Database.
- MongoDB.
- Redis.

## 3. Bancos relacionais

Bancos relacionais organizam informações em tabelas relacionadas.

Conceitos:

- Tabelas.
- Registros.
- Colunas.
- Chaves primárias.
- Chaves estrangeiras.
- Restrições.
- Índices.

### Chave primária

Identifica unicamente um registro.

### Chave estrangeira

Estabelece relacionamento entre tabelas.

### Constraints

Restrições que garantem regras de integridade.

Exemplos:

- NOT NULL.
- UNIQUE.
- CHECK.
- PRIMARY KEY.
- FOREIGN KEY.

## 4. SQL

SQL é utilizado para definir, consultar e manipular dados relacionais.

Categorias:

### DDL

Definição da estrutura.

Exemplos:

- CREATE.
- ALTER.
- DROP.

### DML

Manipulação de dados.

Exemplos:

- INSERT.
- UPDATE.
- DELETE.

### DQL

Consulta de dados.

Principal comando:

- SELECT.

### DCL

Controle de permissões.

Exemplos:

- GRANT.
- REVOKE.

### TCL

Controle de transações.

Exemplos:

- COMMIT.
- ROLLBACK.
- SAVEPOINT.

## 5. Consultas SQL

Exemplo:

```sql
SELECT id, name, email
FROM users
WHERE active = TRUE
ORDER BY name;
```

Boas práticas:

- Selecionar somente as colunas necessárias.
- Utilizar filtros apropriados.
- Evitar consultas excessivamente complexas.
- Utilizar parâmetros.
- Avaliar planos de execução.
- Considerar índices.

## 6. Modelagem de dados

A modelagem representa a estrutura das informações e seus relacionamentos.

Etapas:

1. Identificar entidades.
2. Identificar atributos.
3. Definir relacionamentos.
4. Determinar cardinalidade.
5. Definir chaves.
6. Estabelecer restrições.

Relacionamentos comuns:

- Um para um.
- Um para muitos.
- Muitos para muitos.

Relacionamentos muitos para muitos normalmente utilizam uma tabela associativa.

## 7. Normalização

A normalização organiza dados para reduzir redundâncias e anomalias.

Formas normais:

- Primeira Forma Normal (1FN).
- Segunda Forma Normal (2FN).
- Terceira Forma Normal (3FN).
- BCNF.

A normalização deve ser considerada conforme as necessidades do sistema.

Desnormalização pode ser apropriada para determinados cenários de desempenho, desde que exista justificativa.

## 8. Índices

Índices aceleram determinadas consultas.

Tipos e mecanismos dependem do SGBD.

Exemplos:

- B-tree.
- Hash.
- Índices compostos.
- Índices únicos.
- Índices parciais.

Cuidados:

- Índices consomem armazenamento.
- Podem aumentar o custo de escrita.
- Devem corresponder aos padrões reais de consulta.
- Devem ser avaliados por planos de execução.

## 9. Transações e propriedades ACID

ACID representa:

### Atomicidade

A transação é executada integralmente ou não produz seus efeitos confirmados.

### Consistência

A transação preserva as regras de integridade do banco.

### Isolamento

Transações concorrentes possuem comportamento controlado conforme o nível de isolamento.

### Durabilidade

Alterações confirmadas permanecem registradas conforme as garantias do SGBD.

## 10. Isolamento e concorrência

Níveis comuns:

- Read Uncommitted.
- Read Committed.
- Repeatable Read.
- Serializable.

Os comportamentos específicos variam entre SGBDs.

Problemas possíveis:

- Dirty Reads.
- Non-repeatable Reads.
- Phantom Reads.
- Lost Updates.

Considere concorrência e consistência ao projetar operações.

## 11. Bancos NoSQL

Bancos NoSQL utilizam modelos de armazenamento diferentes do modelo relacional tradicional.

Categorias:

### Documentos

Exemplo: MongoDB.

Armazenam documentos estruturados.

### Chave-valor

Exemplo: Redis.

Armazenam valores associados a chaves.

### Colunares

Exemplo: Cassandra.

Organizam informações em estruturas orientadas a colunas.

### Grafos

Exemplo: Neo4j.

Representam entidades e relacionamentos como nós e arestas.

A escolha deve considerar os padrões de acesso e os requisitos de consistência.

## 12. Segurança de bancos de dados

Boas práticas:

- Utilizar menor privilégio.
- Separar contas administrativas e de aplicação.
- Utilizar consultas parametrizadas.
- Proteger credenciais.
- Restringir exposição de rede.
- Utilizar TLS quando aplicável.
- Aplicar atualizações.
- Monitorar acessos.
- Realizar backups.
- Proteger dados sensíveis.

Nunca armazenar senhas de usuários em texto puro.

Utilize algoritmos específicos de hashing de senhas, como Argon2id, conforme a arquitetura da aplicação.

## 13. Backup e recuperação

Considere:

- Backups completos.
- Backups incrementais.
- Backups diferenciais.
- Replicação.
- Recuperação pontual.
- Testes de restauração.

Backup não é confiável apenas porque foi criado.

É necessário verificar sua integridade e testar a recuperação.

Considere RPO e RTO:

- RPO: perda máxima de dados aceitável medida em tempo.
- RTO: tempo máximo desejado para recuperação.

## 14. Migrações

Migrações controlam alterações na estrutura do banco.

Boas práticas:

- Versionar migrações.
- Testar alterações.
- Considerar compatibilidade.
- Planejar rollback.
- Avaliar impactos.
- Evitar alterações destrutivas sem planejamento.

## 15. Ferramentas

- DBeaver.
- pgAdmin.
- MySQL Workbench.
- SQLite.
- MongoDB Compass.
- Flyway.
- Liquibase.
- Alembic.

## 16. Diretrizes para o agente

Ao trabalhar com bancos:

1. Identifique o SGBD.
2. Verifique a versão.
3. Compreenda o modelo de dados.
4. Avalie relacionamentos.
5. Considere integridade.
6. Analise consultas.
7. Utilize parâmetros.
8. Avalie permissões.
9. Considere backups.
10. Preserve dados existentes.

Nunca execute operações destrutivas em bancos reais sem autorização explícita e confirmação do escopo.

Consulte a documentação oficial do SGBD utilizado.

