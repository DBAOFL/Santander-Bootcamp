# API Development — Desenvolvimento de APIs

## 1. Objetivo

Este documento apresenta conceitos, padrões, arquiteturas e boas práticas para desenvolvimento, documentação, integração e segurança de APIs.

O objetivo é orientar a criação de interfaces de comunicação confiáveis, seguras, escaláveis e fáceis de manter.

## 2. Conceitos fundamentais

API (Application Programming Interface) é uma interface que permite a comunicação entre diferentes sistemas ou componentes de software.

Uma API define:
- Operações disponíveis.
- Parâmetros de entrada.
- Formatos de dados.
- Respostas.
- Regras de autenticação.
- Regras de autorização.
- Tratamento de erros.

Exemplos de utilização:
- Comunicação entre frontend e backend.
- Integração entre serviços.
- Aplicações mobile.
- Integração com serviços externos.
- Arquiteturas de microsserviços.

## 3. Tipos de APIs

### 3.1. REST

REST é um estilo arquitetural amplamente utilizado para APIs HTTP.

Características:
- Recursos identificados por URLs.
- Utilização dos métodos HTTP.
- Comunicação stateless.
- Representação de dados frequentemente em JSON.
- Separação entre cliente e servidor.

Métodos HTTP comuns:

- GET: consultar recursos.
- POST: criar recursos ou executar operações.
- PUT: substituir um recurso.
- PATCH: atualizar parcialmente.
- DELETE: remover recursos.

Exemplo:

```http
GET /api/users/10
```

Resposta:

```json
{
    "id": 10,
    "name": "Daniel",
    "email": "daniel@example.com"
}
```

Boas práticas:
- Utilize URLs consistentes.
- Respeite a semântica HTTP.
- Utilize códigos de status apropriados.
- Evite retornar informações desnecessárias.
- Implemente paginação.
- Documente os endpoints.

### 3.2. GraphQL

GraphQL permite que clientes solicitem exatamente os dados necessários.

Características:
- Schema tipado.
- Queries.
- Mutations.
- Subscriptions.
- Redução de requisições desnecessárias em determinados cenários.

Cuidados:
- Controle de profundidade das consultas.
- Limitação de complexidade.
- Autorização por campo ou recurso.
- Proteção contra consultas excessivamente custosas.

### 3.3. gRPC

gRPC é um framework de comunicação entre serviços.

Características:
- Utilização de Protocol Buffers.
- Comunicação baseada em HTTP/2.
- Suporte a streaming.
- Contratos definidos.
- Adequado para comunicação entre serviços.

### 3.4. WebSockets

Permitem comunicação bidirecional persistente entre cliente e servidor.

Aplicações:
- Chats.
- Notificações em tempo real.
- Monitoramento.
- Colaboração simultânea.
- Atualizações em tempo real.

Cuidados:
- Autenticação.
- Autorização.
- Limitação de conexões.
- Controle de mensagens.
- Gerenciamento de sessões.

## 4. Arquitetura de APIs

Uma arquitetura comum pode conter:

- Routes: definição dos endpoints.
- Controllers: recebimento e tratamento das requisições.
- Services: regras de negócio.
- Repositories: acesso aos dados.
- Models: representação das entidades.
- Middlewares: processamento intermediário.
- Schemas: validação de dados.
- Config: configurações.

Exemplo de estrutura:

```text
src/
├── config/
├── controllers/
├── services/
├── repositories/
├── models/
├── routes/
├── middlewares/
├── schemas/
├── utils/
└── app.ts
```

A estrutura deve ser adaptada à complexidade do projeto.

Evite criar camadas sem necessidade.

## 5. Métodos HTTP e códigos de status

Códigos comuns:

### Sucesso

- 200 OK.
- 201 Created.
- 202 Accepted.
- 204 No Content.

### Erros do cliente

- 400 Bad Request.
- 401 Unauthorized.
- 403 Forbidden.
- 404 Not Found.
- 405 Method Not Allowed.
- 409 Conflict.
- 422 Unprocessable Content.
- 429 Too Many Requests.

### Erros do servidor

- 500 Internal Server Error.
- 502 Bad Gateway.
- 503 Service Unavailable.
- 504 Gateway Timeout.

O agente deve escolher códigos de acordo com a semântica da operação.

Não utilize sempre 200 para representar operações bem-sucedidas ou malsucedidas.

## 6. Validação de entradas

Toda entrada deve ser considerada não confiável.

Valide:
- Tipos.
- Formatos.
- Tamanhos.
- Campos obrigatórios.
- Intervalos.
- Estruturas.
- Regras de negócio.

Exemplo utilizando Zod:

```typescript
import { z } from "zod";

const userSchema = z.object({
    name: z.string().min(2).max(100),
    email: z.string().email(),
    age: z.number().int().positive()
});

const result = userSchema.safeParse(request.body);

if (!result.success) {
    throw new Error("Invalid request data");
}
```

A validação deve ocorrer no servidor, mesmo quando o frontend também valida os dados.

## 7. Autenticação e autorização

### 7.1. Autenticação

Determina a identidade de quem realiza uma requisição.

Mecanismos comuns:

