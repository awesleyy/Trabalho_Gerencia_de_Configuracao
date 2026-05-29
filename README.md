# Estratégias de Branching e Merging

* **Disciplina:** Gerência de Configuração
* **Professor:** Dr. Rafael Will
* **Equipe (Grupo 5):** Levi, Henrique e André
* **Estratégia Sorteada:** GitHub Flow (Estratégia 2)

## 1. Estratégia Utilizada e Como Funciona

### Como a estratégia funciona?

De forma simplificada, se possui uma branch main principal onde ocorre deploys constantes, sendo o estado estável de produção

### Quais branches são utilizadas?

A cada correção ou funcionalidade se criar uma nova branch para desenvolvimento dela, a partir da main.

### Como ocorre o merge?

Se fazem alterações progressivas com commits atômicos até desenvolvimento estável da versão, abrindo um pull request para revisão e discussão. Quando se aprova, o pull request sobe diretamente na main, integrando aquela funcionalidade ou correção direto na prod.

### Vantagens do GitHub Flow
 * Fluxo simples e fácil.
 * Reduz conflitos devido a integração frequente.
 * Adequado em projetos que apresentam deploy contínuo.
 * Excelente integração com plataformas modernas.

### Desvantagens do GitHub Flow
 * Não é adequado para muitas versões de forma simultânea.
 * Exigência de testes automáticos confiáveis para verificação de bugs.
 * Requer disciplina e atenção para manter a "main" estável.

### Em quais tipos de projeto o GitHub Flow costuma ser utilizado
 * Equipes pequenas e médias.
 * Produtos Web e SaaS
 * Ambientes com integração frequente 

 # Relatório Prático: Estratégias de Branching e Merging



Este é o relato organizado da nossa discussão sobre a aplicação prática de controle de versão.


## 2. Organização do Fluxo de Trabalho
Começamos a desenvolver um pequeno sistema de loja de produtos, criando as classes `Cliente`, `Perfil`, `Carrinho`e `Produto`.

* Iniciamos com Levi e André documentando perguntas diferentes referente ao processo, em branchs diferentes para cada grupo de perguntas, mas no mesmo arquivo `README.md`, o que já causou o primeiro conflito mesmo em branches diferentes, para demonstrar uma dificuldade possível do modelo.
* Após isso, Levi desenvolveu uma "infraestrutura" para a solução, fazendo uma divisão macro de pastas e de principais arquivos que o sistema teria, o que causou um gargalo, com Henrique e André ficando dependentes dessa etapa para poder desenvolver.
* Só então, o fluxo foi padronizado e fluído:
    - Cada membro ficava responsável por criar uma branch - de nome padronizado - para cada feature, fix ou implementação que fosse de sua responsibilidade
    - Desenvolve-se, nessas branchs, pequenas funcionalidades e módulos em partes diferentes da infraestrutura do sistema, para qual cada um era responsável
    - Eram realizados commits atômicos e pontuais até conclusão daquela feature ou fix como um todo
    - Ao concluir, abria-se pull requests, corrigidos por outro integrante, solicitando o merge na main
    - Corrigia-se, quando existentes, os conflitos encontrados, e então o merge era aprovado e podia se desenvolver novas funcionalides


## 3. Principais Vantagens Percebidas
* Vantagem 1
* Vantagem 2

## 4. Dificuldades Encontradas
* Dificuldades

## 5. Problemas de Merge ou Conflitos
* Enfrentamos problemas de merge na classe principal no momento de unificar o código de todos (desenvolver melhor essa explicação)


## 6. Opinião do Grupo sobre a Estratégia
Nossa avaliação final é ...
