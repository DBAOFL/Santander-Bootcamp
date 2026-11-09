# Clean Code — Código Limpo

## 1. Objetivo

Este documento apresenta princípios e práticas para escrever código legível, organizado, compreensível e fácil de manter.

O objetivo é orientar o agente na criação, revisão e refatoração de código, priorizando clareza, simplicidade, qualidade e manutenção.

Código limpo não significa código curto ou excessivamente abstrato. Significa código que comunica sua intenção e resolve o problema sem complexidade desnecessária.

## 2. Princípios fundamentais

Um código de qualidade deve ser:

- Legível.
- Simples.
- Organizado.
- Consistente.
- Testável.
- Reutilizável quando apropriado.
- Fácil de modificar.
- Documentado quando necessário.

A prioridade deve ser a clareza, não a demonstração de conhecimento técnico.

## 3. Nomenclatura

Utilize nomes que expressem claramente a finalidade de variáveis, funções, classes e módulos.

Exemplo inadequado:

```python
x = 10
y = 5
z = x * y
```

Exemplo melhor:

```python
product_price = 10
quantity = 5
total_price = product_price * quantity
```

Boas práticas:

- Prefira nomes descritivos.
- Evite abreviações obscuras.
- Utilize convenções da linguagem.
- Mantenha consistência.
- Evite nomes excessivamente genéricos.
- Não utilize nomes que induzam a interpretações incorretas.

## 4. Funções

Funções devem possuir responsabilidades claras.

Boas práticas:

- Faça uma função executar uma tarefa bem definida.
- Evite funções excessivamente longas.
- Reduza parâmetros quando possível.
- Evite efeitos colaterais inesperados.
- Prefira retornos explícitos.
- Utilize nomes que descrevam ações.
- Evite níveis excessivos de aninhamento.

Exemplo:

```python
def calculate_discount(price, discount_percentage):
    return price * (discount_percentage / 100)


def calculate_final_price(price, discount_percentage):
    discount = calculate_discount(price, discount_percentage)
    return price - discount
```

A divisão em funções deve melhorar a compreensão, não criar abstrações desnecessárias.

## 5. Princípio DRY

DRY significa Don't Repeat Yourself.

A ideia é evitar duplicação de conhecimento e regras de negócio.

Quando uma mesma regra aparece em diferentes locais, considere centralizá-la.

Entretanto, nem toda repetição de código precisa ser abstraída.

Abstrações prematuras podem aumentar o acoplamento e dificultar a manutenção.

## 6. Princípio KISS

KISS significa Keep It Simple, Stupid.

Prefira soluções simples que atendam corretamente aos requisitos.

Evite:
- Arquiteturas excessivamente complexas.
- Abstrações sem necessidade.
- Dependências desnecessárias.
- Condições excessivamente aninhadas.
- Implementações difíceis de compreender.

Simplicidade não significa ignorar segurança, qualidade ou requisitos técnicos.

## 7. Princípio YAGNI

YAGNI significa You Aren't Gonna Need It.

Implemente o que o projeto realmente precisa.

Evite:
- Funcionalidades especulativas.
- Generalizações prematuras.
- Sistemas de configuração desnecessários.
- Complexidade baseada em necessidades hipotéticas.

Planeje a evolução sem implementar antecipadamente tudo o que poderia ser necessário.

## 8. SOLID

SOLID reúne cinco princípios de orientação a objetos.

### 8.1. Single Responsibility Principle

Uma classe ou módulo deve possuir uma responsabilidade bem definida.

Evite componentes que concentrem regras de negócio, acesso a dados, comunicação externa e apresentação simultaneamente.

### 8.2. Open/Closed Principle

Componentes devem permitir extensão sem exigir modificações constantes em estruturas estáveis.

Utilize abstrações quando houver necessidade real de extensibilidade.

### 8.3. Liskov Substitution Principle

Implementações derivadas devem respeitar os contratos estabelecidos por seus tipos base.

Uma substituição não deve quebrar o comportamento esperado.

### 8.4. Interface Segregation Principle

Prefira interfaces específicas a contratos excessivamente abrangentes.

Componentes não devem depender de operações que não utilizam.

### 8.5. Dependency Inversion Principle