- Sessões.
- JWT.
- OAuth 2.0.
- OpenID Connect.
- API Keys.
- mTLS.

### 7.2. Autorização

Determina quais recursos e operações uma identidade pode acessar.

Modelos comuns:

- RBAC: Role-Based Access Control.
- ABAC: Attribute-Based Access Control.
- ACL: Access Control Lists.

Autenticação não substitui autorização.

Um usuário autenticado não deve receber acesso automático a todos os recursos.

### 7.3. JWT

JWT é um formato de token utilizado para transportar claims.

Cuidados:
- Validar assinatura.
- Validar emissor.
- Validar audiência.
- Verificar expiração.
- Utilizar algoritmos permitidos explicitamente.
- Evitar informações sensíveis no payload.
- Planejar revogação e renovação.

Não considere o conteúdo de um JWT secreto apenas porque está codificado.

## 8. Segurança de APIs

Riscos importantes:

- Broken Object Level Authorization (BOLA).
- Broken Authentication.
- Broken Function Level Authorization.
- Unrestricted Resource Consumption.
- Mass Assignment.
- Security Misconfiguration.
- Injection.
- SSRF.
- Exposição de informações sensíveis.

Boas práticas:

- Validar entradas.
- Aplicar menor privilégio.
- Verificar autorização em cada operação.
- Utilizar HTTPS.
- Implementar rate limiting.
- Proteger credenciais.
- Evitar mensagens de erro excessivamente detalhadas.
- Controlar tamanho de requisições.
- Restringir origens quando necessário.
- Manter dependências atualizadas.

Consulte o OWASP API Security Top 10.

## 9. Tratamento de erros

As APIs devem apresentar respostas consistentes.

Exemplo:

```json
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "The provided data is invalid",
        "details": [
            {
                "field": "email",
                "message": "Invalid email format"
            }
        ]
    }
}
```

Boas práticas:

- Não retornar stack traces em produção.
- Não revelar credenciais ou segredos.
- Utilizar códigos de erro consistentes.
- Registrar detalhes técnicos nos logs.
- Diferenciar erros do cliente e do servidor.

## 10. Paginação e filtros

APIs que retornam grandes quantidades de dados devem implementar mecanismos de paginação.

Modelos comuns:

- Offset-based pagination.
- Cursor-based pagination.

Exemplo:

```http
GET /api/users?page=1&limit=20
```

Considere:
- Limites máximos.
- Ordenação.
- Filtros permitidos.
- Desempenho.
- Consistência dos resultados.

Nunca permita que parâmetros arbitrários sejam utilizados diretamente em consultas SQL.

## 11. Versionamento

O versionamento permite evoluir uma API preservando compatibilidade.

Exemplo:

```text
/api/v1/users
/api/v2/users
```

Boas práticas:
- Evite alterações incompatíveis sem planejamento.
- Documente mudanças.
- Defina períodos de descontinuação.
- Preserve compatibilidade quando possível.
- Comunique alterações aos consumidores.

## 12. Documentação

Ferramentas comuns:

- OpenAPI.
- Swagger UI.
- Redoc.
- Postman.
- Insomnia.

Uma documentação adequada deve apresentar:
- Endpoints.
- Métodos HTTP.
- Parâmetros.
- Exemplos.
- Respostas.
- Códigos de erro.
- Autenticação.
- Regras de autorização.

## 13. Testes de APIs

Tipos de testes:

- Unitários.
- Integração.
- Contrato.
- End-to-end.
- Segurança.
- Desempenho.

Verifique:
- Respostas esperadas.
- Entradas inválidas.
- Usuários sem permissão.
- Recursos inexistentes.
- Limites de requisições.
- Falhas de serviços externos.
- Comportamento sob concorrência.

Ferramentas:
- Postman.
- Insomnia.
- Bruno.
- REST Assured.
- Supertest.
- Playwright.
- pytest.

## 14. Desempenho e escalabilidade

Considere:

- Cache.
- Paginação.
- Consultas eficientes.
- Processamento assíncrono.
- Filas de mensagens.
- Rate limiting.
- Connection pooling.
- Balanceamento de carga.
- Monitoramento.

Não introduza otimizações complexas sem identificar necessidades reais.

## 15. Diretrizes para o agente

Ao desenvolver ou analisar uma API:

1. Identifique o objetivo e os consumidores.
2. Determine o estilo arquitetural adequado.
3. Analise os contratos existentes.
4. Verifique validação de entradas.
5. Avalie autenticação e autorização.
6. Examine os códigos HTTP.
7. Verifique tratamento de erros.
8. Avalie riscos de segurança.
9. Considere desempenho e escalabilidade.
10. Recomende testes.
11. Documente decisões relevantes.

Antes de modificar uma API existente, considere compatibilidade com os clientes que já utilizam seus endpoints.

Nunca presuma que um endpoint está protegido apenas porque exige autenticação.

## 16. Documentação oficial

- HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP
- REST: https://restfulapi.net/
- OpenAPI: https://www.openapis.org/
- GraphQL: https://graphql.org/learn/
- gRPC: https://grpc.io/docs/
- OWASP API Security: https://owasp.org/www-project-api-security/
- OAuth 2.0: https://oauth.net/2/

