# Delivery Fast (em desenvolvimento...)

![DELIVERY](/delivery_ml.png)


## 1. Problema de Negócio

<p> A Delivery Fast é uma empresa que tem como foco levar o alimento do restaurante para a casa do clinete no menor tempo possível. Portanto, o objetivo desse projeto é a construção de um modelo capaz de prever o tempo de entrega que é mostrada ao cliente </p>

<p>É de suma importância que essa predição seja a mais precisa possível para que a experiência do clinete seja agradável e conseuqentemente aumentar o nível de satisfação do mesmo.</p>

## 2. Lista de Atributos

| Atributos  |  Descrição |
| ------------------- | ------------------- |
|  market_id |  A cidade/região na qual a empresa atua |
|  created_at |  Data e Tempo quando o pedido foi realizado pelo cliente |
|  actual_delivery_time |  Data e Tempo de quando o pedido foi entregue ao cliente |
|  store_id |  Id que representa o restaurante que o pedido foi realizado |
|  store_primary_category |  Categoria do Restaurante |
|  order_protocol |  Um restaurante podereceber pedidos da empresa de vários modos |
|  total_items |  Total de Itens do Pedido |
|  subtotal |  Valor total do pedido (em centavos) |
|  num_distinct_items |  Número distintos de itens no pedido |
|  min_item_price |  Preço do item com menor custo no pedido (em centavos); |
|  max_item_price |  Preço do item com maior custo no pedido (em centavos); |
|  total_onshift_dashers |  Número de entregadores disponíveis que estão a até 16 quilômetros do restaurante no momento da criação do pedido; |
|  total_busy_dashers |  Subconjunto dos total_onshift_dashers acima que estão atualmente trabalhando em um pedido; |
|  total_outstanding_orders |  Número de pedidos em um raio de 10 milhas deste pedido que estão sendo processados atualmente; |
|  estimated_order_place_duration |  Tempo estimado para o restaurante receber o pedido da Delivery Fast (em segundos); |
|  estimated_store_to_consumer_driving_duration |  Tempo estimado de viagem entre o restaurante e o consumidor (em segundos); |

## 3. Estratégia de Solução

![CRISP](/crisp_metodo.png)

***Minha estratégia para resolver esse desafio foi:***

**Step 01. Data Description:**  O objetivo é utilizar métricas estatísticas para identificar outliers no escopo do negócio.

**Step 02. Feature Engineering:** Derivar novos atributos com base nas variáveis originais para descrever melhor o fenômeno a ser modelado.

**Step 03. Data Filtering:** Filtrar as linhas e selecionar as colunas que não contenham informações para modelagem ou não correspondam ao escopo do negócio.

**Step 04. Exploratory Data Analysis:** Explorar os dados para encontrar insights e entender melhor o impacto das variáveis no aprendizado do modelo.

**Step 05. Data Preparation:** Preparar os dados para que os modelos de aprendizado de máquina possam aprender um comportamento específico.

**Step 06. Feature Selection:** Seleção dos atributos mais significativos para treinar o modelo.

**Step 07. Machine Learning Modelling:** Treinamento do modelo de aprendizado de máquina.

**Step 08. Hyperparameter Fine Tunning:** Escolher os melhores valores para cada um dos parâmetros do modelo selecionado na etapa anterior.

**Step 09. MLFlow Monitoring:** Utilizar a ferramenta MLFlow para monitorar todo pipeline de desenvolvimento de machine learning.

## 4. Modelos de Machine Learning Aplicados

## 5. Performance do Modelo de Machine Learning

## 6. Resultados de Negócio (Projeto ainda em desenvolvimento...)



