# DIO Agent — Development & Cybersecurity Specialist

Agente especializado em desenvolvimento de software, engenharia de software e cibersegurança, desenvolvido a partir do Hermes Agent como projeto de conclusão do Santander Bootcamp Cybersegurança: Do Zero à Prática.

O projeto tem como objetivo transformar um agente de IA genérico em um assistente técnico especializado, capaz de analisar vulnerabilidades, orientar correções, auxiliar no desenvolvimento de aplicações e planejar projetos de software.

---

## 🎯 Objetivo do projeto

Desenvolver uma especialização para o agente que vá além de responder perguntas técnicas.

O agente deve compreender o contexto apresentado, identificar problemas, avaliar riscos, propor soluções e orientar o usuário durante o processo de desenvolvimento e segurança.

A especialização foi organizada em três áreas principais:

- **Cibersegurança:** identificação, análise, classificação e correção de vulnerabilidades.
- **Engenharia de software:** desenvolvimento, revisão, organização e manutenção de aplicações.
- **Planejamento de projetos:** levantamento de requisitos, definição de arquitetura e organização de etapas de desenvolvimento.

A proposta é utilizar essas especializações tanto em projetos de estudo quanto em aplicações práticas de desenvolvimento e segurança.

## 🧠 Especializações desenvolvidas

### 1. Security Audit

Skill dedicada à análise de segurança de aplicações, códigos, configurações e processos.

Seu objetivo é identificar possíveis vulnerabilidades, avaliar seus impactos e recomendar medidas de correção.

Principais atividades:

- Auditoria de código-fonte.
- Identificação de vulnerabilidades.
- Análise de configurações inseguras.
- Avaliação de riscos.
- Classificação de severidade.
- Recomendações de correção.
- Validação de medidas de segurança.

A análise considera impacto, probabilidade e severidade, evitando apresentar hipóteses como vulnerabilidades confirmadas.

### 2. Software Engineering

Skill dedicada ao desenvolvimento e à engenharia de software.

Seu objetivo é orientar a construção de aplicações organizadas, eficientes, seguras e sustentáveis.

Principais atividades:

- Desenvolvimento de aplicações.
- Revisão e refatoração de código.
- Aplicação de boas práticas.
- Organização de projetos.
- Desenvolvimento de APIs.
- Implementação de testes.
- Avaliação de arquitetura.
- Melhoria de qualidade e manutenibilidade.

### 3. Project Planning

Skill dedicada ao planejamento e à estruturação de projetos.

Seu objetivo é transformar ideias em projetos organizados, com requisitos, tecnologias e etapas bem definidos.

Principais atividades:

- Levantamento de requisitos.
- Definição de escopo.
- Planejamento de funcionalidades.
- Seleção de tecnologias.
- Estruturação de arquitetura.
- Organização de tarefas.
- Identificação de dependências.
- Definição de etapas de desenvolvimento.

---

## 📚 Base de conhecimento

Além das skills, foi desenvolvida uma base de conhecimento para fornecer referências técnicas ao agente.

Os documentos foram organizados em `agent/knowledge/`.

| Arquivo | Descrição |
|---|---|
| `api-development.md` | Desenvolvimento, integração e documentação de APIs. |
| `clean-code.md` | Princípios de código limpo, legibilidade e manutenibilidade. |
| `c.md` | Fundamentos e boas práticas da linguagem C. |
| `c++.md` | Fundamentos e boas práticas da linguagem C++. |
| `databases.md` | Bancos de dados, modelagem, consultas e persistência. |
| `java.md` | Fundamentos e boas práticas da linguagem Java. |
| `javascript-typescript.md` | JavaScript, TypeScript e seus ecossistemas. |
| `programming-languages.md` | Conceitos e comparação de linguagens de programação. |
| `python.md` | Fundamentos e boas práticas da linguagem Python. |
| `secure-development.md` | Princípios e práticas de desenvolvimento seguro. |
| `security-basics.md` | Fundamentos de segurança da informação. |
| `software-architecture.md` | Arquitetura, padrões e organização de sistemas. |
| `software-engineering.md` | Processos e fundamentos da engenharia de software. |
| `testing-and-quality.md` | Estratégias de testes e garantia de qualidade. |

A base permite que o agente consulte conhecimentos específicos conforme a linguagem, tecnologia ou problema apresentado.

---

## 🏗️ Estrutura do projeto

```text
.
├── agent/
│   ├── knowledge/
│   │   ├── api-development.md
│   │   ├── clean-code.md
│   │   ├── c++.md
│   │   ├── c.md
│   │   ├── databases.md
│   │   ├── java.md
│   │   ├── javascript-typescript.md
│   │   ├── programming-languages.md
│   │   ├── python.md
│   │   ├── secure-development.md
│   │   ├── security-basics.md
│   │   ├── software-architecture.md
│   │   ├── software-engineering.md
│   │   └── testing-and-quality.md
│   └── persona.md
├── skills/
│   ├── project-planning/
│   │   ├── README.md
│   │   └── SKILL.md
│   ├── security-audit/
│   │   ├── README.md
│   │   └── SKILL.md
│   └── software-engineering/
│       ├── README.md
│       └── SKILL.md
├── AGENTS.md
└── README.md
```

