## Caso de Uso 003: Cadastrar Aluno 

### 1. Resumo
O caso de uso **Cadastrar aluno** tem a finalidade de inserir novos registros (**alunos** ou **instrutores**) no sistema, armazenando seus dados principais para que possam acessar e utilizar as funcionalidades específicas de cada perfil.

---

### 2. Atores
* **Administrador**

---

### 3. Pré-condições
* O Usuário deve estar **logado** no sistema.
* O Usuário deve possuir as **permissões necessárias** para cadastrar novos usuários.
* O sistema deve estar **operacional** e a **base de dados acessível**.
* A opção de cadastro de usuário deve estar **disponível** e **selecionada** pelo ator.

---

### 4. Pós-condições
* Um novo registro de usuário (**aluno) é criado com sucesso e **persistido na base de dados**.
* O novo usuário recebe um **identificador único (ID)** e as **credenciais iniciais (login/senha)** são geradas/definidas.
* O novo usuário está associado ao **perfil correto** (aluno).
* O sistema retorna uma **mensagem de sucesso** ao Usuário.

---

### 5. Fluxos de Evento

#### 5.1 Fluxo Básico
1. O Usuário inicia a função de **cadastro de novo usuário**.
2. O sistema exibe o **formulário de cadastro**.
3. O Usuário **seleciona o tipo de perfil** (aluno).
4. O Usuário **preenche todos os campos obrigatórios: nome, email e senha**.
5. O Usuário **confirma o cadastro**.
6. O sistema **valida os dados**.
7. O sistema **cria o registro** e **persiste os dados na base**.
8. O sistema exibe a **mensagem de sucesso** e retorna à tela inicial de gestão de usuários.

#### 5.2 Fluxo Alternativo

##### A1: Dados Opcionais Preenchidos
* **Pós Passo 4** do Fluxo Principal: O Usuário preenche **campos opcionais: email e telefone**.
* Continua a partir do **Passo 5** do Fluxo Principal.

#### 5.3 Fluxo de Exceção

##### E1: Dados Inválidos ou Incompletos
* Ocorre no **Passo 6** do Fluxo Principal.
* O sistema detecta que um ou mais campos obrigatórios estão **vazios ou inválidos**.
* O sistema interrompe o processamento e exibe uma **mensagem de erro** indicando quais campos devem ser corrigidos.
* O Usuário corrige os dados e tenta novamente.

##### E2: Usuário Já Cadastrado
* Ocorre no **Passo 6** do Fluxo Principal.
* O sistema detecta que o **identificador único já existe na base de dados;  
* O sistema interrompe o processamento e exibe uma mensagem de erro informando que o usuário já está cadastrado;  
* O Usuário pode tentar cadastrar um usuário diferente ou cancelar a operação.

## Caso de Uso 013: Fazer Login

### 1. Resumo
O caso de uso **Fazer Login** permite que qualquer usuário cadastrado (**Aluno**, **Instrutor** ou **Administrador**) acesse o sistema após a validação de suas credenciais.

---

### 2. Atores
* **Aluno**
* **Instrutor**
* **Administrador**

---

### 3. Pré-condições
* O Usuário (Aluno, Instrutor ou Administrador) deve ter um **registro válido** e suas credenciais (**login/senha**) na base de dados.
* O sistema deve estar **operacional** e a **tela de login** deve estar acessível.
* O sistema deve estar pronto para **receber e processar** as credenciais.

---

### 4. Pós-condições
* O Usuário está **autenticado** e é direcionado para a **página inicial** de seu respectivo perfil (Aluno, Instrutor ou Administrador).
* Uma **sessão de usuário válida** é criada no sistema.

---

### 5. Fluxos de Evento

#### 5.1 Fluxo Básico
1. O Usuário acessa a **tela de login** do sistema.
2. O sistema exibe os **campos de entrada** (Login/E-mail e Senha).
3. O Usuário **insere suas credenciais** nos campos apropriados.
4. O Usuário aciona o botão **"Entrar"** ou equivalente.
5. O sistema **valida as credenciais** informadas com os dados armazenados na base.
6. O sistema **verifica o perfil** associado às credenciais válidas (Aluno, Instrutor ou Administrador).
7. O sistema **cria a sessão** e **direciona** o usuário para a área principal do perfil detectado.
8. O sistema exibe uma **mensagem de boas-vindas** ou a página inicial do perfil.

#### 5.3 Fluxo de Exceção

