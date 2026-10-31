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
