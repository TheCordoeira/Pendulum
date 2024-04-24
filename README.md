[ENGLISH]

Fitting data is one of the coolests things in the union of physics and programming. Using python and SciPy, we can take some shortcuts and estimate parameters of an model

This model is an damped pendulum following the equation:
$\theta (t) = e^{- \alpha t}A sin(\omega t + \phi) + \kappa$.
$\theta (t)$ is the angular position related on time t, A is the amplitude, $\omega$ is the angular frequency, $\phi$ is an adjusment phase and $\kappa$ an arbitrary constant.

The intrinsic method of curve_fit from the SciPy library is the Nonlinear Least Squares method (Levenberg-Marquardt algorithm). In this model, optimization of 4 parameters is required. Therefore, the initial guess vector should be in the fourth dimension or have four variables.

Feel free to reach out if you need further assistance or want to use this as an example for your Experimental Physics work.

[Portuguese (BR)]

Ajustar dados é uma das coisas mais legais na união da física e da programação. Usando Python e SciPy, podemos tomar alguns atalhos e estimar parâmetros de um modelo.

Este modelo é um pêndulo amortecido seguindo a equação:
$\theta (t) = e^{- \alpha t}A sin(\omega t + \phi) + \kappa$.
$\theta (t)$ é a posição angular relacionada ao tempo t, A é a amplitude, $\omega$ é a frequência angular, $\phi$ é uma fase de ajuste e $\kappa$ uma constante arbitrária.

O método intrínseco do curve_fit da biblioteca SciPy é o método de Mínimos Quadrados Não Linear (algoritmo de Levenberg-Marquardt). Neste modelo, a otimização de 4 parâmetros é necessária. Portanto, o vetor de chute inicial deve estar na quarta dimensão ou ter quatro variáveis.

Fique à vontade para entrar em contato se precisar de mais assistência ou quiser usar isso como exemplo para o seu trabalho de Física Experimental.
