# Gambling

## Instruções iniciais
Antes de começarmos, certifique-se que tenha instalado o **python** e **virtualenv**. Abra o Terminal e crie uma virtualenv chamada **env**.
Caso Windows:
<pre>
virtualenv env
 . env env/Script/activate
</pre>
Caso Linux:
<pre>
virtualenv env
 . env env/bin/activate
</pre>
E um iniciar o projeto:
<pre>
python start_windows.py
# python start_linux.py
</pre>

## 1. Jogo do bicho
Vídeo explicativo: https://drive.google.com/file/d/1zusej-WBqjRmz6jsh8lE5C5nBAI049i6/view?usp=share_link

* Funcionalidade:
   Noticias ->
    Servem para avisar sobre os novos lances e os ganhadores de cada lance encerrado.
  ---
 * Admin ->
    Área de administração para a banca(casa)
  ---
  * Design ->
    Responsividade para todas as telas mobile e desktop
---

* Lances
 São banners de Jogos, são usados para iniciar um novo jogo, somente o administrador pode cria-lo.

---

* Apostas
 O clinte pode fazer mais de uma aposta no mesmo lance, podendo ser de animais diferente ou iguas.

* Premiação
 A banca(casa) por padrão fica com 15% do acumulado no lances.
 Na 1º Prêmiação o ganhador levar 50% do valor descontado pela banca.
 De 2º a 5º Prêmiação, qualquer ganhador leva 25% do restante.
 valor acumulado é calculado pelo número de apostas feitas e valor da categoria do lance.
 Em cada aposta o cliente pode aposta em dois bichos.

## 2. Mega Sena
Vídeo explicativo: https://drive.google.com/file/d/1zusej-WBqjRmz6jsh8lE5C5nBAI049i6/view?usp=share_link

* Apostas 

A aposta mínima, de 6 números, custa R$ 4,50. Quanto mais números marcar, maior o preço da aposta e maiores as chances de faturar o prêmio mais cobiçado do país.

---

* Premiação 

O prêmio bruto corresponde a 43,35% da arrecadação. Dessa porcentagem:

  35% são distribuídos entre os acertadores dos 6 números sorteados (Sena);

  19% entre os acertadores de 5 números (Quina);

  19% entre os acertadores de 4 números (Quadra);

  22% ficam acumulados e são distribuídos aos acertadores dos 6 números nos concursos de final 0 ou 5.

  5% ficam acumulados para a primeira faixa - sena - do último concurso do ano de final 0 ou 5 (Mega da Virada).
