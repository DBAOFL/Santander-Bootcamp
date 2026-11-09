# C — Linguagem de Programação C

## 1. Objetivo

Este documento apresenta fundamentos, características, boas práticas e recomendações de desenvolvimento utilizando a linguagem C.

O objetivo é orientar o agente na criação, análise, manutenção e auditoria de programas em C, com atenção especial ao gerenciamento de memória, desempenho e segurança.

## 2. Características da linguagem

C é uma linguagem de programação compilada, procedural e de tipagem estática.

É amplamente utilizada em:

- Sistemas operacionais.
- Drivers.
- Sistemas embarcados.
- Firmware.
- Bibliotecas.
- Aplicações de alto desempenho.
- Ferramentas de infraestrutura.

Principais características:

- Controle manual de memória.
- Ponteiros.
- Aritmética de baixo nível.
- Tipagem estática.
- Compilação para código nativo.
- Biblioteca padrão.
- Portabilidade entre plataformas.

## 3. Estrutura básica

Exemplo:

```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

Elementos:

- Diretivas de pré-processamento.
- Função principal.
- Declarações.
- Instruções.
- Retorno.

## 4. Tipos de dados

Tipos fundamentais:

- char.
- int.
- float.
- double.
- void.

Modificadores:

- signed.
- unsigned.
- short.
- long.

Tipos adicionais:

- Arrays.
- Ponteiros.
- Structs.
- Unions.
- Enums.

Utilize tipos apropriados para evitar problemas de representação e conversão.

Para tamanhos específicos, considere os tipos definidos em `<stdint.h>`.

Exemplos:

- int8_t.
- int16_t.
- int32_t.
- int64_t.
- uint32_t.
- size_t.

## 5. Funções

Funções permitem organizar o programa em unidades de responsabilidade.

Exemplo:

```c
#include <stdio.h>

int calculate_sum(int a, int b) {
    return a + b;
}

int main(void) {
    int result = calculate_sum(10, 5);

    printf("Result: %d\n", result);

    return 0;
}
```

Boas práticas:

- Utilize nomes descritivos.
- Evite funções excessivamente longas.
- Defina contratos claros.
- Valide parâmetros.
- Evite efeitos colaterais inesperados.

## 6. Ponteiros

Ponteiros armazenam endereços de memória.

São fundamentais para manipulação de memória e estruturas de dados.

Exemplo:

```c
int value = 10;
int *pointer = &value;

printf("%d\n", *pointer);
```

Cuidados:

- Não utilize ponteiros não inicializados.
- Evite dereferenciar NULL.
- Não utilize ponteiros após a liberação da memória.
- Respeite os limites dos objetos.
- Evite aritmética de ponteiros inválida.

## 7. Gerenciamento de memória

A linguagem C permite gerenciamento manual de memória.

Funções comuns:

- malloc().
- calloc().
- realloc().
- free().

Exemplo:

```c
#include <stdlib.h>

int *numbers = malloc(10 * sizeof(int));

if (numbers == NULL) {
    return 1;
}

/* Use the allocated memory */

