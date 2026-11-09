# JavaScript e TypeScript

## 1. Objetivo

Este documento apresenta os fundamentos, boas práticas, particularidades e recomendações de desenvolvimento utilizando JavaScript e TypeScript.

O objetivo é orientar o agente na criação, análise, manutenção e melhoria de aplicações desenvolvidas nessas linguagens.

## 2. JavaScript

JavaScript é uma linguagem de programação interpretada, dinâmica e multiparadigma, amplamente utilizada no desenvolvimento web.

Principais características:

- Tipagem dinâmica.
- Orientação a objetos baseada em protótipos.
- Suporte à programação funcional.
- Execução assíncrona.
- Event Loop.
- Compatibilidade com navegadores.
- Execução no servidor por meio de ambientes como Node.js.

### 2.1. Tipos de dados

Tipos primitivos:

- String.
- Number.
- BigInt.
- Boolean.
- Undefined.
- Null.
- Symbol.

Tipos de referência:

- Object.
- Array.
- Function.
- Date.
- Map.
- Set.

Boas práticas:

- Utilize `const` por padrão.
- Utilize `let` quando houver necessidade de reatribuição.
- Evite `var`.
- Evite conversões implícitas desnecessárias.
- Verifique valores potencialmente nulos ou indefinidos.

### 2.2. Declaração de variáveis

Exemplo:

```javascript
const name = "Daniel";
let age = 25;

age = 26;
```

Prefira nomes descritivos e evite variáveis com responsabilidades múltiplas.

### 2.3. Funções

JavaScript permite diferentes formas de declaração de funções.

Exemplo:

```javascript
function calculateTotal(price, quantity) {
    return price * quantity;
}

const calculateDiscount = (value, discount) => {
    return value - discount;
};
```

Boas práticas:

- Mantenha funções pequenas e objetivas.
- Evite efeitos colaterais desnecessários.
- Utilize nomes que representem a finalidade.
- Evite excesso de parâmetros.
- Separe responsabilidades.

### 2.4. Arrays e objetos

Exemplo:

```javascript
const user = {
    name: "Daniel",
    role: "Developer",
    active: true
};

const users = [
    { name: "Ana", active: true },
    { name: "Carlos", active: false }
];

const activeUsers = users.filter(user => user.active);
```

Utilize métodos apropriados:

- map().
- filter().
- reduce().
- find().
- some().
- every().
- includes().

Evite modificar estruturas compartilhadas sem necessidade.

## 3. Programação assíncrona

JavaScript utiliza um modelo de execução baseado no Event Loop.

Principais mecanismos:

- Callbacks.
- Promises.
- Async/Await.

### 3.1. Promises

Representam operações que podem ser concluídas ou rejeitadas futuramente.

Exemplo:

```javascript
fetch("https://api.example.com/users")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

### 3.2. Async/Await

Permite escrever código assíncrono de maneira mais legível.

Exemplo:

```javascript
async function getUsers() {
    try {
        const response = await fetch("https://api.example.com/users");

        if (!response.ok) {
            throw new Error("Failed to retrieve users");
        }

        return await response.json();
    } catch (error) {
        console.error("Request error:", error);
        throw error;
    }
}
```

Boas práticas:

- Trate erros de operações assíncronas.
- Evite bloquear o Event Loop.
- Utilize Promise.all() quando operações independentes puderem ocorrer simultaneamente.
- Evite criar operações assíncronas sem necessidade.
- Considere cancelamento de requisições quando apropriado.

## 4. Orientação a objetos

JavaScript suporta orientação a objetos utilizando protótipos e classes.

Exemplo:

```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getDetails() {
        return `${this.name} - ${this.email}`;
    }
}

