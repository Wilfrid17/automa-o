Automação de Cadastro com PyAutoGUI

Este projeto utiliza o PyAutoGUI para automatizar o processo de cadastro de usuários em uma plataforma web. A automação abre o navegador, acessa um site específico, realiza login e preenche formulários com dados provenientes de um arquivo CSV.

Funcionalidades

Abertura automática do navegador Chrome

Login automatizado na plataforma

Leitura de dados de um arquivo CSV utilizando pandas

Preenchimento automático de formulários com informações de usuários

Como funciona

O script abre o navegador Chrome e acessa a URL: Link da plataforma.

Realiza login com usuário e senha pré-definidos.

Lê os dados do arquivo alunos.csv e preenche o formulário com nome, email, endereço e telefone.

Submete o formulário e repete o processo para cada linha do CSV.

Pré-requisitos

Python 3.x

Bibliotecas: PyAutoGUI, pandas

Arquivo CSV com as informações dos usuários
