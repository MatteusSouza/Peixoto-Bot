[Inglês](/README.md) | Português

## Como rodar o Bot

Versão testada: Python 3.9

> Eu recomendo fortemente que crie um ambiente de virtualização antes de instalar pacotes.

[Ir para instalação do pacote.](#como-instalar-os-pacotes)

## Como criar um ambiente de virtualização Python

Caso utilize Windows, para evitar erros com o Windows PowerShell siga [**esses passos**](#caso-esteja-esteja-utilizando-windows) antes de prosseguir.

Verifique se o pip está atualizado e instale o virtualenv

```powershell
python -m pip install --upgrade pip
pip3 install virtualenv
```

Certifique-se de que está na pasta raiz do projeto para utilizar os comandos abaixo

Use o comando abaixo para criar uma virtualenv com o nome venv ou outro de sua preferencia.

```powershell
virtualenv nome_da_virtualenv
```

Ative a virtualenv que acabou de criar com o comando

```powershell
.\nome_da_virtualenv\Scripts\activate
```

O nome que você deu a virtualenv aparece na frente do caminho dessa forma.

![image_venv](/images/image_venv.jpg)

[Instale os pacotes](#como-instalar-os-pacotes)

---

<br><br>
## Como instalar os pacotes

Instale os pacotes com o comando `pip install -r requirements.txt`

---
<br><br>
## Caso esteja esteja utilizando Windows.

O PowerShell trabalha com um esquema de autorizações (conhecido como `Execution Policy`) para execução de scripts

Na hora de tentar abrir a virtualenv via PowerShell executando o script `.\nome_da_virtualenv\Scripts\activate` pode apresentar um erro [sobre políticas de execução](https://docs.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1), para evitar erros, siga as instruções.

Para verificar a politica de execução, abra o PowerShell como administrador e execute o seguinte comando:

```powershell
Get-ExecutionPolicy
```

Caso ele retorne `Restricted`, execute o comando:

```powershell
Set-ExecutionPolicy RemoteSigned
```

E escolha a opção `[A] Sim para Todos`

Caso o comando acima apresente erro, tente usar:

`Set-ExecutionPolicy Bypass -Scope Process`

Verifique se alteração de permissão ocorreu com sucesso executando novamente o comando:

```bash
Get-ExecutionPolicy
```

Alterada a permissão, [pode prosseguir](#como-criar-um-ambiente-de-virtualização-python).

---

<br><br>

Altere sua api_key dentro dapasta raiz do projeto antes de rodar.

Ou crie um arquivo config.py como no exemplo abaixo

![image_venv](/images/image_token.png)