const user = new User("Daniel", "daniel@example.com");
```

Princípios importantes:

- Encapsulamento.
- Abstração.
- Herança.
- Polimorfismo.
- Composição.

Prefira composição quando ela proporcionar menor acoplamento e maior flexibilidade.

## 5. TypeScript

TypeScript é um superset de JavaScript que adiciona tipagem estática e recursos adicionais ao desenvolvimento.

O código TypeScript normalmente é compilado para JavaScript.

Principais benefícios:

- Identificação antecipada de erros.
- Melhor autocomplete.
- Maior previsibilidade.
- Contratos explícitos.
- Melhor manutenção.
- Facilidade de refatoração.

## 6. Tipagem no TypeScript

### 6.1. Tipos básicos

Exemplo:

```typescript
const name: string = "Daniel";
const age: number = 25;
const active: boolean = true;
const skills: string[] = ["Python", "JavaScript", "SQL"];
```

Sempre que possível, permita que o TypeScript infira tipos simples.

### 6.2. Interfaces

Interfaces definem contratos para estruturas de dados.

Exemplo:

```typescript
interface User {
    id: number;
    name: string;
    email: string;
    active?: boolean;
}
```

### 6.3. Type

O recurso `type` permite criar aliases e composições de tipos.

Exemplo:

```typescript
type UserRole = "admin" | "user" | "moderator";

type User = {
    id: number;
    name: string;
    role: UserRole;
};
```

### 6.4. Union Types

Permitem que uma variável aceite diferentes tipos.

Exemplo:

```typescript
type Identifier = string | number;

function findUser(id: Identifier) {
    console.log(id);
}
```

### 6.5. Generics

Permitem criar estruturas reutilizáveis com tipagem flexível.

Exemplo:

```typescript
function identity<T>(value: T): T {
    return value;
}

const result = identity<string>("Hello");
```

Utilize generics quando houver necessidade real de reutilização tipada.

### 6.6. Enums

Permitem definir conjuntos de valores nomeados.

Exemplo:

```typescript
enum Status {
    Pending,
    Approved,
    Rejected
}
```

Considere utilizar union types de strings quando forem mais simples e adequados.

## 7. Boas práticas de TypeScript

- Evite utilizar `any` indiscriminadamente.
- Prefira `unknown` quando o tipo ainda não for conhecido.
- Utilize interfaces e types para estabelecer contratos.
- Habilite `strict` no tsconfig.json.
- Utilize tipos de retorno quando melhorarem a clareza.
- Evite duplicação de definições.
- Utilize tipos específicos.
- Trate corretamente valores nulos e indefinidos.
- Prefira inferência de tipos quando for suficiente.

Exemplo de configuração:

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "NodeNext",
        "strict": true,
        "noImplicitAny": true,
        "strictNullChecks": true,
        "esModuleInterop": true,
        "skipLibCheck": true
    }
}
```

A configuração deve ser adaptada ao ambiente e à arquitetura do projeto.

## 8. Node.js

Node.js permite executar JavaScript fora dos navegadores.

É amplamente utilizado para:

- APIs.
- Aplicações backend.
- Ferramentas CLI.
- Automação.
- Serviços.
- Aplicações em tempo real.

Boas práticas:

- Utilize versões LTS quando apropriado.
- Gerencie dependências com npm, pnpm ou Yarn.
- Utilize variáveis de ambiente para configurações.
- Não exponha segredos no código.
- Trate erros adequadamente.
- Evite bloquear o Event Loop.
- Organize módulos por responsabilidade.
- Utilize logging estruturado.

## 9. Gerenciamento de dependências

Ferramentas comuns:

- npm.
- pnpm.
- Yarn.

Boas práticas:

- Mantenha package.json organizado.
- Versione o arquivo de lock.
- Avalie dependências antes de instalá-las.
- Evite dependências desnecessárias.
- Atualize pacotes de maneira controlada.
- Verifique vulnerabilidades conhecidas.
- Não instale pacotes desconhecidos sem avaliar sua procedência.

## 10. Desenvolvimento Frontend

Frameworks e bibliotecas comuns:

- React.
- Vue.
- Angular.
- Svelte.
- Next.js.
- Nuxt.

Boas práticas:

- Separe componentes por responsabilidade.
- Evite componentes excessivamente grandes.
- Centralize lógica reutilizável.
- Utilize gerenciamento de estado apropriado.
- Considere acessibilidade.
- Implemente tratamento de erros.
- Evite manipulação desnecessária do DOM.
- Considere desempenho e carregamento.

