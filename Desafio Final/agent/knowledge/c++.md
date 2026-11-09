# C++ — Linguagem de Programação C++

## 1. Objetivo

Este documento apresenta fundamentos, características, boas práticas e recomendações de desenvolvimento utilizando C++.

O objetivo é orientar o agente na criação, análise, manutenção e auditoria de aplicações C++, considerando desempenho, arquitetura, gerenciamento de memória e segurança.

## 2. Características da linguagem

C++ é uma linguagem compilada, de tipagem estática e multiparadigma.

Suporta:

- Programação procedural.
- Orientação a objetos.
- Programação genérica.
- Programação funcional.
- Metaprogramação.
- Gerenciamento de memória.
- Programação de sistemas.

Aplicações comuns:

- Engines de jogos.
- Sistemas operacionais.
- Aplicações desktop.
- Sistemas embarcados.
- Simulações.
- Computação científica.
- Aplicações de alto desempenho.

## 3. Estrutura básica

Exemplo:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

Boas práticas:

- Utilize recursos modernos da linguagem.
- Prefira a biblioteca padrão.
- Evite complexidade desnecessária.
- Organize o código em módulos.
- Utilize namespaces adequadamente.

## 4. Tipos de dados

Tipos fundamentais:

- bool.
- char.
- int.
- float.
- double.
- void.

Tipos compostos:

- Arrays.
- Pointers.
- References.
- Structs.
- Classes.
- Enums.
- Templates.

Tipos modernos da biblioteca padrão:

- std::string.
- std::vector.
- std::array.
- std::map.
- std::unordered_map.
- std::optional.
- std::variant.

Prefira estruturas da biblioteca padrão quando forem adequadas.

## 5. Orientação a objetos

C++ suporta classes, herança, encapsulamento e polimorfismo.

Exemplo:

```cpp
#include <iostream>
#include <string>

class User {
private:
    std::string name;

public:
    explicit User(const std::string& userName)
        : name(userName) {}

    void display() const {
        std::cout << name << std::endl;
    }
};
```

Boas práticas:

- Encapsule estado interno.
- Utilize construtores adequados.
- Prefira interfaces claras.
- Evite hierarquias profundas.
- Considere composição.
- Utilize destrutores quando houver gerenciamento manual de recursos.

## 6. Gerenciamento de memória

C++ permite gerenciamento manual, mas oferece recursos modernos para gerenciamento automático de recursos.

Prefira:

- std::unique_ptr.
- std::shared_ptr.
- std::weak_ptr.
- RAII.

### RAII

Resource Acquisition Is Initialization.

O gerenciamento de recursos deve estar associado ao ciclo de vida dos objetos.

Exemplo:

```cpp
#include <memory>

auto number = std::make_unique<int>(42);
```

Boas práticas:

- Prefira smart pointers a new e delete explícitos.
- Evite vazamentos de memória.
- Evite ponteiros pendentes.
- Evite ownership ambíguo.
- Não utilize recursos após sua liberação.
- Considere referências e valores conforme a necessidade.

## 7. Standard Template Library

A STL fornece estruturas e algoritmos reutilizáveis.

Contêineres comuns:

- std::vector.
- std::array.
- std::list.
- std::deque.
- std::map.
- std::unordered_map.
- std::set.

Algoritmos:

- std::sort.
- std::find.
- std::transform.
- std::count_if.
- std::accumulate.

Exemplo:

```cpp
#include <algorithm>
#include <vector>

std::vector<int> numbers = {5, 2, 8, 1};

std::sort(numbers.begin(), numbers.end());
```

Prefira algoritmos da biblioteca padrão a implementações próprias quando forem adequados.

## 8. Programação genérica

Templates permitem desenvolver componentes reutilizáveis.

Exemplo:

```cpp
template <typename T>
T maximum(T a, T b) {
    return a > b ? a : b;
}
```

Recursos modernos incluem:

