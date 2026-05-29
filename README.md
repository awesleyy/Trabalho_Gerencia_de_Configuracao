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
* Uma das principais vantagens percebidas ao utilizar esse modelo é a capacidade da main estar sempre estável e pronta para produção. Além disso, as branchs separadas para depois dar merge na main conferem bastante organização para o projeto como um todo. Basicamente, o código que sobe para o GitHub sempre é revisado antes de ir para a main, pois são abertos Pull Requests que, posteriormente, vão para a main.
* Outra vantagem relevante é a facilidade do processo de codificação, pois falando sobre níveis de branchs, existem apenas dois. São eles: a main que segue ativa e estável e as branchs de segundo nível que logo mais vão parar na main. 

## 4. Dificuldades Encontradas
* As dificuldades encontradas no geral não foram de grande impacto, mais a nível de codificação e organização de pastas, além da padronização das branchs. O GitHub Flow é dinâmico e permite fácil entendimento  para projetos pequenos. Acreditamos que dificuldades seriam encontradas em cenários em que o desenvolvimento começasse a escalar. 

## 5. Problemas de Merge ou Conflitos
No início do projeto, a equipe passou por um processo de maturação no uso do Git, lidando diretamente com a resolução de conflitos. Foram registrados dois episódios de modificação simultânea em arquivos vazios: o primeiro no próprio README.md e o segundo no main.py, durante a criação das funções das classes. Em ambos os casos, a equipe resolveu os conflitos de forma rápida utilizando a estratégia de aceitar ambas as alterações (Accept Both Changes), integrando o trabalho dos membros de maneira colaborativa e sem perda de progresso.


## 6. Opinião do Grupo sobre a Estratégia
* Após analisarmos a dinâmica de desenvolvimento da equipe, identificamos que o GitHub Flow atende muito bem à nossa necessidade de simplicidade e agilidade, facilitando o entendimento de todo o time sobre o ciclo de entrega.

* No entanto, observamos dois pontos críticos que demandam evolução: a alta proliferação de branches desalinhadas (gerando desorganização no repositório) e a necessidade de implementar uma rotina de testes mais robusta para garantir a estabilidade da branch main