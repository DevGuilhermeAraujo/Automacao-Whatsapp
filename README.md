🎉 Automação de Envio de Mensagens para Clientes com Python 🚀

Desenvolvi uma automação simples e eficaz para enviar mensagens personalizadas aos clientes via WhatsApp, utilizando o poder do Python! 🤖📱

🔧 Como Funciona?

Esta automação parte de uma planilha Excel (clientes.xlsx), que contém dados importantes dos clientes, como nome, telefone e validade de pagamento. A partir dessas informações, o script envia automaticamente uma mensagem para cada cliente, incluindo um link para pagamento e informando a data limite para pagamento sem juros.

🛠️ Tecnologias e Bibliotecas Utilizadas

Para construir essa automação, utilizei as seguintes bibliotecas Python:

openpyxl: Para integrar o Python com planilhas Excel.

quote: Para formatar corretamente as mensagens que serão enviadas pelo WhatsApp.

webbrowser: Para abrir o WhatsApp Web no navegador padrão do computador.

sleep: Para inserir intervalos entre as operações, garantindo a execução correta da automação.

pyautogui: Para simular movimentos e cliques no navegador, como se fosse um humano interagindo.

pillow: Para manipulação de imagens, utilizada para trabalhar com a imagem da seta do WhatsApp.

📝 O que é Necessário para Rodar a Automação?

Planilha Excel: A planilha clientes.xlsx deve estar na mesma pasta que o arquivo app.py. Caso deseje usar outro nome para a planilha, é preciso alterar o nome no código.

WhatsApp Vinculado ao Navegador: Certifique-se de que o WhatsApp Web esteja vinculado ao navegador padrão do computador.

Planilha Preenchida: Todos os dados dos clientes devem estar devidamente preenchidos na planilha para que a automação funcione corretamente.

🚀 Possibilidades de Expansão

A automação é flexível e permite a adição de mais dados na planilha, caso seja necessário enviar informações adicionais aos clientes.

🌟 Vantagens

Agilidade: Mensagens enviadas em massa, economizando tempo.

Personalização: Cada cliente recebe uma mensagem personalizada com suas informações.

Integração Simples: Basta ajustar a planilha e rodar o script!

Estou empolgado com as possibilidades que essa automação oferece e com os ganhos de produtividade que ela pode proporcionar. Se você se interessa por automações em Python ou precisa de uma solução semelhante, vamos conversar!
