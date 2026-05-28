# Etapa 1 - GitHub Flow

## Como a estratégia funciona?

De forma simplificada, se possui uma branch main principal onde ocorre deploys constantes, sendo o estado estável de produção

## Quais branches são utilizadas?

A cada correção ou funcionalidade se criar uma nova branch para desenvolvimento dela, a partir da main.

## Como ocorre o merge?

Se fazem alterações progressivas com commits atômicos até desenvolvimento estável da versão, abrindo um pull request para revisão e discussão. Quando se aprova, o pull request sobe diretamente na main, integrando aquela funcionalidade ou correção direto na prod.