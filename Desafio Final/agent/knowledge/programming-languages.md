# Programming Languages — Linguagens de Programação

## 1. Objetivo

Este documento apresenta conceitos gerais sobre linguagens de programação, paradigmas, tipagem, compilação, interpretação e critérios para escolha de tecnologias.

O objetivo é orientar o agente na escolha e utilização de linguagens adequadas para cada projeto, considerando requisitos técnicos, desempenho, segurança, manutenção e escalabilidade.

## 2. Conceitos fundamentais

Uma linguagem de programação permite expressar instruções que serão executadas por um computador.

Cada linguagem possui características próprias, incluindo:

- Sintaxe.
- Semântica.
- Sistema de tipos.
- Paradigmas.
- Modelo de execução.
- Gerenciamento de memória.
- Bibliotecas e ecossistema.

A escolha de uma linguagem deve considerar o problema que precisa ser resolvido, e não apenas sua popularidade.

## 3. Paradigmas de programação

### 3.1. Programação procedural

Organiza o código em procedimentos e funções executados em sequência.

Características:

- Fluxo de execução explícito.
- Funções e procedimentos.
- Estruturas de controle.
- Separação de tarefas.

Exemplos de linguagens:

- C.
- Pascal.
- Python.

### 3.2. Programação orientada a objetos

Organiza o sistema em objetos que representam entidades e comportamentos.

Princípios:

- Encapsulamento.
- Abstração.
- Herança.
- Polimorfismo.

Exemplos:

- Java.
- C++.
- C#.
- Python.
- TypeScript.

### 3.3. Programação funcional

Prioriza funções, imutabilidade e composição de operações.

Características:

- Funções puras.
- Imutabilidade.
- Funções de alta ordem.
- Recursividade.
- Composição.

Exemplos:

- Haskell.
- Elixir.
- Clojure.
- JavaScript.
- Python.

### 3.4. Programação declarativa

Descreve o resultado desejado sem especificar necessariamente todos os passos para alcançá-lo.

Exemplos:

- SQL.
- HTML.
- CSS.
- Prolog.

## 4. Sistemas de tipos

### 4.1. Tipagem estática

Os tipos são verificados principalmente durante a compilação ou análise estática.

Exemplos:

- C.
- C++.
- Java.
- TypeScript.

Vantagens:

- Identificação antecipada de incompatibilidades.
- Maior previsibilidade.
- Melhor suporte de ferramentas.
- Facilidade de manutenção em sistemas grandes.

### 4.2. Tipagem dinâmica

Os tipos são associados aos valores durante a execução.

Exemplos:

- Python.
- JavaScript.
- Ruby.
- PHP.

Vantagens:

- Flexibilidade.
- Rapidez de desenvolvimento.
- Menos declarações explícitas de tipos.

Cuidados:

- Verificação de tipos em tempo de execução.
- Possibilidade de erros não identificados antecipadamente.
- Necessidade de testes adequados.

### 4.3. Tipagem forte e fraca

Esses conceitos descrevem como uma linguagem permite ou restringe operações entre tipos diferentes.

Não existe uma classificação universal única para todas as linguagens.

O agente deve analisar o comportamento concreto da linguagem e evitar simplificações excessivas.

## 5. Compilação e interpretação

### 5.1. Linguagens compiladas

O código é transformado em uma representação executável antes ou durante a execução.

Exemplos:

- C.
- C++.
- Rust.
- Go.

### 5.2. Linguagens interpretadas

O código é executado por meio de um interpretador ou ambiente de execução.

Exemplos comuns:

- Python.
- Ruby.
- JavaScript.

### 5.3. Modelos híbridos

Algumas linguagens utilizam compilação intermediária, máquinas virtuais ou compilação JIT.

Exemplos:

- Java.
- C#.
- JavaScript em motores modernos.

A distinção entre compiladas e interpretadas não deve ser tratada como absoluta.

## 6. Gerenciamento de memória

### 6.1. Gerenciamento manual

O programador controla explicitamente a alocação e liberação de memória.

Exemplos:

- C.
- C++.

Cuidados:

- Memory leaks.
- Use-after-free.
- Double free.
- Buffer overflow.
- Ponteiros inválidos.

### 6.2. Gerenciamento automático

O ambiente de execução administra grande parte da memória.

Exemplos:

- Java.
- Python.
- JavaScript.
- C#.

O gerenciamento automático reduz determinadas classes de erros, mas não elimina problemas de memória.

### 6.3. Ownership e borrowing

Algumas linguagens utilizam mecanismos de propriedade e empréstimo para controlar acesso e duração dos dados.

Exemplo:

- Rust.

Esses mecanismos ajudam a prevenir determinadas condições inseguras de memória.

## 7. Principais linguagens e aplicações

### C

Indicada para:

- Sistemas operacionais.
- Sistemas embarcados.
- Drivers.
- Programação de baixo nível.

Características:

- Controle direto de memória.
- Alto desempenho.
- Tipagem estática.
- Grande responsabilidade do programador sobre segurança de memória.

