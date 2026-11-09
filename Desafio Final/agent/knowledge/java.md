# Java — Linguagem de Programação Java

## 1. Objetivo

Este documento apresenta fundamentos, características, boas práticas e recomendações de desenvolvimento utilizando Java.

O objetivo é orientar o agente na criação, análise, manutenção e auditoria de aplicações Java, considerando arquitetura, desempenho, segurança e qualidade.

## 2. Características da linguagem

Java é uma linguagem de programação de tipagem estática, orientada a objetos e amplamente utilizada em sistemas corporativos.

Características:

- Compilação para bytecode.
- Execução na Java Virtual Machine (JVM).
- Gerenciamento automático de memória.
- Orientação a objetos.
- Suporte a programação funcional.
- Multithreading.
- Ecossistema maduro.

Aplicações comuns:

- APIs.
- Sistemas corporativos.
- Aplicações backend.
- Sistemas distribuídos.
- Aplicações Android.
- Processamento de dados.

## 3. Estrutura básica

Exemplo:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Boas práticas:

- Utilize nomes descritivos.
- Organize classes por responsabilidade.
- Respeite convenções Java.
- Evite classes excessivamente grandes.
- Utilize encapsulamento.

## 4. Tipos de dados

### Tipos primitivos

- byte.
- short.
- int.
- long.
- float.
- double.
- char.
- boolean.

### Tipos de referência

- String.
- Arrays.
- Classes.
- Interfaces.
- Collections.
- Enums.

Utilize tipos adequados ao domínio da aplicação.

## 5. Orientação a objetos

Java utiliza amplamente orientação a objetos.

Conceitos fundamentais:

- Classes.
- Objetos.
- Encapsulamento.
- Herança.
- Polimorfismo.
- Abstração.
- Interfaces.

Exemplo:

```java
public class User {
    private final String name;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

Boas práticas:

- Prefira encapsulamento.
- Utilize interfaces quando houver necessidade de abstração.
- Evite herança excessiva.
- Prefira composição quando apropriado.
- Mantenha classes coesas.

## 6. Collections Framework

Java oferece estruturas para armazenamento e manipulação de coleções.

Principais interfaces:

- List.
- Set.
- Map.
- Queue.
- Deque.

Implementações comuns:

- ArrayList.
- LinkedList.
- HashSet.
- TreeSet.
- HashMap.
- TreeMap.
- ArrayDeque.

Escolha estruturas conforme os requisitos de acesso, ordenação e desempenho.

## 7. Generics

Generics permitem criar classes e métodos reutilizáveis com segurança de tipos.

Exemplo:

```java
public class Box<T> {
    private T value;

