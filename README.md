# Trabalho_Gerencia_de_Configuracao

# Etapa 1 - GitHub Flow

## Como a estratégia funciona?

De forma simplificada, se possui uma branch main principal onde ocorre deploys constantes, sendo o estado estável de produção

## Quais branches são utilizadas?

A cada correção ou funcionalidade se criar uma nova branch para desenvolvimento dela, a partir da main.

## Como ocorre o merge?

Se fazem alterações progressivas com commits atômicos até desenvolvimento estável da versão, abrindo um pull request para revisão e discussão. Quando se aprova, o pull request sobe diretamente na main, integrando aquela funcionalidade ou correção direto na prod.

## Vantagens do GitHub Flow
 * Fluxo simples e fácil.
 * Reduz conflitos devido a integração frequente.
 * Adequado em projetos que apresentam deploy contínuo.
 * Excelente integração com plataformas modernas.

## Desvantagens do GitHub Flow
 * Não é adequado para muitas versões de forma simultânea.
 * Exigência de testes automáticos confiáveis para verificação de bugs.
 * Requer disciplina e atenção para manter a "main" estável.

## Em quais tipos de projeto o GitHub Flow costuma ser utilizado
 * Equipes pequenas e médias.
 * Produtos Web e SaaS
 * Ambientes com integração frequente 