free(numbers);
numbers = NULL;
```

Boas práticas:

- Verifique resultados de alocação.
- Libere recursos quando não forem mais necessários.
- Evite liberar memória duas vezes.
- Evite utilizar memória após sua liberação.
- Verifique cálculos de tamanho antes de alocar.
- Defina claramente a responsabilidade pela propriedade da memória.

## 8. Strings

Strings em C são sequências de caracteres terminadas em NULL (`\0`).

Exemplo:

```c
char name[] = "Daniel";
```

Funções comuns:

- strlen().
- strcmp().
- strcpy().
- strncpy().
- snprintf().
- strchr().

Cuidados importantes:

- Verifique limites dos buffers.
- Garanta espaço para o terminador NULL.
- Evite cópias sem controle de tamanho.
- Não utilize funções inseguras.
- Valide entradas externas.

Prefira operações que permitam controlar explicitamente o tamanho dos buffers.

## 9. Estruturas de dados

C permite implementar estruturas de dados manualmente.

Exemplos:

- Listas encadeadas.
- Pilhas.
- Filas.
- Árvores.
- Hash tables.
- Grafos.

Utilize structs para agrupar dados relacionados.

Exemplo:

```c
typedef struct {
    int id;
    char name[100];
} User;
```

Considere gerenciamento de memória e propriedade dos elementos.

## 10. Modularização

Organize projetos utilizando arquivos `.c` e `.h`.

Exemplo:

```text
project/
├── include/
│   └── calculator.h
├── src/
│   ├── calculator.c
│   └── main.c
└── Makefile
```

Boas práticas:

- Declare interfaces nos headers.
- Implemente funcionalidades nos arquivos fonte.
- Utilize include guards.
- Evite dependências circulares.
- Reduza o acoplamento.
- Organize módulos por responsabilidade.

## 11. Compilação

Compiladores comuns:

- GCC.
- Clang.
- MSVC.

Exemplo:

```bash
gcc -Wall -Wextra -Wpedantic -std=c17 main.c -o program
```

Opções úteis:

- `-Wall`: habilita diversos avisos.
- `-Wextra`: habilita avisos adicionais.
- `-Wpedantic`: verifica conformidade com o padrão.
- `-std=c17`: define a versão do padrão C.

Não ignore avisos do compilador sem compreender sua origem.

## 12. Segurança em C

C exige atenção especial à segurança de memória.

Vulnerabilidades comuns:

- Buffer Overflow.
- Stack Overflow.
- Heap Overflow.
- Use-After-Free.
- Double Free.
- Memory Leak.
- Integer Overflow.
- Format String Vulnerability.
- Out-of-Bounds Read.
- Out-of-Bounds Write.
- Null Pointer Dereference.

Boas práticas:

- Validar todas as entradas.
- Verificar limites de arrays.
- Controlar tamanhos de buffers.
- Validar operações aritméticas.
- Gerenciar corretamente ponteiros.
- Evitar funções inseguras.
- Utilizar compiladores atualizados.
- Habilitar proteções disponíveis.
- Utilizar ferramentas de análise estática.

## 13. Ferramentas de análise

Ferramentas úteis:

- AddressSanitizer.
- UndefinedBehaviorSanitizer.
- Valgrind.
- GCC.
- Clang.
- Clang Static Analyzer.
- Cppcheck.
- GDB.

Sanitizers podem ajudar a identificar erros durante testes.

Eles não substituem uma auditoria de segurança completa.

## 14. Testes

Considere:

- Testes unitários.
- Testes de integração.
- Testes de limites.
- Testes com entradas inválidas.
- Testes de memória.
- Testes de desempenho.

Frameworks:

- Unity.
- CMocka.
- Check.

Inclua testes para situações extremas e condições de erro.

## 15. Diretrizes para o agente

Ao desenvolver ou analisar código C:

1. Identifique o compilador e a versão.
2. Verifique o padrão C utilizado.
3. Analise o gerenciamento de memória.
4. Verifique o uso de ponteiros.
5. Avalie limites de buffers.
6. Examine operações aritméticas.
7. Identifique possíveis comportamentos indefinidos.
8. Verifique tratamento de erros.
9. Avalie dependências.
10. Recomende testes apropriados.

Ao identificar uma vulnerabilidade, explique sua causa, impacto, condições necessárias e correção recomendada.

Não execute código desconhecido fora de um ambiente isolado e autorizado.

## 16. Documentação oficial

- ISO C: https://www.iso.org/
- C Reference: https://en.cppreference.com/w/c
- GCC: https://gcc.gnu.org/onlinedocs/
- Clang: https://clang.llvm.org/docs/
- SEI CERT C: https://wiki.sei.cmu.edu/confluence/display/c