- Templates.
- Concepts.
- Type traits.
- Variadic templates.
- Constexpr.

Utilize abstrações genéricas com cuidado para não aumentar desnecessariamente a complexidade.

## 9. Modern C++

Versões importantes:

- C++11.
- C++14.
- C++17.
- C++20.
- C++23.

Recursos relevantes:

- Auto.
- Lambda expressions.
- Smart pointers.
- Move semantics.
- Range-based for.
- Structured bindings.
- Concepts.
- Ranges.
- std::optional.
- std::expected.

Utilize recursos compatíveis com o padrão e o compilador definidos pelo projeto.

## 10. Tratamento de erros

C++ oferece diferentes mecanismos de tratamento de erros.

Exemplos:

- Exceções.
- Códigos de retorno.
- std::optional.
- std::expected.

Boas práticas:

- Defina estratégias consistentes.
- Evite ignorar exceções.
- Utilize exceções para situações excepcionais.
- Evite retornar estados ambíguos.
- Preserve informações úteis.
- Não exponha informações sensíveis.

## 11. Concorrência

C++ oferece recursos para programação concorrente.

Principais mecanismos:

- std::thread.
- std::mutex.
- std::lock_guard.
- std::unique_lock.
- std::atomic.
- std::future.
- std::async.

Cuidados:

- Data races.
- Deadlocks.
- Race conditions.
- False sharing.
- Problemas de sincronização.

Prefira abstrações seguras e simples.

Utilize sanitizers e testes para identificar problemas concorrentes.

## 12. Organização de projetos

Estrutura possível:

```text
project/
├── include/
├── src/
├── tests/
├── CMakeLists.txt
└── README.md
```

Ferramentas:

- CMake.
- Ninja.
- Make.
- Conan.
- vcpkg.

Boas práticas:

- Separe interfaces e implementações.
- Organize dependências.
- Utilize builds reproduzíveis.
- Versione configurações importantes.
- Documente requisitos de compilação.

## 13. Segurança em C++

Riscos comuns:

- Buffer Overflow.
- Use-After-Free.
- Double Free.
- Integer Overflow.
- Dangling Pointers.
- Data Races.
- Undefined Behavior.
- Format String Vulnerability.
- Insecure Deserialization.

Boas práticas:

- Utilize RAII.
- Prefira containers seguros.
- Evite manipulação manual de memória sem necessidade.
- Valide entradas.
- Verifique limites.
- Utilize referências e ponteiros corretamente.
- Evite casts perigosos.
- Atualize dependências.
- Utilize ferramentas de análise.

## 14. Ferramentas

- GCC.
- Clang.
- MSVC.
- CMake.
- GDB.
- LLDB.
- Valgrind.
- AddressSanitizer.
- UndefinedBehaviorSanitizer.
- ThreadSanitizer.
- Cppcheck.
- Clang-Tidy.

## 15. Testes

Frameworks:

- GoogleTest.
- Catch2.
- doctest.

Tipos:

- Unitários.
- Integração.
- Desempenho.
- Concorrência.
- Segurança.

Teste casos extremos, entradas inválidas e comportamento sob falhas.

## 16. Diretrizes para o agente

Ao desenvolver ou analisar C++:

1. Identifique o padrão C++ utilizado.
2. Verifique o compilador.
3. Analise o gerenciamento de recursos.
4. Avalie o uso de ponteiros.
5. Considere RAII.
6. Verifique possíveis comportamentos indefinidos.
7. Avalie concorrência.
8. Analise dependências.
9. Recomende ferramentas de análise.
10. Preserve compatibilidade.

Prefira soluções modernas e seguras, mas respeite as restrições do projeto existente.

## 17. Documentação oficial

- C++ Reference: https://en.cppreference.com/w/
- ISO C++: https://isocpp.org/
- GCC: https://gcc.gnu.org/
- Clang: https://clang.llvm.org/docs/
- CMake: https://cmake.org/documentation/
- C++ Core Guidelines: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

