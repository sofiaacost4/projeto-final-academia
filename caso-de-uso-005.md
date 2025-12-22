**Academia**  
**Especificação de Caso de Uso**  
**\[CDU005\] Cadastrar Aula**  
**Histórico da Revisão**

| Data | Versão | Descrição | Autor |
| ----- | ----- | ----- | ----- |
| 04/08/2025 | 1.0 | Adição das informações sobre cada item. | Maria Helena C. de Medeiros |

**1 Resumo**

O caso de uso Cadastrar Aula permite que um Instrutor ou Administrador adicione um novo módulo de conteúdo ou aula a um curso existente no sistema.

**Ator**

* Gestor

**3 Pré-condições**

* O Usuário Ator (Instrutor ou Gestor) deve estar logado no sistema.  
* O Usuário Ator deve possuir as permissões necessárias para criar ou modificar cursos.  
* O Curso ao qual a aula será adicionada deve existir e estar cadastrado na base de dados.

**4 Pós-condições** 

* Um novo registro de Aula é criado e associado à modalidade especificada.  
* O registro contém todos os metadados da aula.  
* O sistema retorna uma mensagem de sucesso ao Usuário Ator.

**5 Fluxos de evento**  
**5.1 Fluxo básico (gestor)**

1. O Usuário Ator acessa a função de "Cadastrar Aula".  
2. O sistema exibe o formulário de cadastro de aula.  
3. O Usuário Ator seleciona a modalidade desejada para adicionar a aula.  
4. O Usuário Ator preenche os campos obrigatórios exigidos do formulário.  
5. O Usuário Ator confirma o cadastro.  
6. O sistema valida os dados.  
8. O sistema cria o registro da aula e a associa à modalidade na base de dados.  
9. O sistema exibe a mensagem de sucesso e retorna à visão geral da aula.

**5.2 Fluxo alternativo:**   
	*A1: Conteúdo Opcional/Adicional*

* Ocorre após o Passo 4 do Fluxo Principal.  
* O Usuário Ator adiciona conteúdo extra.  
* Continua no Passo 5 do Fluxo Principal.

	*A2: Pré-requisitos para a Aula*

* Ocorre após o Passo 4 do Fluxo Principal.  
* O Usuário Ator define pré-requisitos para esta aula (Ex: "O aluno deve ter concluído a Aula 3").  
* Continua no Passo 5 do Fluxo Principal. (O sistema armazena o requisito de conclusão).

**5.3 Fluxo de exceção**  
*E1: Dados inválidos ou incompletos*

* Ocorre no Passo 8 do Fluxo Principal.  
* O sistema detecta que um ou mais campos obrigatórios estão vazios ou inválidos .  
* O sistema interrompe o processamento e exibe uma mensagem de erro indicando quais campos devem ser corrigidos.  
* O Usuário Ator corrige os dados e tenta novamente (retorna ao Passo 7).

	*E2: Modalidade Não Encontrada/Inexistente*

* Ocorre no Passo 2 do Fluxo Principal.  
* A modalidade selecionada pelo Usuário Ator não existe ou foi removida da base de dados.  
* O sistema exibe uma mensagem de erro e impede o prosseguimento do cadastro da aula.  
* O Usuário Ator seleciona outra modalidade ou cancela a operação.