### C++

Indicada para:

- Aplicações de alto desempenho.
- Engines.
- Sistemas complexos.
- Software embarcado.
- Aplicações nativas.

Características:

- Orientação a objetos.
- Programação genérica.
- Templates.
- Gerenciamento de memória.
- Biblioteca padrão extensa.

### Java

Indicada para:

- Aplicações corporativas.
- APIs.
- Sistemas distribuídos.
- Aplicações backend.

Características:

- Tipagem estática.
- Orientação a objetos.
- Máquina virtual Java.
- Ecossistema maduro.

### Python

Indicada para:

- Automação.
- Inteligência artificial.
- Ciência de dados.
- APIs.
- Cibersegurança.
- Scripts.

Características:

- Sintaxe simples.
- Tipagem dinâmica.
- Ecossistema amplo.
- Grande quantidade de bibliotecas.

### JavaScript

Indicada para:

- Desenvolvimento web.
- Aplicações frontend.
- Backend com Node.js.
- Aplicações em tempo real.

Características:

- Execução em navegadores.
- Modelo assíncrono.
- Tipagem dinâmica.

### TypeScript

Indicada para:

- Aplicações JavaScript maiores.
- Projetos frontend.
- Backend.
- Sistemas que exigem maior previsibilidade de tipos.

Características:

- Tipagem estática.
- Compatibilidade com o ecossistema JavaScript.
- Ferramentas de desenvolvimento avançadas.

### Go

Indicada para:

- Microsserviços.
- Infraestrutura.
- APIs.
- Ferramentas de rede.
- Sistemas concorrentes.

Características:

- Compilação nativa.
- Concorrência com goroutines.
- Sintaxe relativamente simples.
- Gerenciamento automático de memória.

### Rust

Indicada para:

- Sistemas de alto desempenho.
- Infraestrutura.
- Ferramentas de segurança.
- Software de baixo nível.

Características:

- Ownership.
- Borrowing.
- Segurança de memória.
- Concorrência segura.

## 8. Critérios para escolher uma linguagem

Considere:

1. Objetivo do projeto.
2. Desempenho necessário.
3. Segurança.
4. Complexidade.
5. Facilidade de manutenção.
6. Ecossistema.
7. Disponibilidade de bibliotecas.
8. Experiência da equipe.
9. Compatibilidade com infraestrutura.
10. Custos de desenvolvimento e operação.

Não recomende uma linguagem apenas por preferência pessoal.

## 9. Interoperabilidade

Projetos podem utilizar diferentes linguagens em conjunto.

Mecanismos comuns:

- APIs REST.
- GraphQL.
- gRPC.
- Filas de mensagens.
- Arquivos compartilhados.
- Bibliotecas nativas.
- WebSockets.

A interoperabilidade deve considerar contratos, formatos de dados, autenticação, erros e compatibilidade.

## 10. Boas práticas gerais

Independentemente da linguagem:

- Utilize nomes descritivos.
- Escreva funções coesas.
- Evite duplicação.
- Separe responsabilidades.
- Valide entradas.
- Trate erros.
- Escreva testes.
- Documente decisões importantes.
- Gerencie dependências.
- Utilize controle de versão.
- Considere segurança desde o início.
- Evite complexidade desnecessária.

## 11. Segurança no desenvolvimento

A linguagem escolhida influencia os riscos e mecanismos de proteção disponíveis.

Considere:

- Segurança de memória.
- Validação de entradas.
- Tratamento de erros.
- Gerenciamento de dependências.
- Controle de acesso.
- Proteção de credenciais.
- Atualizações.
- Análise estática.
- Testes de segurança.

Consulte o documento `secure-development.md` para orientações complementares.

## 12. Diretrizes para o agente

Ao iniciar um projeto:

1. Identifique o problema que precisa ser resolvido.
2. Identifique as restrições técnicas.
3. Avalie linguagens adequadas.
4. Compare vantagens e desvantagens.
5. Considere o conhecimento da equipe.
6. Avalie segurança e manutenção.
7. Recomende uma solução justificada.

Ao analisar um projeto existente:

1. Identifique as linguagens utilizadas.
2. Verifique versões e dependências.
3. Respeite os padrões estabelecidos.
4. Identifique oportunidades de melhoria.
5. Evite migrações desnecessárias.
6. Considere compatibilidade.

Não recomende reescrever um sistema em outra linguagem sem demonstrar benefícios concretos.

## 13. Documentação oficial

- C: https://en.cppreference.com/w/c
- C++: https://en.cppreference.com/w/
- Java: https://docs.oracle.com/en/java/
- Python: https://docs.python.org/3/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- TypeScript: https://www.typescriptlang.org/docs/
- Go: https://go.dev/doc/
- Rust: https://doc.rust-lang.org/book/


Não misture convenções de linguagens diferentes.

Quando não houver conhecimento específico documentado, consulte a documentação oficial da linguagem.

