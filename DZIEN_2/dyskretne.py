#prawdopodobieństwo wyrxucenia dokładnie 3 orłów w 5 rzutach monetą!

from scipy.stats import binom,poisson,norm,expon

#rozkład dwumianowy
p_binom = binom.pmf(3,5,0.5)
print(f"prawdopodobieństwo wyrxucenia dokładnie 3 orłów w 5 rzutach monetą: {p_binom}")

#rozkład poissona -> prawdopodobieństwo że w ciągu godziny pojawią się 2 telefony przy średniej na godzine 3
p_poiss = poisson.pmf(2,3)
print(f"prawdopodobieństwo że w ciągu godziny pojawią się 2 telefoy przy średniej na godzine 3: {p_poiss}")

#prawdopodobieństwo ze losowo wybrana osobama wzrost od 170-180cm zakładając że srodeni wzrrost to 175cm z odchyleniem 5cm


p_wzrost = norm.cdf(180,175,5) - norm.cdf(170,175,5)
print(f"prawdopodobieństwo ze losowo wybrana osobama wzrost od 170-180cm zakładając "
      f"że srodeni wzrост to 175cm z odchyleniem 5cm: {p_wzrost}")


#prawdopodobieństwo że czas oczekiwania na autobis (średnio jezdzi co 10 min, rozkład wykładniczy) będzie krótszy niż 5 minut
p_autobus = expon.cdf(5,scale=10)
print(f"prawdopodobieństwo że czas oczekiwania na autobis (średnio jezdzi co 10 min, rozkład wykładniczy) "
      f"będzie krótszy niż 5 minut: {p_autobus}")
