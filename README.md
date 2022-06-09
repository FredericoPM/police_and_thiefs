# police_and_thiefs
 Algoritmo para resolver o problema polícia ladrão. Dado um array de tamanho N em que cada elemento é polícia ou ladrão. O problema possui as seguintes especificações:
    
    - Cada policial pode capturar apenas um ladrão;
    - Um policial não pode capturar um ladrão com distância superior a “k”
Para solucionar o problema foi adotada uma estratégia gulosa, na qual é calculado quantos ladrões são alcançáveis por cada policial e de quantos policiais um ladrão está no alcance. Feito isso os policiais com o menor número de ladrões alcançáveis selecionam o ladrão ao seu alcance que é selecionável pelo menor número de policiais.