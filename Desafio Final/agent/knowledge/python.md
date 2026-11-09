# Python — Linguagem de Programação Python

## 1. Objetivo

Este documento apresenta fundamentos, características, boas práticas e recomendações de desenvolvimento utilizando Python.

O objetivo é orientar o agente na criação, análise, manutenção e auditoria de aplicações Python, considerando legibilidade, arquitetura, desempenho, segurança e qualidade.

## 2. Características da linguagem

Python é uma linguagem de programação de alto nível, interpretada, multiparadigma e de tipagem dinâmica.

É amplamente utilizada em:

- Automação.
- Desenvolvimento backend.
- Inteligência artificial.
- Machine Learning.
- Ciência de dados.
- Cibersegurança.
- Análise de informações.
- Scripts.
- DevOps.

Características:

- Sintaxe simples.
- Tipagem dinâmica.
- Gerenciamento automático de memória.
- Orientação a objetos.
- Programação funcional.
- Grande ecossistema de bibliotecas.

## 3. Estrutura básica

Exemplo:

```python
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
```

Boas práticas:

- Utilize nomes descritivos.
- Organize funcionalidades em módulos.
- Evite arquivos excessivamente grandes.
- Utilize funções reutilizáveis.
- Siga a PEP 8.
- Evite código executado automaticamente durante importações sem necessidade.

## 4. Tipos de dados

Tipos fundamentais:

- int.
- float.
- complex.
- str.
- bool.
- NoneType.

Estruturas comuns:

- list.
- tuple.
- set.
- dict.

Exemplo:

```python
user = {
    "name": "Daniel",
    "age": 25,
    "active": True
}
```

Escolha estruturas adequadas ao comportamento esperado.

## 5. Tipagem

Python utiliza tipagem dinâmica, mas oferece suporte a type hints.

Exemplo:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

Boas práticas:

- Utilize type hints em projetos relevantes.
- Prefira tipos explícitos quando melhorarem a compreensão.
- Evite anotações incorretas.
- Utilize ferramentas de verificação estática.
- Considere mypy ou Pyright.

### Tipos avançados

O módulo typing oferece recursos como:

- Optional.
- Union.
- Literal.
- Protocol.
- TypedDict.
- Generic.
- TypeVar.

Exemplo:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Daniel"

    return None
```

## 6. Funções

Funções devem possuir responsabilidades claras.

Exemplo:

```python
def calculate_discount(price: float, percentage: float) -> float:
    return price * (percentage / 100)


def calculate_final_price(price: float, percentage: float) -> float:
    discount = calculate_discount(price, percentage)
    return price - discount
```

Boas práticas:

- Evite funções excessivamente longas.
- Utilize nomes descritivos.
- Evite parâmetros desnecessários.
- Prefira retornos explícitos.
- Evite efeitos colaterais.
- Utilize valores padrão com cuidado.

Evite utilizar objetos mutáveis como valores padrão de argumentos.

Exemplo problemático:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Alternativa:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

## 7. Orientação a objetos

Python suporta orientação a objetos.

Exemplo:

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_details(self) -> str:
        return f"{self.name} - {self.email}"
```

Boas práticas:

- Utilize classes quando representarem conceitos relevantes.
- Prefira composição quando apropriado.
- Evite hierarquias excessivas.
- Mantenha responsabilidades claras.
- Utilize properties quando fizer sentido.

## 8. Recursos da linguagem

Recursos importantes:

- List comprehensions.
- Dictionary comprehensions.
- Generators.
- Decorators.
- Context managers.
- Iterators.
- Lambda functions.
- Dataclasses.
- Pattern matching.

### List comprehensions

Exemplo:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
```

Utilize comprehensions quando melhorarem a legibilidade.

### Generators

Permitem produzir valores sob demanda.

Exemplo:

```python
def generate_numbers(limit):
    for number in range(limit):
        yield number
```

São úteis para trabalhar com grandes conjuntos de dados sem armazenar tudo simultaneamente.

### Context managers

Gerenciam recursos automaticamente.

Exemplo:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Prefira context managers para recursos que precisam ser encerrados corretamente.

## 9. Programação assíncrona

Python oferece suporte à programação assíncrona com asyncio.

Exemplo:

```python
import asyncio

async def main():
    print("Starting operation")
    await asyncio.sleep(1)
    print("Operation completed")


