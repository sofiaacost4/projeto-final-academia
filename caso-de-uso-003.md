**Academia**  
**Especificação de Caso de Uso**  
**\[CDU003\] Cadastrar Aluno**

**1 Resumo**

O caso de uso Cadastrar aluno tem a finalidade de inserir novos registros (alunos) no sistema, armazenando seus dados principais para que possam acessar e utilizar as funcionalidades específicas de cada perfil.

**2 Atores**

* Gestor

**3 Pré-condições**

* O Usuário deve estar logado no sistema;  
* O Usuário deve possuir as permissões necessárias para cadastrar novos usuários;  
* O sistema deve estar operacional e a base de dados acessível;  
* A opção de cadastro de usuário deve estar disponível e selecionada pelo ator.

**4 Pós-condições** 

* Um novo registro de usuário é criado com sucesso e persistido na base de dados;  
* O novo usuário recebe um identificador único (ID) e as credenciais iniciais (login/senha) são geradas/definidas;  
* O novo usuário está associado ao perfil correto (aluno ou instrutor);  
* O sistema retorna uma mensagem de sucesso ao Usuário.

**5 Fluxos de evento**  
**5.1 Fluxo básico**

1. O Usuário seleciona o tipo de perfil a ser cadastrado (aluno);  
2. O Usuário inicia a função de cadastro de novo usuário;  
3. O sistema exibe o formulário de cadastro;  
4. O Usuário preenche todos os campos obrigatórios (nome, email e senha);  
5. O Usuário confirma o cadastro;  
6. O sistema valida os dados;  
7. O sistema cria o registro e persiste os dados na base;  
8. O sistema exibe a mensagem de sucesso e retorna à tela de cadastro de novo usuário.

**5.2 Fluxo alternativo (gestor)**  
	*A1: Dados Opcionais Preenchidos*

* Pós Passo 4 do Fluxo Principal;  
* O Usuário preenche campos opcionais;  
* Continua a partir do Passo 5 do Fluxo Principal.

**5.3 Fluxo de exceção**  
	*E1: Dados Inválidos ou Incompletos*

* Ocorre no Passo 6 do Fluxo Principal;  
* O sistema detecta que um ou mais campos obrigatórios estão vazios ou inválidos;  
* O sistema interrompe o processamento e exibe uma mensagem de erro indicando quais campos devem ser corrigidos;  
* O Usuário corrige os dados e tenta novamente.

	*E2: Usuário Já Cadastrado*

* Ocorre no Passo 6 do Fluxo Principal;  
* O sistema detecta que o identificador único já existe na base de dados;  
* O sistema interrompe o processamento e exibe uma mensagem de erro informando que o usuário já está cadastrado;  
* O Usuário pode tentar cadastrar um usuário diferente ou cancelar a operação.
