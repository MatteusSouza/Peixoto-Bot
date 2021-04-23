English | [Portuguese](README_ptbr.md)

## How to run the bot?

Tested version: Python 3.9

> I highly recommend creating a Python virtualization environment before installing packages.

[Go to package installation](#how-to-install-the-packages)

## How to create a python virtualization environment

If you use Windows to avoid errors with Windows PowerShell, follow [these steps](#if-you-are-using-windows.) before proceeding.

Check that the pip is up to date and install virtualenv

```powershell
python -m pip install --upgrade pip
pip3 install virtualenv
```

Make sure you are in the project's root folder to use the commands below

Use the command below to create a virtualenv with the name "venv" or another of your choice.

```powershell
virtualenv name_of_virtualenv
```

Activate the virtualenv you just created with this command

```powershell
.\\name_of_virtualenv\\Scripts\\activate
```

The name you chose for virtualenv appears before the path, like this.

![image_venv](/images/image_venv.jpg)

[Install the packages](#how-to-install-the-packages)

---

<br><br>
## How to install the packages

Use the command `pip install -r requirements.txt`

---
<br><br>
## If you are using Windows.

PowerShell works with an authorization feature (known as `Execution Policy`) for running scripts

When trying to open virtualenv with PowerShell by running the script `.\\name_of_virtualenv\\Scripts\\activate` may present an error [about the execution policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1), to avoid errors follow the instructions

To check the execution policy, open PowerShell as an administrator and run the following command:

```powershell
Get-ExecutionPolicy
```

If it returns `Restricted`, run the command:

```powershell
Set-ExecutionPolicy RemoteSigned
```

And choose the option `[A] Yes to All`

If the above command has an error, try using:

`Set-ExecutionPolicy Bypass -Scope Process`

Verify that the permission change has occurred successfully by running the command again:

```bash
Get-ExecutionPolicy
```

With the permission changed, [you can proceed](#how-to-create-a-python-virtualization-environment).

---

<br><br>

Change your api_key within the project before running.

Or create a `config.py` file like the example below 

![image_venv](/images/image_token.png)