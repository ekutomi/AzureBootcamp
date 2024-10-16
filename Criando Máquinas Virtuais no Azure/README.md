# SLAs

A instrutora começou falando de SLAs, ou acordos de nível de serviço. Esse é um termo no qual o Azure se compromete a cumprir uma medida de disponibilidade. Em caso de falhas, compensações serão dadas, ou em outras palavras, o Azure vai te pagar parte do valor de volta.

## Como funciona?

O Azure diz que cumprirá uma percentagem de disponibilidade. Ela pode ser tanto **99%** como **99,9%** ou até mesmo **99,99%**. Quanto melhor a disponibilidade, mais caro. Essa disponibilidade pode se aplicar a BDs, VMs, ou até mesmo funções. O tempo é calculado como mensal, o que é uma medida justa. Se fosse diárias seria muito puxada. Se fosse anual, muito frouxa.

Abaixo uma tabelinha com os tempos de indisponibilidade máxima por SLA:

| Percentual de SLA | Tempo máximo de inatividade por mês |
|-------------------|------------------------------------|
| 99,99%            | ~4,38 minutos                     |
| 99,95%            | ~21,56 minutos                    |
| 99,9%             | ~43,83 minutos                    |

## Link

As informações estão disponíveis na [SLA do Azure](https://azure.microsoft.com/pt-br/support/legal/sla/).


# Como Criar uma Máquina Virtual (VM) no Azure

## Passo a passo

- Realize um login no [Azure](https://portal.azure.com).
- No painel principal, clique em **"Criar um recurso"**.
- Na pesquisa, digite **"Máquina Virtual"** e selecione a opção **"Máquina Virtual (Azure Compute)"**.
- Configure sua VM, escolhendo assinatura, grupo de recursos, região, imagem docker, tamanho e recursos, etc...
- Selecione como acessará, se por senha ou chave SSH.
- Escolha o tipo de espaço em disco.
- Escolha o tipo de rede.
- Confirme.

## Acessando a VM

A instrutora também falou de como acessar a VM.

- **Windows**: via RDP (Remote Desktop Protocol).
- **Linux**: via SSH