##### E1: Credenciais Inválidas
* Ocorre no **Passo 5** do Fluxo Principal.
* O sistema **não encontra a combinação exata** de login/e-mail e senha na base de dados.
* O sistema **interrompe o processamento** de login.
* O sistema exibe uma **mensagem de erro genérica** para evitar vazamento de informações.
* O Usuário retorna ao **Passo 3** para tentar novamente.

##### E2: Usuário Inativo/Bloqueado
* Ocorre no **Passo 5** do Fluxo Principal, **após a validação das credenciais**.
* O sistema detecta que as credenciais são válidas, mas o status do usuário está como **"Inativo" ou "Bloqueado"**.
* O sistema **interrompe o processamento** e exibe uma **mensagem de erro** específica para o bloqueio.
* O Usuário é **impedido de acessar** e permanece na tela de login.

##### E3: Falha de Comunicação com a Base de Dados
* Ocorre no **Passo 5** do Fluxo Principal.
* O sistema **não consegue acessar** ou se comunicar com o banco de dados para verificar as credenciais.
* O sistema **interrompe o processamento** e exibe uma **mensagem de erro técnico**.
* O Usuário **permanece na tela de login**.

## Caso de Uso 005: Cadastrar Esporte

### 1. Resumo
O caso de uso **Cadastrar Esporte** permite que um Instrutor ou Administrador adicione um novo módulo de conteúdo ou esporte a um curso existente no sistema.

---

### 2. Atores
* **Instrutor**
* **Administrador**

---

### 3. Pré-condições
* O Usuário (Instrutor ou Administrador) deve estar **logado** no sistema.
* O Usuário deve possuir as **permissões necessárias** para criar ou modificar cursos.
* O **Curso** ao qual o esporte será adicionado deve **existir** e estar cadastrado na base de dados.

---

### 4. Pós-condições
* Um novo registro de **Esporte** é criado e associado à **modalidade** especificada.
* O registro contém todos os **metadados** da aula.
* O sistema retorna uma **mensagem de sucesso** ao Usuário Ator.

---

### 5. Fluxos de Evento

#### 5.1 Fluxo Básico
1. O Usuário acessa a seção de **gestão de modalidades/cursos**.
2. O Usuário **seleciona a modalidade** desejada para adicionar o esporte.
3. O Usuário inicia a função **"Cadastrar Esporte"**.
4. O sistema exibe o **formulário de cadastro de esporte**.
5. O Usuário **preenche os campos obrigatórios** exigidos dentro da modalidade.
6. O Usuário faz o **upload do material** da aula ou insere o **link** para o conteúdo.
7. O Usuário **confirma o cadastro**.
8. O sistema **valida os dados**.
9. O sistema **cria o registro do esporte** e a associa à modalidade na base de dados.
10. O sistema exibe a **mensagem de sucesso** e retorna à visão geral da modalidade.

#### 5.2 Fluxo Alternativo

##### A1: Conteúdo Opcional/Adicional
* Ocorre **após o Passo 6** do Fluxo Principal.
* O Usuário **adiciona conteúdo extra** (Ex: material de apoio, slides).
* Continua no **Passo 7** do Fluxo Principal.

##### A2: Pré-requisitos para a Aula
* Ocorre **após o Passo 5** do Fluxo Principal.
* O Usuário define **pré-requisitos** para este esporte (Ex: "O aluno deve ter concluído o Esporte 3").
* Continua no **Passo 6** do Fluxo Principal. (O sistema armazena o requisito de conclusão).

#### 5.3 Fluxo de Exceção

##### E1: Dados Inválidos ou Incompletos
* Ocorre no **Passo 8** do Fluxo Principal.
* O sistema detecta que um ou mais campos obrigatórios estão **vazios ou inválidos**.
* O sistema interrompe o processamento e exibe uma **mensagem de erro** indicando quais campos devem ser corrigidos.
* O Usuário Ator corrige os dados e tenta novamente (retorna ao **Passo 7**).

##### E2: Modalidade Não Encontrada/Inexistente
* Ocorre no **Passo 2** do Fluxo Principal.
* A modalidade selecionada pelo Usuário Ator **não existe** ou foi removida da base de dados.
* O sistema exibe uma **mensagem de erro** e impede o prosseguimento do cadastro da aula.
* O Usuário Ator seleciona outra modalidade ou cancela a operação.

##### E3: Falha no Upload do Conteúdo
* Ocorre no **Passo 7** do Fluxo Principal (durante o processamento do upload).
* O sistema **não consegue processar ou armazenar** o arquivo de conteúdo (Ex: limite de tamanho excedido, erro de rede).
* O sistema interrompe o processamento e exibe uma **mensagem de erro específica** sobre a falha do upload.
* O Usuário é solicitado a tentar novamente com o mesmo ou outro arquivo/link.