Módulos de alto nível devem depender de abstrações, não diretamente de implementações concretas quando isso trouxer benefícios arquiteturais.

Evite aplicar SOLID mecanicamente em projetos pequenos.

## 9. Tratamento de erros

Erros devem ser tratados de maneira explícita e adequada.

Boas práticas:

- Não ignore exceções silenciosamente.
- Utilize exceções específicas.
- Não utilize erros para controlar fluxos normais sem necessidade.
- Registre informações úteis.
- Evite expor detalhes internos.
- Preserve informações importantes durante o tratamento.

Exemplo:

```python
try:
    result = perform_operation()
except FileNotFoundError:
    print("The requested file was not found.")
except PermissionError:
    print("Permission denied.")
```

O tratamento deve corresponder ao contexto da aplicação.

## 10. Comentários e documentação

Comentários devem explicar decisões e contextos que não são evidentes pelo código.

Evite comentários que apenas repetem instruções.

Exemplo desnecessário:

```python
# Increment the counter
counter += 1
```

Comentários úteis podem explicar:

- Decisões arquiteturais.
- Regras de negócio complexas.
- Limitações técnicas.
- Comportamentos inesperados.
- Motivos de uma implementação específica.

Documente APIs públicas e funcionalidades relevantes.

## 11. Organização do código

Separe responsabilidades em módulos e componentes coerentes.

Considere:

- Domínios.
- Funcionalidades.
- Camadas.
- Dependências.
- Responsabilidades.

Evite:
- Arquivos excessivamente grandes.
- Dependências circulares.
- Acoplamento desnecessário.
- Código duplicado.
- Módulos com responsabilidades incompatíveis.

A estrutura deve acompanhar a complexidade real do sistema.

## 12. Imutabilidade

Sempre que apropriado, prefira não modificar diretamente estruturas compartilhadas.

Benefícios:

- Menos efeitos colaterais.
- Maior previsibilidade.
- Facilidade de testes.
- Menor risco de alterações inesperadas.

A imutabilidade deve ser aplicada considerando as características da linguagem e o desempenho necessário.

## 13. Refatoração

Refatoração é a melhoria da estrutura interna do código sem alterar seu comportamento externo esperado.

Exemplos:

- Extrair funções.
- Simplificar condições.
- Renomear variáveis.
- Eliminar duplicações.
- Reduzir acoplamento.
- Organizar módulos.

Boas práticas:

1. Compreenda o comportamento existente.
2. Identifique o problema.
3. Garanta a existência de testes adequados.
4. Faça alterações pequenas.
5. Execute os testes.
6. Compare os resultados.
7. Documente mudanças relevantes.

Não misture refatorações amplas com alterações funcionais sem necessidade.

## 14. Testabilidade

Código deve ser estruturado de maneira que facilite sua validação.

Considere:

- Separação de responsabilidades.
- Dependências explícitas.
- Funções previsíveis.
- Interfaces bem definidas.
- Isolamento de operações externas.

Evite dependências globais difíceis de substituir durante testes.

## 15. Code Review

Uma revisão de código deve considerar:

- Correção funcional.
- Legibilidade.
- Segurança.
- Desempenho.
- Manutenção.
- Testes.
- Consistência.
- Compatibilidade.

Aponte problemas concretos e explique suas consequências.

Não solicite mudanças apenas por preferência estilística quando o padrão existente for adequado.

## 16. Diretrizes para o agente

Ao escrever ou revisar código:

1. Priorize legibilidade.
2. Utilize nomes descritivos.
3. Mantenha funções coesas.
4. Evite duplicação desnecessária.
5. Aplique SOLID quando apropriado.
6. Evite complexidade prematura.
7. Trate erros corretamente.
8. Documente decisões importantes.
9. Considere testabilidade.
10. Preserve o comportamento esperado.
11. Evite alterações sem justificativa.
12. Explique melhorias propostas.

O agente deve diferenciar problemas reais de qualidade de preferências pessoais de estilo.

## 17. Referências

- Clean Code — Robert C. Martin.
- Refactoring — Martin Fowler.
- The Pragmatic Programmer — Andrew Hunt e David Thomas.
- SOLID Principles — https://en.wikipedia.org/wiki/SOLID
- Google Engineering Practices: https://google.github.io/eng-practices/
