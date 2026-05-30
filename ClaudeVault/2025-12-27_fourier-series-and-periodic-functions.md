---
title: "Fourier series and periodic functions"
date: 2025-12-27
tags:
  - linux
  - research
  - web-dev
source: claude-export
---

# Fourier series and periodic functions

**Date:** 2025-12-27  
**Topics:** [[Linux]] · [[Research]] · [[Web-Dev]]

---

### 🧑 You

I B.TECH - II SEMESTER UNIT - III FOURIER SERIES CLASSES: 10 Periodic function-Determination of Fourier Coefficients-Fourier Series-Even and Odd functions-Fourier series in arbitrary interval-Half range Fourier sine and cosine expansions.

---

### 🤖 Claude

# UNIT - III: FOURIER SERIES
## B.Tech - II Semester (10 Classes)

---

## **Class 1-2: Introduction to Periodic Functions and Fourier Series**

### **Periodic Functions**
A function f(x) is said to be periodic with period T if:
$$f(x + T) = f(x) \text{ for all } x$$

The smallest positive value of T is called the fundamental period.

**Examples:**
- sin(x) has period 2π
- cos(x) has period 2π
- tan(x) has period π
- |sin(x)| has period π

### **Concept of Fourier Series**
Any periodic function f(x) with period 2π can be expressed as an infinite sum of sines and cosines:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n \cos(nx) + b_n \sin(nx)]$$

This representation is called the Fourier series of f(x).

**Physical Significance:**
- Decomposes complex periodic signals into simple sinusoidal components
- Used in signal processing, heat transfer, vibration analysis, electrical circuits

---

## **Class 3-4: Determination of Fourier Coefficients**

### **Euler's Formulas**
For a function f(x) with period 2π defined in the interval [-π, π]:

$$a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \, dx$$

$$a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) \, dx, \quad n = 1, 2, 3, ...$$

$$b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) \, dx, \quad n = 1, 2, 3, ...$$

### **Derivation of Coefficients**
The coefficients are derived using orthogonality properties:
- $\int_{-\pi}^{\pi} \sin(mx) \sin(nx) \, dx = 0$ if m ≠ n, and π if m = n
- $\int_{-\pi}^{\pi} \cos(mx) \cos(nx) \, dx = 0$ if m ≠ n, and π if m = n
- $\int_{-\pi}^{\pi} \sin(mx) \cos(nx) \, dx = 0$ for all m, n

### **Example Problem:**
Find the Fourier series of f(x) = x in [-π, π]

**Solution:**
Since f(x) = x is an odd function, a₀ = 0 and aₙ = 0.

$$b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x \sin(nx) \, dx = \frac{2(-1)^{n+1}}{n}$$

Therefore: $f(x) = 2\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin(nx)$

---

## **Class 5-6: Even and Odd Functions**

### **Even Functions**
A function f(x) is even if f(-x) = f(x)

**Properties:**
- Symmetric about y-axis
- Examples: cos(x), x², |x|, x⁴ + 1

**Fourier Series of Even Functions:**
- Contains only cosine terms (and possibly a constant)
- bₙ = 0 for all n
- $f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(nx)$

**Simplified Coefficients:**
$$a_0 = \frac{2}{\pi} \int_{0}^{\pi} f(x) \, dx$$
$$a_n = \frac{2}{\pi} \int_{0}^{\pi} f(x) \cos(nx) \, dx$$

### **Odd Functions**
A function f(x) is odd if f(-x) = -f(x)

**Properties:**
- Symmetric about origin
- Examples: sin(x), x, x³, x⁵

**Fourier Series of Odd Functions:**
- Contains only sine terms
- a₀ = 0, aₙ = 0 for all n
- $f(x) = \sum_{n=1}^{\infty} b_n \sin(nx)$

**Simplified Coefficient:**
$$b_n = \frac{2}{\pi} \int_{0}^{\pi} f(x) \sin(nx) \, dx$$