asyncio.run(main())
```

Recursos:

- async.
- await.
- asyncio.
- Tasks.
- Futures.

Utilize programação assíncrona quando houver operações de I/O concorrentes.

Ela não acelera automaticamente tarefas limitadas por CPU.

## 10. Gerenciamento de dependências

Ferramentas comuns:

- pip.
- venv.
- Poetry.
- uv.
- Pipenv.

Boas práticas:

- Utilize ambientes virtuais.
- Versione dependências.
- Evite instalações globais desnecessárias.
- Avalie pacotes antes de instalá-los.
- Verifique vulnerabilidades.
- Mantenha arquivos de dependências organizados.

Exemplo:

```bash
python -m venv .venv
```

Ativação no Linux:

```bash
source .venv/bin/activate
```

Instalação:

```bash
python -m pip install requests
```

## 11. Organização de projetos

Estrutura possível:

```text
project/
├── src/
│   └── application/
│       ├── __init__.py
│       ├── main.py
│       ├── services/
│       ├── models/
│       └── utils/
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

Adapte a estrutura ao tamanho do projeto.

Evite criar camadas desnecessárias.

## 12. Desenvolvimento backend

Frameworks comuns:

- Django.
- Flask.
- FastAPI.
- Litestar.

Boas práticas:

- Valide entradas.
- Utilize schemas.
- Separe regras de negócio.
- Proteja endpoints.
- Implemente autenticação e autorização.
- Trate exceções.
- Documente APIs.
- Gerencie conexões com bancos.

## 13. Segurança em Python

Riscos comuns:

- SQL Injection.
- Command Injection.
- Path Traversal.
- Insecure Deserialization.
- SSRF.
- Exposição de credenciais.
- Dependências vulneráveis.
- Uso inseguro de eval() e exec().
- Desserialização insegura com pickle.

Boas práticas:

- Valide entradas.
- Utilize consultas parametrizadas.
- Evite executar comandos com entradas não confiáveis.
- Não utilize eval() para processar entradas externas.
- Evite pickle com dados não confiáveis.
- Proteja segredos.
- Utilize bibliotecas atualizadas.
- Aplique menor privilégio.
- Controle permissões de arquivos.
- Utilize HTTPS.

## 14. Tratamento de erros

Utilize exceções específicas.

Exemplo:

```python
try:
    result = perform_operation()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
```

Boas práticas:

- Não ignore exceções.
- Evite capturar Exception sem necessidade.
- Preserve informações importantes.
- Não exponha detalhes internos em respostas públicas.
- Registre erros de maneira apropriada.

## 15. Testes

Ferramentas comuns:

- pytest.
- unittest.
- Hypothesis.
- coverage.py.

Tipos:

- Unitários.
- Integração.
- End-to-end.
- Propriedades.
- Regressão.

Boas práticas:

- Teste comportamentos.
- Inclua casos extremos.
- Teste entradas inválidas.
- Isole dependências externas quando necessário.
- Mantenha testes reproduzíveis.

## 16. Qualidade de código

Ferramentas:

- Ruff.
- Black.
- isort.
- mypy.
- Pyright.
- Pylint.
- Bandit.

Utilize ferramentas de linting, formatação e análise estática de acordo com as necessidades do projeto.

## 17. Desempenho

Considere:

- Complexidade algorítmica.
- Estruturas de dados.
- Geradores.
- Processamento em lotes.
- Cache.
- Multiprocessing.
- Concorrência.
- Profiling.

Ferramentas:

- cProfile.
- timeit.
- py-spy.
- Scalene.

Não otimize prematuramente.

Meça o comportamento antes de propor mudanças de desempenho.

## 18. Diretrizes para o agente

Ao desenvolver ou analisar Python:

1. Identifique a versão utilizada.
2. Analise a estrutura existente.
3. Verifique dependências.
4. Respeite a PEP 8.
5. Utilize type hints quando apropriado.
6. Avalie o gerenciamento de recursos.
7. Verifique tratamento de erros.
8. Analise possíveis vulnerabilidades.
9. Recomende testes.
10. Considere desempenho.
11. Evite dependências desnecessárias.
12. Preserve compatibilidade.

## 19. Documentação oficial

- Python: https://docs.python.org/3/
- PEP 8: https://peps.python.org/pep-0008/
- Python Typing: https://docs.python.org/3/library/typing.html
- Pytest: https://docs.pytest.org/
- FastAPI: https://fastapi.tiangolo.com/
- Django: https://docs.djangoproject.com/
- Flask: https://flask.palletsprojects.com/
