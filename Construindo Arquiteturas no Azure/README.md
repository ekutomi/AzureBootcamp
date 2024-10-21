# Microsoft Data Centers - Geografia e Mapa do Planeta

## Geografia e Mapa do Planeta
O [site oficial dos Data Centers da Microsoft](https://datacenters.microsoft.com/globe/explore) oferece uma visão interativa dos locais de data centers distribuídos globalmente. A plataforma permite explorar a geografia dos centros, identificando as diversas regiões ao redor do mundo onde a Microsoft opera seus data centers, garantindo alta disponibilidade e baixa latência de seus serviços.

## Dados Sensíveis e Regiões
Os dados sensíveis são tratados com prioridade em todas as regiões, com políticas rigorosas de privacidade e segurança, garantindo conformidade com leis locais, como GDPR na Europa. As regiões são planejadas para permitir redundância e recuperação de desastres, com segmentação para evitar falhas generalizadas.

## Centro de Operações
O Centro de Operações da Microsoft é responsável pela monitoração e manutenção dos data centers em tempo real. A equipe trabalha 24/7 para garantir que os serviços sejam fornecidos com o mínimo de interrupção, gerenciando energia, refrigeração, e segurança física.

## Visualizar Imagens e Sala de Servidores
A plataforma também permite visualizar imagens dos data centers, incluindo salas de servidores. Essas imagens oferecem uma visão detalhada da infraestrutura física utilizada para manter os serviços online, como racks de servidores, sistemas de refrigeração e controles de segurança.

Explore mais em [datacenters.microsoft.com/globe/explore](https://datacenters.microsoft.com/globe/explore).

## LGDP
Caso deseje que seus dados estejam disponíveis somente no Brasil, entre em contato com a Microsoft.

# Criando grupos de recursos

## 1. Criação de Grupo de Recursos
Para criar um grupo de recursos no Azure:
1. Acesse o portal do Azure.
2. No menu de navegação, selecione **Grupos de Recursos**.
3. Clique em **Adicionar**.
4. Defina o **Nome do Grupo de Recursos** e selecione a **Região**.
5. Clique em **Revisar + Criar** e, em seguida, **Criar**.

## 2. Bloqueios
Para adicionar bloqueios a um recurso ou grupo de recursos:
1. Acesse o **Grupo de Recursos** ou **Recurso**.
2. Selecione **Configurações** > **Bloqueios**.
3. Escolha entre os tipos de bloqueio:
   - **Read-only**: Impede alterações, mas permite leitura.
   - **Delete**: Impede a exclusão.
4. Clique em **Adicionar**, nomeie o bloqueio e salve.

## 3. Criação de uma Rede Virtual (VNet)
Para criar uma VNet:
1. No portal do Azure, vá até **Redes Virtuais** e selecione **Criar**.
2. Defina o **Nome da VNet**, **Espaço de Endereçamento**, e a **Região**.
3. Configure as **Sub-redes** e os **Grupos de Segurança de Rede** (NSG).
4. Clique em **Revisar + Criar** e, depois, **Criar** para provisionar a VNet.
5. Acesse a VNet criada para configurar outras opções, como gateways de VPN ou peering entre VNets.