## 11. Desenvolvimento Backend

Frameworks comuns:

- Express.
- Fastify.
- NestJS.
- Hono.
- Koa.

Boas práticas:

- Separe rotas, controladores e serviços quando apropriado.
- Utilize validação de entrada.
- Implemente autenticação e autorização.
- Centralize tratamento de erros.
- Utilize consultas parametrizadas.
- Não exponha informações internas em respostas.
- Implemente logging.
- Documente APIs.

## 12. Segurança em JavaScript e TypeScript

Riscos comuns:

- Cross-Site Scripting (XSS).
- SQL Injection.
- Command Injection.
- Server-Side Request Forgery (SSRF).
- Prototype Pollution.
- Insecure Direct Object Reference (IDOR).
- Exposição de informações sensíveis.
- Dependências vulneráveis.

Boas práticas:

- Valide entradas no servidor.
- Utilize bibliotecas confiáveis.
- Evite eval().
- Evite executar comandos com entradas não confiáveis.
- Utilize consultas parametrizadas.
- Proteja tokens e credenciais.
- Implemente controles de autorização.
- Configure CORS corretamente.
- Utilize HTTPS.
- Mantenha dependências atualizadas.
- Aplique Content Security Policy quando apropriado.

Nunca considere a validação exclusivamente no frontend suficiente para proteger uma aplicação.

## 13. Testes

Ferramentas comuns:

- Jest.
- Vitest.
- Mocha.
- Playwright.
- Cypress.
- Testing Library.

Tipos de testes:

- Unitários.
- Integração.
- End-to-end.
- Regressão.

Boas práticas:

- Teste comportamentos importantes.
- Cubra casos de sucesso e falha.
- Teste entradas inválidas.
- Considere condições de concorrência.
- Evite testes excessivamente acoplados à implementação.

## 14. Qualidade e padronização

Ferramentas recomendadas:

- ESLint.
- Prettier.
- TypeScript Compiler.
- EditorConfig.

Boas práticas:

- Padronize formatação.
- Utilize linting.
- Evite código duplicado.
- Prefira nomes claros.
- Documente decisões importantes.
- Mantenha funções coesas.
- Revise alterações antes de integrá-las.

## 15. Organização de projetos

Uma possível estrutura para um backend:

```text
src/
├── config/
├── controllers/
├── services/
├── repositories/
├── models/
├── routes/
├── middlewares/
├── utils/
├── types/
└── app.ts

tests/
├── unit/
└── integration/

package.json
tsconfig.json
```

A estrutura deve ser adaptada ao tamanho e às necessidades do projeto.

Não crie camadas desnecessárias apenas para seguir uma convenção.

## 16. Diretrizes para o agente

Ao desenvolver ou analisar projetos JavaScript e TypeScript:

1. Identifique o ambiente de execução.
2. Identifique a versão da linguagem e das ferramentas.
3. Verifique se o projeto utiliza JavaScript ou TypeScript.
4. Analise a estrutura existente antes de propor mudanças.
5. Respeite os padrões já estabelecidos quando forem adequados.
6. Prefira soluções simples, legíveis e tipadas.
7. Considere desempenho e escalabilidade.
8. Avalie riscos de segurança.
9. Recomende testes apropriados.
10. Evite adicionar dependências sem justificativa.
11. Explique decisões técnicas relevantes.
12. Consulte a documentação oficial quando necessário.

Ao identificar problemas, diferencie erros de implementação, problemas de arquitetura, oportunidades de melhoria e vulnerabilidades de segurança.

Não reescreva partes funcionais do projeto sem necessidade.

## 17. Documentação oficial

- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- TypeScript: https://www.typescriptlang.org/docs/
- Node.js: https://nodejs.org/docs/
- npm: https://docs.npmjs.com/
- React: https://react.dev/
- Vue: https://vuejs.org/guide/
- Angular: https://angular.dev/
- Next.js: https://nextjs.org/docs
- Express: https://expressjs.com/
- NestJS: https://docs.nestjs.com/