### **Example:**
Find Fourier series of f(x) = x² in [-π, π]

Since f(x) = x² is even:
$$a_0 = \frac{2}{\pi} \int_{0}^{\pi} x^2 \, dx = \frac{2\pi^2}{3}$$
$$a_n = \frac{2}{\pi} \int_{0}^{\pi} x^2 \cos(nx) \, dx = \frac{4(-1)^n}{n^2}$$

Result: $f(x) = \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} \cos(nx)$

---

## **Class 7-8: Fourier Series in Arbitrary Interval**

### **General Period 2L**
For a function with period 2L defined in [-L, L]:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right)\right]$$

**Coefficients:**
$$a_0 = \frac{1}{L} \int_{-L}^{L} f(x) \, dx$$

$$a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) dx$$

$$b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) dx$$

### **For Even Functions in [-L, L]:**
$$a_0 = \frac{2}{L} \int_{0}^{L} f(x) \, dx$$
$$a_n = \frac{2}{L} \int_{0}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) dx$$

### **For Odd Functions in [-L, L]:**
$$b_n = \frac{2}{L} \int_{0}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) dx$$

### **Example:**
Find Fourier series of f(x) = x in [-2, 2]

Here L = 2, and f(x) is odd, so:
$$b_n = \frac{2}{2} \int_{0}^{2} x \sin\left(\frac{n\pi x}{2}\right) dx = \frac{8(-1)^{n+1}}{n\pi}$$

---

## **Class 9-10: Half Range Fourier Series**

### **Half Range Fourier Sine Series**
For a function f(x) defined in the interval [0, L], we can extend it as an odd function to [-L, L] and obtain a sine series:

$$f(x) = \sum_{n=1}^{\infty} b_n \sin\left(\frac{n\pi x}{L}\right)$$

**Coefficient:**
$$b_n = \frac{2}{L} \int_{0}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) dx$$

**Applications:** Heat conduction with zero boundary conditions, vibrating strings fixed at both ends

### **Half Range Fourier Cosine Series**
For a function f(x) defined in [0, L], extend it as an even function:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\left(\frac{n\pi x}{L}\right)$$

**Coefficients:**
$$a_0 = \frac{2}{L} \int_{0}^{L} f(x) \, dx$$
$$a_n = \frac{2}{L} \int_{0}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) dx$$

**Applications:** Heat conduction with insulated boundary conditions

### **Important Note:**
The same function can have different Fourier series depending on whether we choose sine or cosine expansion.

### **Example:**
Find half range sine and cosine series for f(x) = 1 in [0, π]

**Sine Series:**
$$b_n = \frac{2}{\pi} \int_{0}^{\pi} \sin(nx) \, dx = \frac{2}{n\pi}[1 - (-1)^n]$$

**Cosine Series:**
$$a_0 = \frac{2}{\pi} \int_{0}^{\pi} 1 \, dx = 2$$
$$a_n = \frac{2}{\pi} \int_{0}^{\pi} \cos(nx) \, dx = 0$$

So cosine series: f(x) = 1 (the function itself)

---

## **Key Points to Remember:**

1. **Dirichlet Conditions** for convergence: f(x) must be periodic, have finite number of discontinuities, maxima and minima in one period

2. At points of discontinuity, Fourier series converges to the average of left and right limits

3. Parseval's identity relates function energy to Fourier coefficients

4. Choice between sine and cosine half-range series depends on boundary conditions in applications

5. Integration is simplified when recognizing even/odd symmetry

---

## **Practice Problems:**

1. Find Fourier series of f(x) = |x| in [-π, π]
2. Expand f(x) = eˣ in [-π, π] as Fourier series
3. Find half range sine series for f(x) = x in [0, 1]
4. Obtain Fourier series for f(x) = x² in [-2, 2]
5. Deduce the value of 1 - 1/3 + 1/5 - 1/7 + ... using Fourier series

---
