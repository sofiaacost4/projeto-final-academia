**Documento de Visão**

1. **Projeto**: Gym Time  
2. **Descrição do problema:** 

   Em uma academia é oferecida uma ampla variedade de modalidades esportivas, o que gera uma complexidade elevada na gestão operacional. A falta de um sistema centralizado dificulta a organização de horários e a alocação de instrutores, resultando frequentemente em conflitos de agenda, sobreposição de aulas em um mesmo espaço e falhas na comunicação de disponibilidade. Tal desorganização compromete a eficiência administrativa e impacta negativamente a experiência do aluno, tornando indispensável uma solução que automatize o gradeamento e garanta a harmonia entre as diversas atividades oferecidas.

3. **Solução:**

   O sistema gerenciará horários e atividades que centralizam o registro de todas as aulas e instrutores da academia. O software permitirá o cadastro das modalidades esportivas e a definição de turnos para cada professor, bloqueando automaticamente qualquer tentativa de marcar eventos que coincidam no mesmo horário ou local. Logo, funciona como uma ferramenta de controle para a administração, assegurando que a distribuição das aulas seja organizada e que não ocorram erros de planejamento que prejudiquem o atendimento aos alunos.

4. **Stakeholders e necessidades:**  
* **Alunos:** conseguir consultar os horários das aulas de forma fácil e ter a garantia de que, ao chegar na academia, o instrutor e a aula estarão disponíveis;  
* **Instrutores:** saber exatamente seus horários de trabalho, ter acesso à lista de alunos por aula e ser avisado com antecedência sobre qualquer mudança na grade;  
* **Administrador:** ter controle total sobre o uso do espaço, evitar prejuízos com salas vazias ou aulas canceladas por erro e visualizar a ocupação geral da academia.  
5. **Requisitos FUNCIONAIS:**  
   F01 \- **Cadastro de Modalidades/Esporte:** o sistema deve permitir o cadastro de diferentes esportes (ex: natação, musculação, yoga) com suas respectivas durações;  
   F02 \- **Gerenciamento de Instrutores:** permitir o registro de instrutores, associando-os às suas especialidades e disponibilidades de horário;  
   F03 \- **Alocação de Salas:** possibilitar a criação de uma grade fixa ou semanal de aulas, unindo modalidade, instrutor e local;  
   F04 \- **Bloqueio de Conflitos:** impedir salvar um registro caso o instrutor ou a sala já estejam ocupados no mesmo horário;  
   F05 \- **Consulta de Agenda:** o sistema deve disponibilizar uma visualização clara (para alunos e funcionários) de todos os horários e vagas disponíveis;  
   F06 \- **Reserva de vagas:** permitir que o aluno se inscreva em uma aula, respeitando o limite de vagas definido.  
6. **Requisitos NÃO-FUNCIONAIS:**  
   NF01 \- **Usabilidade:** possuir uma interface intuitiva, permitindo que alunos e instrutores realizem operações básicas sem a necessidade de “treinamento prévio”;  
   NF02 \- **Disponibilidade:** permanecer operacional sempre, garantindo o acesso às agendas tanto no horário de funcionamento da academia quanto remotamente pelos alunos;  
   NF03 \- **Desempenho:** a verificação de conflitos de horários e locais deve ser processada rapidamente;  
   NF04 \- **Segurança:** o acesso ao sistema deve ser controlado por perfis de usuário (Login e Senha), garantindo que apenas administradores possam alterar a grade de horários principal;  
   