    public void setValue(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }
}
```

Evite utilizar tipos genéricos sem necessidade ou recorrer indiscriminadamente a Object.

## 8. Tratamento de exceções

Java oferece exceções verificadas e não verificadas.

Exemplos:

- IOException.
- SQLException.
- IllegalArgumentException.
- NullPointerException.
- RuntimeException.

Exemplo:

```java
try {
    performOperation();
} catch (IOException exception) {
    System.err.println("Operation failed.");
}
```

Boas práticas:

- Não ignore exceções.
- Evite capturar Exception indiscriminadamente.
- Utilize exceções específicas.
- Preserve a causa original.
- Não utilize exceções como fluxo normal.
- Evite revelar informações sensíveis.

## 9. Recursos modernos do Java

Versões importantes:

- Java 8.
- Java 11.
- Java 17.
- Java 21.
- Java 25.

Recursos relevantes:

- Lambda Expressions.
- Stream API.
- Records.
- Pattern Matching.
- Sealed Classes.
- Virtual Threads.
- Switch Expressions.

Utilize recursos compatíveis com a versão configurada no projeto.

### Stream API

Permite processar coleções de maneira declarativa.

Exemplo:

```java
List<String> activeUsers = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .toList();
```

Evite pipelines excessivamente complexos.

## 10. Gerenciamento de memória

Java utiliza gerenciamento automático de memória por meio do Garbage Collector.

Entretanto, ainda podem ocorrer:

- Memory Leaks.
- Retenção desnecessária de objetos.
- Consumo excessivo de memória.
- Pressão sobre o Garbage Collector.

Boas práticas:

- Evite referências desnecessárias.
- Libere recursos externos.
- Utilize try-with-resources.
- Monitore o consumo de memória.
- Avalie o comportamento do Garbage Collector.

## 11. Desenvolvimento backend

Frameworks comuns:

- Spring Boot.
- Quarkus.
- Micronaut.
- Jakarta EE.

Uma estrutura comum:

```text
src/
├── main/
│   ├── java/
│   │   └── com/example/
│   │       ├── controller/
│   │       ├── service/
│   │       ├── repository/
│   │       ├── model/
│   │       └── config/
│   └── resources/
└── test/
```

Separe responsabilidades conforme a arquitetura adotada.

## 12. Gerenciamento de dependências

Ferramentas comuns:

- Maven.
- Gradle.

Boas práticas:

- Versione dependências.
- Utilize versões estáveis.
- Avalie bibliotecas externas.
- Verifique vulnerabilidades.
- Evite dependências desnecessárias.
- Mantenha builds reproduzíveis.

## 13. Persistência de dados

Tecnologias comuns:

- JDBC.
- JPA.
- Hibernate.
- Spring Data JPA.

Boas práticas:

- Utilize consultas parametrizadas.
- Gerencie transações.
- Evite N+1 queries.
- Considere índices.
- Defina relacionamentos corretamente.
- Avalie o impacto de operações em massa.

Nunca concatene entradas não confiáveis diretamente em consultas SQL.

## 14. Segurança em Java

Riscos comuns:

- SQL Injection.
- Insecure Deserialization.
- Broken Access Control.
- Path Traversal.
- SSRF.
- Exposição de informações sensíveis.
- Dependências vulneráveis.
- Configurações inseguras.

Boas práticas:

- Validar entradas.
- Aplicar menor privilégio.
- Utilizar consultas parametrizadas.
- Proteger credenciais.
- Configurar autenticação e autorização.
- Atualizar bibliotecas.
- Utilizar HTTPS.
- Evitar desserialização insegura.
- Configurar corretamente o ambiente de produção.

## 15. Concorrência

Java oferece diversos mecanismos para programação concorrente.

Exemplos:

- Thread.
- ExecutorService.
- CompletableFuture.
- synchronized.
- Locks.
- ConcurrentHashMap.
- Virtual Threads.

Cuidados:

- Race Conditions.
- Deadlocks.
- Starvation.
- Problemas de sincronização.
- Compartilhamento inseguro de estado.

Prefira mecanismos de concorrência bem definidos e adequados ao problema.

## 16. Testes

Ferramentas:

- JUnit.
- Mockito.
- Testcontainers.
- AssertJ.
- JaCoCo.

Tipos de testes:

- Unitários.
- Integração.
- Contrato.
- End-to-end.

Teste regras de negócio, persistência, autenticação, autorização e condições de falha.

## 17. Diretrizes para o agente

Ao trabalhar com Java:

1. Identifique a versão do JDK.
2. Verifique o sistema de build.
3. Analise a arquitetura.
4. Respeite os padrões existentes.
5. Avalie o uso de orientação a objetos.
6. Verifique gerenciamento de recursos.
7. Analise dependências.
8. Avalie segurança.
9. Considere concorrência.
10. Recomende testes apropriados.

Não introduza frameworks ou bibliotecas sem justificativa.

## 18. Documentação oficial

- Java: https://docs.oracle.com/en/java/
- Java Tutorials: https://dev.java/learn/
- Spring Boot: https://docs.spring.io/spring-boot/index.html
- Maven: https://maven.apache.org/guides/
- Gradle: https://docs.gradle.org/
- JUnit: https://junit.org/junit5/docs/current/user-guide/
- OWASP Java Security: https://cheatsheetseries.owasp.org/