## ⚙️ Arquivos de configuração

### AGENTS.md

Define as orientações gerais do agente, incluindo:

- Skills disponíveis e suas finalidades.
- Condições para utilização de cada skill.
- Referências à base de conhecimento.
- Fluxo de trabalho.
- Critérios de análise e avaliação de segurança.
- Diretrizes de desenvolvimento.
- Regras de autorização e responsabilidade.

### persona.md

Define a identidade e o comportamento do agente.

Estabelece sua postura como especialista técnico, incluindo comunicação, abordagem investigativa, relacionamento com o usuário e compromisso com a qualidade.

### SKILL.md

Cada especialização possui seu próprio arquivo de instruções.

Os arquivos orientam o agente sobre como conduzir cada atividade, quais etapas seguir e quais critérios considerar.

---

## 🚀 Como executar

O projeto utiliza o Hermes Agent como ambiente de execução.

### 1. Instalar o Hermes Agent

Siga as instruções oficiais de instalação:

https://github.com/NousResearch/hermes-agent

### 2. Obter o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre na pasta:

```bash
cd SEU-REPOSITORIO
```

### 3. Configurar o ambiente

Configure o Hermes Agent conforme a documentação oficial.

Verifique se o provedor de modelo está autenticado e funcionando.

### 4. Executar o agente

Com o terminal aberto na pasta do projeto, execute:

```bash
hermes
```

O agente deverá utilizar as instruções e especializações disponíveis no projeto, conforme o suporte do harness à estrutura de arquivos.

---

## 🧪 Exemplos de utilização

### Auditoria de segurança

Solicitação:

> Analise este código Python como um especialista em AppSec. Identifique possíveis vulnerabilidades, explique os riscos, classifique a severidade e recomende correções.

Resultado esperado:

- Identificação de possíveis vulnerabilidades.
- Explicação técnica.
- Avaliação de impacto e probabilidade.
- Classificação de severidade.
- Recomendações de correção.
- Sugestões de testes para validação.

### Desenvolvimento de software

Solicitação:

> Quero desenvolver uma API REST em Python. Ajude-me a definir uma estrutura organizada, aplicar boas práticas e implementar testes.

Resultado esperado:

- Avaliação dos requisitos.
- Sugestão de arquitetura.
- Organização de diretórios.
- Recomendações de tecnologias.
- Orientações de implementação.
- Estratégia de testes.

### Planejamento de projetos

Solicitação:

> Quero criar uma aplicação para organizar tarefas pessoais. Ajude-me a definir os requisitos, funcionalidades, tecnologias e etapas de desenvolvimento.

Resultado esperado:

- Levantamento de requisitos.
- Definição de funcionalidades.
- Sugestão de tecnologias.
- Planejamento da arquitetura.
- Organização das etapas.
- Identificação de prioridades.

---

## 🔐 Segurança e responsabilidade

As atividades de análise e testes de segurança devem ser realizadas somente em aplicações, sistemas e ambientes próprios ou com autorização explícita.

O agente deve priorizar:

- Análise defensiva.
- Identificação e correção de vulnerabilidades.
- Proteção de informações.
- Redução de riscos.
- Validação segura de correções.

Ações destrutivas ou irreversíveis devem exigir confirmação explícita.

---

## 🔮 Melhorias futuras

Este projeto representa a primeira etapa de uma proposta mais ampla.

A intenção é evoluir o agente para um assistente pessoal inspirado no conceito do Jarvis, ampliando suas capacidades além do desenvolvimento de software e da cibersegurança.

Entre as possibilidades futuras estão:

- Skill de assistente pessoal.
- Organização de tarefas e compromissos.
- Gerenciamento de projetos pessoais.
- Integração com ferramentas e serviços externos.
- Automação de atividades cotidianas.
- Gerenciamento de arquivos e informações.
- Assistência por voz.
- Interação com dispositivos e ambiente de trabalho.
- Memória persistente e personalização.

A ideia é aproveitar a arquitetura, as skills e os conhecimentos já desenvolvidos para construir um assistente cada vez mais completo e integrado.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como desafio final do:

**Santander Bootcamp — Cybersegurança: Do Zero à Prática**

A proposta consiste em especializar o agente utilizando skills, documentos de conhecimento e configurações de persona, transformando-o em uma ferramenta orientada à análise de vulnerabilidades e à correção de problemas de segurança.

O desenvolvimento também explora a aplicação desses conceitos em engenharia de software e planejamento de projetos.

---

## 👨‍💻 Autor

Desenvolvido como projeto de aprendizado e evolução prática nas áreas de:

- Cibersegurança.
- Desenvolvimento de software.
- Engenharia de software.
- Inteligência artificial.
- Automação.


