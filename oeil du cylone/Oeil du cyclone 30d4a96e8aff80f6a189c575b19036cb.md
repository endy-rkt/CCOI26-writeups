# Oeil du cyclone

**About:**

- Category: Crypto
- Level: Hard

**Subject:**

Le cyclone Garance a dévasté l'île de La Réunion. Le code d'activation du système d'évacuation d'urgence était protégé par un schéma de partage de secret, distribué entre 9 stations météorologiques. Le seuil de reconstruction est de 6 fragments. 5 stations en altitude sont intactes mais 4 stations côtières ont été inondées : leurs données ont perdu les bits de poids faible. flag format CCOI26

**Resource:**

- challenge: https://drive.google.com/file/d/11R7lJPIWs7zgyPi4eXDEDwtO2EntrWMP/view

In this challenge we are given these:

```
challenge.txt file about a cyclone on Reunion Island
a Shamir Secret Sharing (SSS) scheme with a threshold of 6
```

and we see this:

- 5 complete fragments from highland stations
- 4 partial fragments from flooded coastal stations where the lowest 20 bits are missing

Hypothesis:

- does we need to crack the Shamir Secret Sharing math?
- we need 6 shares but only have 5 complete ones, so how to get the 6th?

1. Let’ s see first what is this Shamir Secret sharing:

https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing
https://apogiatzis.medium.com/shamirs-secret-sharing-a-numeric-example-walkthrough-a59b288c34c4

Shamir's Secret Sharing relies on evaluating a polynomial P(x) of degree k−1 over a finite field. 
For a threshold of k=6, the polynomial has degree 5:

P(x)=S+a1x+a2x2+a3x3+a4x4+a5x5(modp)

The secret S is the constant term P(0). 
Given k distinct points (xi,yi), we can uniquely determine P(x) and retrieve S using **Lagrange Interpolation**:
S=P(0)=∑i=1kyi⋅ℓi(0)(modp)

where ℓi(0) are the Lagrange basis polynomials evaluated at x=0:

ℓi(0)=∏j≠i−xjxi−xj(modp)

1. What vulnerability we can see?

We have 5 intact shares, which is exactly k−1. We need just **one more share** to recover the secret. We have partial shares where only the lowest 20 bits are missing.

Missing 20 bits means there are only 220=1,048,576 possible values for the lost part of the share. This is a trivially small space to brute-force!

Let's pick the 6th share (Saint-Benoit, x6=6). Its true value is:

y6=Ybase+δ

where Ybase is the given flooded value (ending in `00000` in hex) and δ∈[0,220−1].

If we brute-force δ by performing a full Lagrange interpolation 1  million times, it would be computationally wasteful. Instead, we can  precompute the static parts of the equation.

The secret S as a function of δ is:

S(δ)=∑i=15yiℓi(0)+(Ybase+δ)ℓ6(0)(modp)S(δ)=(∑i=15yiℓi(0)+Ybaseℓ6(0))+δ⋅ℓ6(0)(modp)

Let C=∑i=15yiℓi(0)+Ybaseℓ6(0)(modp).

This leaves us with a highly optimized linear search:

S(δ)=C+δ⋅ℓ6(0)(modp)

We compute the sequence iteratively, converting each S(δ) to bytes. If it starts with `CCOI26{`, we hash it with SHA256 to verify against `f687cb74fdcefefc`.

To summerize:

1. **The Goal:** we need 6 pieces (shares) to put the secret flag back together.
2. **The Problem:** we only have 5 perfect pieces. The other pieces are damaged (they are missing their last 20 bits).
3. **The Trick:** Because only 20 bits are missing, there are only about 1,000,000 possible guesses for the missing part. For a computer, testing 1 million guesses takes less than a second!
4. **The Solution:**
    - Take the 5 perfect pieces and just **one** of the damaged pieces.
    - Write a script to guess the missing 1 million values for that damaged piece.
    - For every guess, use the math formula to combine the 6 pieces.
    - Check if the output gives you a text that starts with `CCOI26{`. Once it does, you have the flag!

So to solve it we use the `script.py` , and eureka

![image.png](Oeil%20du%20cyclone/image.png)
