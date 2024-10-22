# Como escalar uma aplicação (Virtual Machine) no Azure

## Opções de Escalabilidade

### 1. Escalabilidade Vertical (Vertical Scaling)
A escalabilidade vertical aumenta a capacidade de uma única Virtual Machine (VM) ajustando seus recursos (CPU, memória, armazenamento). 
#### Passos para escalar verticalmente:
- **Passo 1:** No **Azure Portal**, vá até a VM que você deseja escalar.
- **Passo 2:** Na página de detalhes da VM, selecione **Tamanho (Size)**.
- **Passo 3:** Escolha um tamanho de VM superior que atenda às suas novas necessidades de capacidade.
- **Passo 4:** Confirme a alteração. A VM será reiniciada para aplicar a nova configuração.

**Observação:** A escalabilidade vertical exige a reinicialização da VM, o que pode causar um breve tempo de inatividade.

### 2. Escalabilidade Horizontal (Horizontal Scaling)
A escalabilidade horizontal envolve a adição de múltiplas instâncias de VMs para distribuir a carga de trabalho entre elas. Isso é feito por meio de **Azure Virtual Machine Scale Sets (VMSS)**, que gerenciam automaticamente o número de VMs baseadas em regras de escalonamento definidas.

#### Passos para configurar um Virtual Machine Scale Set (VMSS):
- **Passo 1:** No **Azure Portal**, selecione **Criar um recurso** e escolha **Virtual Machine Scale Set**.
- **Passo 2:** Defina as propriedades iniciais da instância, como o sistema operacional e o tamanho da VM.
- **Passo 3:** Na guia **Escalabilidade (Scaling)**, configure as opções de escalabilidade, como o número inicial de VMs.
- **Passo 4:** Habilite o **Autoescalonamento (Autoscale)** para ajustar automaticamente o número de instâncias com base em métricas.
- **Passo 5:** Configure as regras de escalonamento com base em:
  - **CPU:** Defina um percentual de uso da CPU para iniciar o escalonamento.
  - **Memória:** Escale com base no uso da memória.
  - **Métricas customizadas:** Baseie o escalonamento em métricas personalizadas ou sinais de saúde da aplicação.

### 3. Autoescalonamento (Autoscale)
O Autoescalonamento permite adicionar ou remover VMs automaticamente com base nas condições de uso definidas. Funciona em conjunto com o **VM Scale Sets** e as métricas de monitoramento do Azure.
#### Configurando o Autoescalonamento:
- **Passo 1:** No recurso do **VM Scale Set**, selecione **Autoescala**.
- **Passo 2:** Defina **Condições de Escalonamento**, por exemplo:
  - **Subir o número de instâncias** quando a CPU estiver acima de 70%.
  - **Descer o número de instâncias** quando a CPU estiver abaixo de 30%.
- **Passo 3:** Defina o intervalo de tempo em que o sistema verifica as métricas para determinar se precisa ajustar o número de instâncias.

### 4. Escalonamento Manual (Manual Scaling)
Essa opção permite ao administrador ajustar o número de VMs de forma manual, sem depender de regras automáticas.

#### Como fazer escalonamento manual:
- **Passo 1:** Acesse o **VM Scale Set** no Azure Portal.
- **Passo 2:** Vá até a opção **Configurações de Escala**.
- **Passo 3:** Defina o número de instâncias manualmente e confirme.

### 5. Zonas de Disponibilidade (Availability Zones)
Ao criar ou escalar uma VM, você pode distribuí-la em **Zonas de Disponibilidade** para garantir maior redundância e tolerância a falhas. Isso permite que as VMs estejam espalhadas entre diferentes zonas físicas dentro de uma região do Azure.
- **Configuração:** Ao criar o **VM Scale Set**, defina a distribuição das instâncias entre diferentes Zonas de Disponibilidade.

## Considerações
- **Vertical Scaling** é limitado ao hardware disponível para uma única VM e envolve tempo de inatividade.
- **Horizontal Scaling** com **VM Scale Sets** oferece mais flexibilidade e resiliência, com escalonamento automático baseado em demanda.
- O uso de **Zonas de Disponibilidade** melhora a tolerância a falhas.
- O disco parado resulta em custo. Escolher a opção **excluir VM** reduzirá os custos incorridos.
- **Excluir o IP público e a NIC quando a VM for excluída** também economizará recursos e tornará a administração de nossa rede mais limpa.