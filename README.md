## NTU Training Course
There are four different topics that you can see in this repository. 
* First topic is related to Try-Except excercise. And programming should be able to judge whether blank exists between two figures, and whethe figures are integer or not.
* Secondly, people can input `Year` and `Month`, and the result can output every Wednesday of the month. In this practice, programming should apply `datetime.strftime(“%w”)` to judge Wednesday.
* Third, This is a game.
  * There are two players, all initial HP is 30 and MP is 0. And There are three attack ways, Sugar Attack with power 3, Spicy Boomer with power 6, and Hot Splash with power 9.
  * Total attack power is equal to attack way plus MP. player's MP can add 1 on one of lower HP after every attack.
  * Finishing game by input `stop` or someone's HP is 0.
* Last one is relevant to Cosine Similarity. Code is able to determine which document input has best Correlation. In this topic, it should apply the following code of Cosine Similarity to sovle.
  ```py
  import math
  import operator
  def dot_product2(v1, v2):
    return sum(map(operator.mul, v1, v2))

  def cosineSimilarity(v1, v2):
    #v1請放入doc，v2請放入query
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod / (len1 * len2)
  ```
