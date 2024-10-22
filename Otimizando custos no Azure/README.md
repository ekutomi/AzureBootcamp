# Custos

## Calculadora do TCO
- Uma ferramenta de comparação de custos, vendo migração de recursos.
- Caso você opte por um servidor, terá custos de manutenção de servidores, perda de valor de capitais, energia e resfriamento, e mão de obra de operação. A longo prazo esse custo, em minha experiência, é melhor e mais barato que o Azure e AWS. Mas o custo de entrada é alto e custoso.
- Cada custo depende de recurso usado, tier do recurso, configurações, regiões, etc... por exemplo, cada BD pode ter um custo diferente. Uma BD com alto espaço de disco será mais cara que uma com pouco espaço. Elementos com baxio SLA são mais baratos. Baixa replicação também...

## Calculadora de Preços
- Cada coisa tem seu custo, embora algumas tenham um tier grátis, como Azure Functions...
- Na calculadora está em dólares, mas no portal Azure ele aparece em BRL (reais) para mim
- Planos de economia (se comprometer a um tempo maior) pode trazer economia, mas meio que te prende a uma solução... então é bom paraquem sabe que continuará utilizando o Azure.
- Os custos operacionais do Azure tornam os custos de uma startup, por exemplo, mais caras para se manter... é bom para começar, mas logo o preço se aplica ao cliente final... É importante sabermos economizar o máximo possível.
- Estruturas híbridas são ideiais... você usa o máximo de seus servidores, e o que vier a mais eventualmente você usa a nuvem.
- Budget e Threshold: podemos estabelecer nossos limites, colocar limites, alertas, para nos apoiar em nosso controle. 