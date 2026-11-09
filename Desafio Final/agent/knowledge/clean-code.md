# Clean Code — Código Limpo

## 1. Objetivo

Este documento reúne princípios para produzir código legível, organizado, compreensível e fácil de manter.

Código limpo não significa código excessivamente abstrato ou sofisticado.

Significa código cuja intenção pode ser compreendida sem esforço desnecessário.

## 2. Legibilidade

O código deve comunicar claramente sua finalidade.

Priorize:

    Nomes significativos.
    Estruturas simples.
    Funções pequenas e coesas.
    Organização consistente.
    Poucas dependências desnecessárias.
    Tratamento explícito de erros.

Evite otimizar a quantidade de linhas em detrimento da compreensão.

## 3. Nomenclatura

Nomes devem representar claramente a responsabilidade de variáveis, funções, classes e módulos.

Exemplo inadequado:

```python 
x = 150 
y = 20 
z = x * y 
```

Exemplo melhor:

```python 
product_price = 150 
quantity = 20 
total_price = product_price * quantity 
```

Evite:

    Abreviações sem significado.
    Nomes genéricos.
    Nomes enganosos.
    Siglas desnecessárias.
    Nomes que escondam efeitos colaterais.

Respeite as convenções da linguagem.

## 4. Funções

Uma função deve representar uma responsabilidade clara.

Boas práticas:

    Manter funções focadas.
    Reduzir parâmetros desnecessários.
    Evitar efeitos colaterais inesperados.
    Utilizar nomes que descrevam ações.
    Evitar funções excessivamente longas.
    Separar responsabilidades diferentes.

Exemplo:

```python 
def calculate_total(price, quantity): 
    return price * quantity

def apply_discount(total, discount): 
    return total * (1 - discount) 
```

Evite criar funções pequenas artificialmente quando isso prejudicar a compreensão.

## 5. Responsabilidade única

Uma função, classe ou módulo deve possuir uma responsabilidade bem definida.

O princípio da responsabilidade única não significa que cada função deve realizar apenas uma operação matemática.

Significa que suas responsabilidades devem permanecer coesas e relacionadas.

## 6. DRY — Don't Repeat Yourself

Evite duplicação de lógica.

Quando uma mesma regra aparece em diversos locais, considere centralizá-la.

Entretanto, nem toda repetição deve ser eliminada.

Abstrações prematuras podem aumentar o acoplamento e dificultar a manutenção.

Priorize eliminar duplicações de conhecimento e regras de negócio.

## 7. KISS — Keep It Simple

Prefira soluções simples e compreensíveis.

Evite:

    Complexidade sem necessidade.
    Abstrações prematuras.
    Dependências excessivas.
    Arquiteturas desproporcionais.
    Otimizações sem evidências.

Simplicidade não significa ignorar requisitos importantes.

## 8. YAGNI — You Aren't Gonna Need It

Não implemente funcionalidades hipotéticas sem necessidade identificada.

Desenvolva com base nos requisitos atuais e preserve possibilidades razoáveis de evolução.

Evite antecipar complexidade que não possui justificativa.

## 9. Tratamento de erros

Erros devem ser tratados de forma explícita e adequada.

Boas práticas:

    Utilizar exceções apropriadas.
    Não ignorar erros silenciosamente.
    Preservar informações úteis para diagnóstico.
    Evitar expor detalhes internos aos usuários.
    Registrar erros relevantes.
    Não utilizar exceções para controlar fluxos normais sem justificativa.

## 10. Comentários e documentação

Comentários devem explicar decisões, restrições e comportamentos que não sejam evidentes.

Evite comentários que apenas repetem o código.

Exemplo desnecessário:

```python
# Incrementa o contador

counter += 1 
```

Exemplo útil:

```python
# Mantemos a margem de segurança para evitar arredondamentos que poderiam ultrapassar o limite financeiro permitido.

```

A documentação deve acompanhar o código e permanecer atualizada.

## 11. Organização

Organize o código conforme suas responsabilidades.

Considere:

    Separação por módulos.
    Separação entre regras de negócio e infraestrutura.
    Organização de configurações.
    Isolamento de componentes.
    Estrutura previsível de diretórios.

Evite criar estruturas excessivamente profundas ou fragmentadas.

## 12. Imutabilidade e efeitos colaterais

Sempre que adequado, prefira operações previsíveis.

Considere:

    Evitar alterações desnecessárias de estado.
    Limitar efeitos colaterais.
    Não modificar argumentos inesperadamente.
    Tornar dependências explícitas.
    Utilizar estruturas imutáveis quando apropriado.

A imutabilidade pode facilitar testes e reduzir erros.

## 13. Acoplamento e coesão

### Baixo acoplamento

Componentes devem depender o mínimo possível de detalhes internos de outros componentes.

### Alta coesão

Elementos relacionados devem permanecer organizados juntos.

Esses princípios facilitam manutenção, testes e evolução.

## 14. Refatoração

Refatoração é a melhoria da estrutura interna do código sem alterar seu comportamento externo esperado.

Exemplos:

    Extrair funções.
    Renomear variáveis.
    Eliminar duplicações.
    Simplificar condições.
    Separar responsabilidades.
    Reduzir acoplamento.

Antes de refatorar:

    - Compreenda o comportamento atual.
    - Identifique os problemas.
    - Considere testes existentes.
    - Faça alterações pequenas.
    - Execute testes de regressão.

## 15. Código limpo e desempenho

Legibilidade e desempenho devem ser equilibrados.

Não realize otimizações prematuras.

Quando houver problemas de desempenho:

    - Identifique o gargalo.
    - Colete métricas.
    - Analise a causa.
    - Escolha uma otimização adequada.
    - Compare os resultados.

Não torne o código significativamente mais complexo sem benefício comprovado.

## 16. Diretrizes para o agente

Ao revisar código:

    - Avalie legibilidade.
    - Examine nomenclatura.
    - Identifique duplicações.
    - Avalie responsabilidades.
    - Observe complexidade.
    - Examine tratamento de erros.
    - Identifique abstrações desnecessárias.
    - Considere manutenção futura.

Não classifique automaticamente um código como ruim por possuir muitas linhas ou por não utilizar determinado padrão de projeto.

Avalie o contexto e justifique as recomendações.
