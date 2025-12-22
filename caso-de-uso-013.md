**Academia**  
**Especificação de Caso de Uso**  
**\[CDU013\] Fazer Login**

**Histórico da Revisão**

| Data | Versão | Descrição | Autor |
| ----- | ----- | ----- | ----- |
| 04/08/2025 | 1.0 | Adição das informações sobre cada item. | Maria Helena C. de Medeiros |

**1 Resumo**

O caso de uso Fazer Login permite que qualquer usuário cadastrado (Aluno, Instrutor ou Gestor) acesse o sistema após a validação de suas credenciais.

**2 Atores**

* Aluno  
* Instrutor  
* Gestor

**3 Pré-condições**

* O Usuário Ator (Aluno, Instrutor ou Gestor) deve ter um registro válido e suas credenciais (login/senha) na base de dados;  
* O sistema deve estar operacional e a tela de login deve estar acessível;  
* O sistema deve estar pronto para receber e processar as credenciais.

**4 Pós-condições** 

* O Usuário Ator está autenticado e é direcionado para a página inicial de seu respectivo perfil (Aluno, Instrutor ou Gestor);  
* Uma sessão de usuário válida é criada no sistema.

**5 Fluxos de evento**  
**5.1 Fluxo básico**

1. O Usuário Ator acessa a tela de login do sistema;  
2. O sistema exibe os campos de entrada (Login/E-mail e Senha);  
3. O Usuário Ator insere suas credenciais nos campos apropriados;  
4. O Usuário Ator aciona o botão "Entrar" ou equivalente;  
5. O sistema valida as credenciais informadas com os dados armazenados na base;  
6. O sistema verifica o perfil associado às credenciais válidas (Aluno, Instrutor ou Gestor);  
7. O sistema cria a sessão e direciona o usuário para a área principal do perfil detectado;  
8. O sistema exibe uma mensagem de boas-vindas ou a página inicial do perfil.

**5.2 Fluxo alternativo: Recuperação de Senha**

* Ocorre antes do Passo 3 do Fluxo Principal;  
* O Usuário Ator aciona o link "Esqueceu sua senha?";  
* O sistema solicita o e-mail ou nome de usuário para recuperação;  
* O Usuário Ator insere a informação e confirma;  
* O sistema envia um link ou código de redefinição para o e-mail cadastrado;  
* O sistema retorna para a tela de login.  
    
    
    
    
  


**5.3 Fluxo de exceção**  
	*E1: Credenciais Inválidas*

* Ocorre no Passo 5 do Fluxo Principal.  
* O sistema não encontra a combinação exata de login/e-mail e senha na base de dados.  
* O sistema interrompe o processamento de login.  
* O sistema exibe uma mensagem de erro.  
* O Usuário Ator retorna ao Passo 3 para tentar novamente.

	*E2: Usuário Inativo/Bloqueado*

* Ocorre no Passo 5 do Fluxo Principal, após a validação das credenciais;  
* O sistema detecta que as credenciais são válidas, mas o status do usuário está como "Inativo" ou "Bloqueado";  
* O sistema interrompe o processamento e exibe uma mensagem de erro;  
* O Usuário Ator é impedido de acessar e permanece na tela de login.

	*E3: Falha de Comunicação com a Base de Dados*

* Ocorre no Passo 5 do Fluxo Principal;  
* O sistema não consegue acessar ou se comunicar com o banco de dados para verificar as credenciais;  
* O sistema interrompe o processamento e exibe uma mensagem de erro técnico;  
* O Usuário Ator permanece na tela de login.
