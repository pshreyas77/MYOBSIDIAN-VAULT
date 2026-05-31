---
title: "Discrete Mathematics Comprehensive Notes"
date: 2025-12-09
tags:
  - linux
  - obsidian
  - geopolitics
  - stock-market
  - research
  - creative
  - finance
  - web-dev
  - game-design
source: qwen-export
model: qwen3-max-2025-10-20
---

# Discrete Mathematics Comprehensive Notes

**Date:** 2025-12-09  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[Linux]] · [[Obsidian]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Since the PDF contains only the syllabus, I'll create comprehensive detailed notes for all five units with complete explanations, formulas, diagrams, and examples. This will be extensive, so let me prepare complete notes for all units.

---

# **DISCRETE MATHEMATICS - COMPLETE NOTES**
## **II B.TECH - II SEMESTER**

---

# **UNIT - I: MATHEMATICAL LOGIC**

## **1. STATEMENTS AND NOTATIONS**

### **Definition:**
A **statement (proposition)** is a declarative sentence that is either **true (T)** or **false (F)**, but not both.

### **Examples:**
✅ **Statements:**
- "5 is an odd number" (True)
- "New York is the capital of USA" (False)
- "2 + 2 = 4" (True)

❌ **Not Statements:**
- "What is your name?" (Question)
- "Please sit down" (Command)
- "x + 2 = 5" (Contains variable - truth depends on x)

### **Notation:**
- Lowercase letters: p, q, r, s
- Truth values: T or 1 (True), F or 0 (False)

---

## **2. CONNECTIVES**

| Symbol | Name | Operation | Example |
|--------|------|-----------|---------|
| ¬ or ~ | Negation | NOT | ¬p |
| ∧ | Conjunction | AND | p ∧ q |
| ∨ | Disjunction | OR | p ∨ q |
| → | Conditional | IF...THEN | p → q |
| ↔ | Biconditional | IFF | p ↔ q |

### **Truth Tables:**

**Negation (¬p):**
```
p | ¬p
--|---
T | F
F | T
```

**Conjunction (p ∧ q):**
```
p | q | p ∧ q
--|---|------
T | T |   T
T | F |   F
F | T |   F
F | F |   F
```

**Disjunction (p ∨ q):**
```
p | q | p ∨ q
--|---|------
T | T |   T
T | F |   T
F | T |   T
F | F |   F
```

**Conditional (p → q):**
```
p | q | p → q
--|---|------
T | T |   T
T | F |   F    ← Only false case
F | T |   T
F | F |   T
```

**Biconditional (p ↔ q):**
```
p | q | p ↔ q
--|---|------
T | T |   T    ← Same values
T | F |   F
F | T |   F
F | F |   T    ← Same values
```

---

## **3. WELL-FORMED FORMULAS (WFF)**

### **Rules:**
1. Single variable is WFF: p, q, r
2. If A is WFF, then ¬A is WFF
3. If A, B are WFFs, then (A ∧ B), (A ∨ B), (A → B), (A ↔ B) are WFFs

### **Precedence (High to Low):**
1. ¬ (Negation)
2. ∧ (Conjunction)
3. ∨ (Disjunction)
4. → (Conditional)
5. ↔ (Biconditional)

### **Examples:**
- Valid WFF: ((p ∧ q) → r)
- Valid WFF: ¬p ∨ (q ∧ r)
- Invalid: p q ∧ (no operator)

---

## **4. TAUTOLOGY, CONTRADICTION, CONTINGENCY**

### **Tautology:** Always TRUE
Example: p ∨ ¬p
```
p | ¬p | p ∨ ¬p
--|----| ------
T | F  |   T
F | T  |   T    ← All T
```

### **Contradiction:** Always FALSE
Example: p ∧ ¬p
```
p | ¬p | p ∧ ¬p
--|----| ------
T | F  |   F
F | T  |   F    ← All F
```

### **Contingency:** Sometimes T, sometimes F
Example: p ∧ q

---

## **5. LOGICAL EQUIVALENCES**

### **Important Laws:**

**De Morgan's Laws:**
- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q

**Commutative Laws:**
- p ∧ q ≡ q ∧ p
- p ∨ q ≡ q ∨ p

**Associative Laws:**
- (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
- (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)

**Distributive Laws:**
- p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
- p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)

**Identity Laws:**
- p ∧ T ≡ p
- p ∨ F ≡ p

**Domination Laws:**
- p ∨ T ≡ T
- p ∧ F ≡ F

**Idempotent Laws:**
- p ∧ p ≡ p
- p ∨ p ≡ p

**Absorption Laws:**
- p ∧ (p ∨ q) ≡ p
- p ∨ (p ∧ q) ≡ p

**Double Negation:**
- ¬(¬p) ≡ p

**Conditional Equivalences:**
- p → q ≡ ¬p ∨ q
- p → q ≡ ¬q → ¬p (Contrapositive)
- ¬(p → q) ≡ p ∧ ¬q

**Biconditional Equivalences:**
- p ↔ q ≡ (p → q) ∧ (q → p)
- p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)

---

## **6. NORMAL FORMS**

### **Conjunctive Normal Form (CNF):**
Product of Sums: (A ∨ B) ∧ (C ∨ D)

### **Disjunctive Normal Form (DNF):**
Sum of Products: (A ∧ B) ∨ (C ∧ D)

### **Example:**
Convert p → q to CNF and DNF

**Step 1:** p → q ≡ ¬p ∨ q (already in CNF and DNF)

**For (p → q) ∧ r:**
- **CNF:** (¬p ∨ q) ∧ r
- **DNF:** (¬p ∧ r) ∨ (q ∧ r)

---

## **7. RULES OF INFERENCE**

### **1. Modus Ponens (MP):**
```
p → q
p
-----
∴ q
```

### **2. Modus Tollens (MT):**
```
p → q
¬q
-----
∴ ¬p
```

### **3. Hypothetical Syllogism (HS):**
```
p → q
q → r
-----
∴ p → r
```

### **4. Disjunctive Syllogism (DS):**
```
p ∨ q
¬p
-----
∴ q
```

### **5. Addition:**
```
p
-----
∴ p ∨ q
```

### **6. Simplification:**
```
p ∧ q
-----
∴ p
```

### **7. Conjunction:**
```
p
q
-----
∴ p ∧ q
```

### **8. Resolution:**
```
p ∨ q
¬p ∨ r
------
∴ q ∨ r
```

---

## **8. PROOF METHODS**

### **A. Direct Method:**

**Example:** Prove r from premises:
1. p → q
2. q → r
3. p

**Proof:**
| Step | Statement | Reason |
|------|-----------|--------|
| 1 | p → q | Premise |
| 2 | q → r | Premise |
| 3 | p | Premise |
| 4 | q | MP (1,3) |
| 5 | r | MP (2,4) |

### **B. Conditional Proof (CP):**

To prove P → Q, assume P and derive Q.

**Example:** Prove (p ∧ q) → p

| Step | Statement | Reason |
|------|-----------|--------|
| 1 | p ∧ q | Assumption |
| 2 | p | Simplification (1) |
| 3 | (p ∧ q) → p | CP |

### **C. Proof by Contradiction:**

Assume ¬Q and derive contradiction.

**Example:** Prove q from p → q, p

| Step | Statement | Reason |
|------|-----------|--------|
| 1 | p → q | Premise |
| 2 | p | Premise |
| 3 | ¬q | Assumption |
| 4 | q | MP (1,2) |
| 5 | q ∧ ¬q | Contradiction |
| 6 | ∴ q | By contradiction |

---

## **9. CONSISTENCY**

A set of statements is **consistent** if they can all be true simultaneously.

**Example:** Check {p → q, p, ¬q}
- If p is true (given)
- From p → q and p: q is true
- But ¬q is given (q is false)
- **Inconsistent!**

---

## **10. AUTOMATIC THEOREM PROVING**

### **Resolution Method:**

**Steps:**
1. Convert to CNF
2. Negate conclusion
3. Apply resolution
4. Derive empty clause □

**Example:** Prove q from p ∨ q, ¬p

Clauses:
1. p ∨ q
2. ¬p
3. ¬q (negate conclusion)

Resolution:
- From (1) and (2): q
- From q and (3): □ (contradiction)
- **Proved!**

---

---

# **UNIT - II: RELATIONS**

## **1. INTRODUCTION TO SET THEORY**

### **Set Definition:**
A **set** is a well-defined collection of distinct objects.

### **Notation:**
- A = {1, 2, 3, 4}
- B = {x | x is even number}
- ∈ : belongs to
- ∉ : does not belong to
- ⊆ : subset
- ⊂ : proper subset

### **Types of Sets:**
1. **Empty Set:** ∅ or { }
2. **Finite Set:** A = {1, 2, 3}
3. **Infinite Set:** N = {1, 2, 3, ...}
4. **Universal Set:** U
5. **Power Set:** P(A) = set of all subsets

### **Set Operations:**

**Union (A ∪ B):**
A ∪ B = {x | x ∈ A or x ∈ B}

**Intersection (A ∩ B):**
A ∩ B = {x | x ∈ A and x ∈ B}

**Difference (A - B):**
A - B = {x | x ∈ A and x ∉ B}

**Complement (A'):**
A' = {x | x ∈ U and x ∉ A}

### **Important Formulas:**

**Cardinality:**
- |A ∪ B| = |A| + |B| - |A ∩ B|
- |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |B ∩ C| - |A ∩ C| + |A ∩ B ∩ C|

**Power Set:**
- If |A| = n, then |P(A)| = 2ⁿ

**Cartesian Product:**
- A × B = {(a,b) | a ∈ A, b ∈ B}
- |A × B| = |A| × |B|

---

## **2. RELATIONS**

### **Definition:**
A **relation R** from set A to set B is a subset of A × B.

**Notation:** 
- R ⊆ A × B
- (a, b) ∈ R or aRb

### **Example:**
A = {1, 2, 3}, B = {x, y}
R = {(1, x), (2, y), (3, x)}

### **Types of Relations:**
1. **Empty Relation:** R = ∅
2. **Universal Relation:** R = A × A
3. **Identity Relation:** R = {(a, a) | a ∈ A}
4. **Inverse Relation:** R⁻¹ = {(b, a) | (a, b) ∈ R}

---

## **3. PROPERTIES OF BINARY RELATIONS**

Let R be a relation on set A.

### **1. Reflexive:**
**Definition:** ∀a ∈ A, (a, a) ∈ R

**Example:** 
- "≤" on integers is reflexive (a ≤ a)
- R = {(1,1), (2,2), (3,3)} on {1,2,3} is reflexive

### **2. Symmetric:**
**Definition:** If (a, b) ∈ R, then (b, a) ∈ R

**Example:**
- "is sibling of" is symmetric
- R = {(1,2), (2,1), (3,3)} is symmetric

### **3. Antisymmetric:**
**Definition:** If (a, b) ∈ R and (b, a) ∈ R, then a = b

**Example:**
- "≤" is antisymmetric
- R = {(1,1), (1,2), (2,2)} is antisymmetric

### **4. Transitive:**
**Definition:** If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R

**Example:**
- "<" is transitive (if a < b and b < c, then a < c)
- "is ancestor of" is transitive

### **Summary Table:**

| Relation | Reflexive | Symmetric | Antisymmetric | Transitive |
|----------|-----------|-----------|---------------|------------|
| < | No | No | Yes | Yes |
| ≤ | Yes | No | Yes | Yes |
| = | Yes | Yes | Yes | Yes |

---

## **4. EQUIVALENCE RELATION**

### **Definition:**
A relation R is an **equivalence relation** if it is:
1. **Reflexive**
2. **Symmetric**
3. **Transitive**

### **Example:**
"Congruence modulo n" on integers:
- a ≡ b (mod n) if n divides (a - b)
- Reflexive: a ≡ a (mod n) ✓
- Symmetric: a ≡ b ⟹ b ≡ a ✓
- Transitive: a ≡ b, b ≡ c ⟹ a ≡ c ✓

### **Equivalence Classes:**

**Definition:** [a] = {x ∈ A | xRa}

**Example:** For mod 3 on {0,1,2,3,4,5,6}:
- [0] = {0, 3, 6}
- [1] = {1, 4}
- [2] = {2, 5}

**Properties:**
1. Every element belongs to exactly one equivalence class
2. Equivalence classes partition the set
3. Either [a] = [b] or [a] ∩ [b] = ∅

---

## **5. PARTIAL ORDERING RELATIONS**

### **Definition:**
A relation R is a **partial order (POSET)** if it is:
1. **Reflexive**
2. **Antisymmetric**
3. **Transitive**

**Notation:** (A, ≤) denotes POSET

### **Example:**
- "≤" on real numbers
- "⊆" on power set
- "divides" on positive integers

### **Comparable Elements:**
Elements a, b are comparable if a ≤ b or b ≤ a

### **Total Order:**
A partial order where every pair is comparable.

### **Special Elements:**

**1. Maximal Element:** 
No element is greater than it

**2. Minimal Element:** 
No element is less than it

**3. Greatest Element (Maximum):**
Greater than or equal to all elements

**4. Least Element (Minimum):**
Less than or equal to all elements

**5. Upper Bound:**
Element greater than or equal to all elements in subset

**6. Lower Bound:**
Element less than or equal to all elements in subset

**7. Least Upper Bound (LUB/Supremum):**
Smallest upper bound

**8. Greatest Lower Bound (GLB/Infimum):**
Largest lower bound

---

## **6. HASSE DIAGRAM**

### **Definition:**
A visual representation of a POSET.

### **Rules to Draw:**
1. Draw vertices for each element
2. Place smaller elements lower
3. Draw edge from a to b if a < b and no element between them
4. Remove reflexive loops
5. Remove transitive edges

### **Example:**
A = {1, 2, 3, 6}, R = "divides"

```
        6
       / \
      2   3
       \ /
        1
```

**Reading:**
- 1 divides 2, 3, 6
- 2 divides 6
- 3 divides 6

---

## **7. LATTICES**

### **Definition:**
A POSET (L, ≤) is a **lattice** if every pair of elements has:
1. **LUB (join):** a ∨ b
2. **GLB (meet):** a ∧ b

### **Example:**
Divisors of 12: {1, 2, 3, 4, 6, 12}

```
       12
      / | \
     4  6  
     |\ |\ 
     2  3
      \ /
       1
```

- LUB(2,3) = 6
- GLB(4,6) = 2

### **Properties:**

**1. Commutative:**
- a ∨ b = b ∨ a
- a ∧ b = b ∧ a

**2. Associative:**
- (a ∨ b) ∨ c = a ∨ (b ∨ c)
- (a ∧ b) ∧ c = a ∧ (b ∧ c)

**3. Absorption:**
- a ∨ (a ∧ b) = a
- a ∧ (a ∨ b) = a

**4. Idempotent:**
- a ∨ a = a
- a ∧ a = a

### **Types of Lattices:**

**1. Bounded Lattice:**
Has greatest element (1) and least element (0)

**2. Complemented Lattice:**
Every element a has complement a' where:
- a ∨ a' = 1
- a ∧ a' = 0

**3. Distributive Lattice:**
- a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)

**4. Boolean Lattice:**
Complemented distributive lattice

---

## **8. TRANSITIVE CLOSURE**

### **Definition:**
The **transitive closure R⁺** of R is the smallest transitive relation containing R.

### **Warshall's Algorithm:**

**Input:** Adjacency matrix M of relation R
**Output:** Transitive closure matrix

**Algorithm:**
```
For k = 1 to n:
    For i = 1 to n:
        For j = 1 to n:
            M[i][j] = M[i][j] OR (M[i][k] AND M[k][j])
```

### **Example:**
R = {(1,2), (2,3), (3,4)}

**Matrix M:**
```
  1 2 3 4
1[0 1 0 0]
2[0 0 1 0]
3[0 0 0 1]
4[0 0 0 0]
```

**After Warshall's:**
```
  1 2 3 4
1[0 1 1 1]  (1→2→3→4)
2[0 0 1 1]  (2→3→4)
3[0 0 0 1]  (3→4)
4[0 0 0 0]
```

R⁺ = {(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)}

---

## **9. FUNCTIONS**

### **Definition:**
A function f: A → B is a relation where each element in A maps to exactly one element in B.

### **Types:**

**1. One-to-One (Injective):**
Different inputs → Different outputs
f(a₁) = f(a₂) ⟹ a₁ = a₂

**2. Onto (Surjective):**
Every element in B is mapped
∀b ∈ B, ∃a ∈ A such that f(a) = b

**3. Bijective:**
Both one-to-one and onto

### **Inverse Function:**
f⁻¹: B → A exists if f is bijective
f⁻¹(b) = a if f(a) = b

### **Composition of Functions:**
(g ∘ f)(x) = g(f(x))

**Properties:**
- Associative: (h ∘ g) ∘ f = h ∘ (g ∘ f)
- Not commutative: g ∘ f ≠ f ∘ g (generally)

**Example:**
f(x) = 2x, g(x) = x + 3
- (g ∘ f)(x) = g(f(x)) = g(2x) = 2x + 3
- (f ∘ g)(x) = f(g(x)) = f(x+3) = 2(x+3) = 2x + 6

---

## **10. ALGEBRAIC SYSTEMS**

### **Definition:**
An **algebraic system** is a set with one or more binary operations.

**Notation:** (S, *)

### **Properties of Binary Operation *:**

**1. Closure:**
∀a, b ∈ S, a * b ∈ S

**2. Associativity:**
(a * b) * c = a * (b * c)

**3. Commutativity:**
a * b = b * a

**4. Identity Element (e):**
a * e = e * a = a

**5. Inverse Element:**
a * a⁻¹ = a⁻¹ * a = e

---

## **11. SEMIGROUPS**

### **Definition:**
A **semigroup** is (S, *) where:
1. * is **closed**
2. * is **associative**

### **Example:**
- (N, +): Natural numbers under addition
- (N, ×): Natural numbers under multiplication

---

## **12. MONOIDS**

### **Definition:**
A **monoid** is a semigroup with an **identity element**.

**Requirements:**
1. Closure
2. Associativity
3. Identity element exists

### **Example:**
- (N, +, 0): 0 is identity
- (N, ×, 1): 1 is identity
- (Strings, concatenation, ""): Empty string is identity

### **Properties:**
- Identity element is unique
- (a * b) * c = a * (b * c)

---

---

# **UNIT - III: ELEMENTARY COMBINATORICS**

## **1. BASIS OF COUNTING**

### **Fundamental Principles:**

### **A. Addition Principle (OR Rule):**
If task A can be done in **m** ways and task B in **n** ways (mutually exclusive), then A **OR** B can be done in **m + n** ways.

**Example:** 
- 5 routes by bus, 3 routes by train
- Total ways = 5 + 3 = **8 ways**

### **B. Multiplication Principle (AND Rule):**
If task A can be done in **m** ways and task B in **n** ways (independent), then A **AND** B can be done in **m × n** ways.

**Example:**
- 4 shirts, 3 pants
- Total outfits = 4 × 3 = **12 outfits**

---

## **2. PERMUTATIONS**

### **Definition:**
A **permutation** is an arrangement of objects where **order matters**.

### **Formula:**

**1. Permutation of n objects:**
P(n, n) = n!

**2. Permutation of r objects from n:**
P(n, r) = n!/(n-r)!

### **Examples:**

**Example 1:** Arrange 5 books on a shelf
- P(5, 5) = 5! = **120 ways**

**Example 2:** Select 3 positions from 7 people
- P(7, 3) = 7!/(7-3)! = 7!/4! = 7×6×5 = **210 ways**

### **Circular Permutations:**
Arrangements in a circle: **(n-1)!**

**Example:** 5 people around a table
- (5-1)! = 4! = **24 ways**

---

## **3. COMBINATIONS**

### **Definition:**
A **combination** is a selection of objects where **order doesn't matter**.

### **Formula:**
C(n, r) = n!/(r!(n-r)!)

**Also written as:** (n choose r) or ⁿCᵣ

### **Examples:**

**Example 1:** Choose 3 students from 10
- C(10, 3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = **120 ways**

**Example 2:** Select a committee of 4 from 12 people
- C(12, 4) = 12!/(4!×8!) = **495 ways**

### **Properties:**
1. C(n, r) = C(n, n-r)
2. C(n, 0) = C(n, n) = 1
3. C(n, r) + C(n, r-1) = C(n+1, r) (Pascal's Identity)

---

## **4. PERMUTATIONS WITH REPETITION**

### **Formula:**
n objects with repetitions: n₁ of type 1, n₂ of type 2, ..., nₖ of type k

**Permutations = n!/(n₁! × n₂! × ... × nₖ!)**

### **Examples:**

**Example 1:** Arrangements of "MISSISSIPPI"
- Total letters: 11
- M: 1, I: 4, S: 4, P: 2
- Arrangements = 11!/(1!×4!×4!×2!) = **34,650 ways**

**Example 2:** Arrangements of "BANANA"
- Total: 6
- B: 1, A: 3, N: 2
- Arrangements = 6!/(1!×3!×2!) = **60 ways**

---

## **5. COMBINATIONS WITH REPETITION**

### **Formula:**
Selecting r objects from n types (repetition allowed):

**C(n+r-1, r) = (n+r-1)!/(r!(n-1)!)**

### **Example:**
Select 4 fruits from {apple, orange, banana}
- n = 3, r = 4
- C(3+4-1, 4) = C(6, 4) = **15 ways**

**Possible selections:**
- 4 apples
- 3 apples, 1 orange
- 2 apples, 2 oranges
- etc.

---

## **6. PERMUTATIONS WITH CONSTRAINED REPETITIONS**

### **Restricted Positions:**

**Example 1:** Arrange A, B, C, D, E where A, B must be together
- Treat AB as single unit: {AB, C, D, E} = 4 objects
- Arrangements = 4! = 24
- AB can be arranged in 2! = 2 ways
- Total = 4! × 2! = **48 ways**

**Example 2:** Arrange 5 people where 2 specific people cannot be adjacent
- Total arrangements = 5! = 120
- Arrangements with them together = 4! × 2! = 48
- Answer = 120 - 48 = **72 ways**

---

## **7. BINOMIAL COEFFICIENTS**

### **Definition:**
The coefficient of xʳ in expansion of (1+x)ⁿ

**Notation:** (n choose r) or C(n, r)

### **Pascal's Triangle:**
```
           1
         1   1
       1   2   1
     1   3   3   1
   1   4   6   4   1
 1   5  10  10   5   1
```

### **Properties:**
1. C(n, 0) + C(n, 1) + ... + C(n, n) = 2ⁿ
2. C(n, 0) - C(n, 1) + C(n, 2) - ... = 0
3. C(n, r) = C(n-1, r-1) + C(n-1, r)

---

## **8. BINOMIAL THEOREM**

### **Formula:**
(x + y)ⁿ = Σ C(n, r) × xⁿ⁻ʳ × yʳ  (r = 0 to n)

### **Expansion:**
(x + y)ⁿ = C(n,0)xⁿ + C(n,1)xⁿ⁻¹y + C(n,2)xⁿ⁻²y² + ... + C(n,n)yⁿ

### **Examples:**

**Example 1:** Expand (x + 2)⁴
```
= C(4,0)x⁴ + C(4,1)x³(2) + C(4,2)x²(2²) + C(4,3)x(2³) + C(4,4)(2⁴)
= x⁴ + 8x³ + 24x² + 32x + 16
```

**Example 2:** Find coefficient of x⁵ in (2x + 3)⁷
- General term: C(7,r)(2x)⁷⁻ʳ(3)ʳ
- For x⁵: 7-r = 5 ⟹ r = 2
- Coefficient = C(7,2) × 2⁵ × 3² = 21 × 32 × 9 = **6048**

---

## **9. MULTINOMIAL THEOREM**

### **Formula:**
(x₁ + x₂ + ... + xₘ)ⁿ = Σ [n!/(n₁!n₂!...nₘ!)] × x₁ⁿ¹ × x₂ⁿ² × ... × xₘⁿᵐ

Where n₁ + n₂ + ... + nₘ = n

### **Example:**
Coefficient of x²y³z in (x + y + z)⁶

n₁ = 2, n₂ = 3, n₃ = 1, n = 6
Coefficient = 6!/(2!×3!×1!) = 720/(2×6×1) = **60**

---

## **10. INCLUSION-EXCLUSION PRINCIPLE**

### **For Two Sets:**
|A ∪ B| = |A| + |B| - |A ∩ B|

### **For Three Sets:**
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |B ∩ C| - |A ∩ C| + |A ∩ B ∩ C|

### **General Formula:**
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|

### **Example:**

**Problem:** In a class of 50 students:
- 30 study Math
- 25 study Physics
- 20 study Chemistry
- 15 study Math and Physics
- 12 study Physics and Chemistry
- 10 study Math and Chemistry
- 8 study all three

**Find:** Students studying at least one subject

**Solution:**
|M ∪ P ∪ C| = |M| + |P| + |C| - |M∩P| - |P∩C| - |M∩C| + |M∩P∩C|
= 30 + 25 + 20 - 15 - 12 - 10 + 8
= **46 students**

---

## **11. PIGEONHOLE PRINCIPLE**

### **Basic Principle:**
If **n+1** objects are placed into **n** boxes, at least one box contains **2 or more** objects.

### **Generalized Principle:**
If **n** objects are placed into **k** boxes, at least one box contains **⌈n/k⌉** objects.

### **Examples:**

**Example 1:** 
In any group of 13 people, at least 2 have birthdays in the same month.
- 13 people (pigeons), 12 months (holes)
- ⌈13/12⌉ = 2 people in same month

**Example 2:**
Show that among 5 points inside a square of side 2, at least two are within √2 distance.

**Solution:**
- Divide square into 4 unit squares
- 5 points in 4 squares
- At least 2 points in same unit square
- Maximum distance in unit square = √(1² + 1²) = √2

**Example 3:**
From integers 1 to 100, select 51 numbers. Show that at least two are consecutive.

**Solution:**
- Form 50 pairs: {1,2}, {3,4}, ..., {99,100}
- 51 numbers from 50 pairs
- At least 2 from same pair (consecutive)

---

---

# **UNIT - IV: RECURRENCE RELATIONS**

## **1. GENERATING FUNCTIONS**

### **Definition:**
For sequence {aₙ}, the **generating function** is:

**G(x) = a₀ + a₁x + a₂x² + a₃x³ + ... = Σ aₙxⁿ**

### **Purpose:**
- Encode sequence information
- Solve recurrence relations
- Find closed formulas

### **Common Generating Functions:**

**1. Geometric Series:**
1/(1-x) = 1 + x + x² + x³ + ...
(for |x| < 1)

**2. Binomial Series:**
(1+x)ⁿ = Σ C(n,k)xᵏ  (k=0 to n)

**3. Exponential:**
eˣ = 1 + x + x²/2! + x³/3! + ...

---

## **2. CALCULATING COEFFICIENTS**

### **Methods:**

**A. Direct Expansion:**

**Example:** Find coefficient of x⁵ in (1-2x)⁻³

Using binomial series:
(1-2x)⁻³ = Σ C(-3, k)(-2x)ᵏ
For x⁵: k = 5
Coefficient = C(-3, 5)(-2)⁵ = C(7, 5)(-32) = 21×32 = **672**

**B. Partial Fractions:**

**Example:** Find aₙ if G(x) = (3x+1)/((1-x)(1-2x))

**Step 1:** Partial fractions
(3x+1)/((1-x)(1-2x)) = A/(1-x) + B/(1-2x)

Solving: A = 4, B = -1

**Step 2:** Expand
G(x) = 4/(1-x) - 1/(1-2x)
= 4(1 + x + x² + ...) - (1 + 2x + 4x² + ...)
= 3 + 2x + 0x² + ...

Coefficient of xⁿ: **aₙ = 4 - 2ⁿ**

---

## **3. RECURRENCE RELATIONS**

### **Definition:**
An equation expressing aₙ in terms of previous terms.

### **Examples:**
- aₙ = aₙ₋₁ + aₙ₋₂ (Fibonacci)
- aₙ = 2aₙ₋₁ + 1
- aₙ = aₙ₋₁ + n

### **Types:**

**1. Linear Recurrence:**
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ + f(n)

**2. Homogeneous:**
f(n) = 0

**3. Non-homogeneous:**
f(n) ≠ 0

---

## **4. SOLVING BY SUBSTITUTION**

### **Method:**
Repeatedly substitute previous terms until pattern emerges.

### **Example:**
Solve: aₙ = 2aₙ₋₁ + 1, a₀ = 1

**Substitutions:**
```
a₁ = 2a₀ + 1 = 2(1) + 1 = 3
a₂ = 2a₁ + 1 = 2(3) + 1 = 7
a₃ = 2a₂ + 1 = 2(7) + 1 = 15
a₄ = 2a₃ + 1 = 2(15) + 1 = 31
```

**Pattern:** aₙ = 2ⁿ⁺¹ - 1

**Verification:**
- a₀ = 2¹ - 1 = 1 ✓
- aₙ = 2ⁿ⁺¹ - 1
- aₙ₋₁ = 2ⁿ - 1
- 2aₙ₋₁ + 1 = 2(2ⁿ - 1) + 1 = 2ⁿ⁺¹ - 1 = aₙ ✓

---

## **5. SOLVING BY GENERATING FUNCTIONS**

### **Method:**
1. Multiply recurrence by xⁿ
2. Sum over all n
3. Express as generating function
4. Solve for G(x)
5. Extract coefficient

### **Example:**
Solve: aₙ = 3aₙ₋₁ - 2aₙ₋₂, a₀ = 0, a₁ = 1

**Step 1:** Let G(x) = Σ aₙxⁿ

**Step 2:** Multiply by xⁿ and sum:
Σ aₙxⁿ = 3Σ aₙ₋₁xⁿ - 2Σ aₙ₋₂xⁿ

**Step 3:** 
G(x) = 3xG(x) - 2x²G(x) + x

**Step 4:** Solve for G(x)
G(x)(1 - 3x + 2x²) = x
G(x) = x/(1 - 3x + 2x²) = x/((1-x)(1-2x))

**Step 5:** Partial fractions
G(x) = -1/(1-x) + 1/(1-2x)

**Step 6:** Expand
G(x) = -(1 + x + x² + ...) + (1 + 2x + 4x² + ...)
= (2ⁿ - 1)xⁿ

**Answer:** aₙ = 2ⁿ - 1

---

## **6. METHOD OF CHARACTERISTIC ROOTS**

### **For Homogeneous Linear Recurrence:**
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ

### **Steps:**

**1. Form characteristic equation:**
rᵏ = c₁rᵏ⁻¹ + c₂rᵏ⁻² + ... + cₖ

Or: rᵏ - c₁rᵏ⁻¹ - c₂rᵏ⁻² - ... - cₖ = 0

**2. Solve for roots r₁, r₂, ..., rₖ**

**3. General solution:**

**Case 1: Distinct roots**
aₙ = A₁r₁ⁿ + A₂r₂ⁿ + ... + Aₖrₖⁿ

**Case 2: Repeated roots (r repeated m times)**
aₙ = (A₁ + A₂n + A₃n² + ... + Aₘnᵐ⁻¹)rⁿ

**4. Use initial conditions to find constants**

---

### **Example 1: Distinct Roots**

**Solve:** aₙ = 5aₙ₋₁ - 6aₙ₋₂, a₀ = 1, a₁ = 4

**Step 1:** Characteristic equation
r² = 5r - 6
r² - 5r + 6 = 0
(r-2)(r-3) = 0

**Roots:** r₁ = 2, r₂ = 3

**Step 2:** General solution
aₙ = A(2ⁿ) + B(3ⁿ)

**Step 3:** Apply initial conditions
a₀ = 1: A + B = 1
a₁ = 4: 2A + 3B = 4

Solving: A = -1, B = 2

**Answer:** aₙ = -2ⁿ + 2(3ⁿ) = **2(3ⁿ) - 2ⁿ**

---

### **Example 2: Repeated Roots**

**Solve:** aₙ = 4aₙ₋₁ - 4aₙ₋₂, a₀ = 2, a₁ = 4

**Step 1:** Characteristic equation
r² - 4r + 4 = 0
(r-2)² = 0

**Root:** r = 2 (repeated)

**Step 2:** General solution
aₙ = (A + Bn)2ⁿ

**Step 3:** Apply initial conditions
a₀ = 2: A = 2
a₁ = 4: (A + B)2 = 4 ⟹ 2 + B = 2 ⟹ B = 0

**Answer:** aₙ = **2ⁿ⁺¹**

---

### **Example 3: Fibonacci Sequence**

**Solve:** Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1

**Characteristic equation:**
r² = r + 1
r² - r - 1 = 0

**Roots:**
r = (1 ± √5)/2
r₁ = (1 + √5)/2 = φ (golden ratio)
r₂ = (1 - √5)/2

**General solution:**
Fₙ = A·φⁿ + B·((1-√5)/2)ⁿ

**Using initial conditions:**
F₀ = 0, F₁ = 1

After solving:
**Fₙ = (φⁿ - (1-φ)ⁿ)/√5** (Binet's formula)

---

## **7. NON-HOMOGENEOUS RECURRENCES**

### **Form:**
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + f(n)

### **Solution:**
aₙ = aₙ⁽ʰ⁾ + aₙ⁽ᵖ⁾

Where:
- aₙ⁽ʰ⁾ = homogeneous solution
- aₙ⁽ᵖ⁾ = particular solution

### **Finding Particular Solution:**

**If f(n) = constant c:**
Try aₙ⁽ᵖ⁾ = k

**If f(n) = polynomial:**
Try aₙ⁽ᵖ⁾ = polynomial of same degree

**If f(n) = rⁿ:**
Try aₙ⁽ᵖ⁾ = krⁿ

### **Example:**
Solve: aₙ = 2aₙ₋₁ + 3, a₀ = 1

**Homogeneous:** aₙ = 2aₙ₋₁
Characteristic: r = 2
aₙ⁽ʰ⁾ = A(2ⁿ)

**Particular:** Try aₙ⁽ᵖ⁾ = k
k = 2k + 3
k = -3

**General:** aₙ = A(2ⁿ) - 3

**Initial condition:** a₀ = 1
1 = A - 3 ⟹ A = 4

**Answer:** aₙ = **4(2ⁿ) - 3**

---

---

# **UNIT - V: GRAPH THEORY**

## **1. BASIC CONCEPTS**

### **Graph Definition:**
A **graph G = (V, E)** consists of:
- **V:** Set of vertices (nodes)
- **E:** Set of edges (connections)

### **Types of Graphs:**

**1. Undirected Graph:**
Edges have no direction
Edge: {u, v}

**2. Directed Graph (Digraph):**
Edges have direction
Edge: (u, v) from u to v

**3. Weighted Graph:**
Edges have weights/costs

**4. Simple Graph:**
- No loops (edge from vertex to itself)
- No multiple edges

**5. Multigraph:**
Multiple edges between vertices allowed

**6. Complete Graph (Kₙ):**
Every pair of vertices connected
Edges = n(n-1)/2

**7. Bipartite Graph:**
Vertices divided into two sets
Edges only between sets

**8. Cycle Graph (Cₙ):**
Forms a closed loop

**9. Path Graph (Pₙ):**
Simple path with n vertices

---

### **Graph Terminology:**

**1. Degree:**
- **deg(v):** Number of edges incident to v
- In digraph: in-degree + out-degree

**2. Path:**
Sequence of vertices connected by edges

**3. Cycle:**
Path starting and ending at same vertex

**4. Connected Graph:**
Path exists between every pair of vertices

**5. Component:**
Maximal connected subgraph

**6. Adjacent Vertices:**
Connected by an edge

**7. Incident:**
Edge connected to vertex

---

### **Important Theorems:**

**Handshaking Lemma:**
Σ deg(v) = 2|E|

Sum of all degrees = 2 × number of edges

**Corollary:**
Number of odd-degree vertices is even

---

## **2. GRAPH REPRESENTATION**

### **A. Adjacency Matrix:**

For graph with n vertices: n × n matrix A
- A[i][j] = 1 if edge exists from i to j
- A[i][j] = 0 otherwise

**Example:**
```
Graph: 1-2, 1-3, 2-3

  1 2 3
1[0 1 1]
2[1 0 1]
3[1 1 0]
```

**Properties:**
- Undirected: Symmetric matrix
- Space: O(n²)
- Check edge: O(1)

### **B. Adjacency List:**

Array of lists
- Each vertex has list of adjacent vertices

**Example:**
```
1 → [2, 3]
2 → [1, 3]
3 → [1, 2]
```

**Properties:**
- Space: O(|V| + |E|)
- Better for sparse graphs

---

## **3. ISOMORPHISM AND SUBGRAPHS**

### **Graph Isomorphism:**

Graphs G₁ and G₂ are **isomorphic** if there exists bijection f: V₁ → V₂ such that:
- (u, v) ∈ E₁ ⟺ (f(u), f(v)) ∈ E₂

**Same structure, different labels**

### **Necessary Conditions:**
- Same number of vertices
- Same number of edges
- Same degree sequence
- Same number of cycles

### **Subgraph:**
G' = (V', E') is subgraph of G = (V, E) if:
- V' ⊆ V
- E' ⊆ E

### **Induced Subgraph:**
Subgraph with all edges between vertices in V'

---

## **4. TREES**

### **Definition:**
A **tree** is a connected acyclic graph.

### **Properties:**
1. Connected with n vertices has n-1 edges
2. Exactly one path between any two vertices
3. Removing any edge disconnects graph
4. Adding any edge creates a cycle
5. Acyclic with n vertices becomes tree by adding one edge

### **Types of Trees:**

**1. Rooted Tree:**
- One vertex designated as root
- Parent-child relationships

**2. Binary Tree:**
- Each node has at most 2 children
- Left child and right child

**3. Spanning Tree:**
- Subgraph that is a tree
- Includes all vertices
- Minimal connected subgraph

### **Forest:**
Acyclic graph (collection of trees)

---

## **5. SPANNING TREES - DFS & BFS**

### **A. Depth-First Search (DFS):**

**Algorithm:**
```
DFS(v):
    mark v as visited
    for each unvisited neighbor u of v:
        DFS(u)
```

**Example:**
```
Graph:    1---2
          |   |
          3---4

DFS from 1: 1 → 2 → 4 → 3

Spanning Tree:
    1---2
    |   |
    3   4
```

**Properties:**
- Time: O(|V| + |E|)
- Space: O(|V|) for recursion stack
- Produces DFS spanning tree

---

### **B. Breadth-First Search (BFS):**

**Algorithm:**
```
BFS(s):
    create queue Q
    mark s as visited, enqueue s
    while Q not empty:
        v = dequeue
        for each unvisited neighbor u of v:
            mark u as visited
            enqueue u
```

**Example:**
```
Graph:    1---2
          |\ /|
          | X |
          |/ \|
          3---4

BFS from 1: 1 → 2 → 3 → 4

Spanning Tree:
    1---2
    |   
    3---4
```

**Properties:**
- Time: O(|V| + |E|)
- Space: O(|V|) for queue
- Shortest path in unweighted graph

---

## **6. MINIMUM SPANNING TREE**

### **Definition:**
Spanning tree with **minimum total edge weight**.

---

### **A. PRIM'S ALGORITHM**

**Greedy approach:** Grow tree from starting vertex

**Algorithm:**
```
1. Start with any vertex
2. Add minimum weight edge connecting tree to non-tree vertex
3. Repeat until all vertices included
```

**Example:**
```
Graph:
    1--[2]--2
    |       |
   [3]     [1]
    |       |
    3--[4]--4

Start from 1:
Step 1: Add 1-2 (weight 2)
Step 2: Add 2-4 (weight 1)
Step 3: Add 1-3 (weight 3)

MST weight = 2 + 1 + 3 = 6
```

**Complexity:** O(|E| log |V|) with priority queue

---

### **B. KRUSKAL'S ALGORITHM**

**Greedy approach:** Select minimum weight edges without creating cycles

**Algorithm:**
```
1. Sort edges by weight
2. For each edge (u, v):
    if u and v not in same component:
        add edge to MST
        merge components
```

**Uses Union-Find data structure**

**Example:**
```
Edges sorted:
(2,4):1, (1,2):2, (1,3):3, (3,4):4

Step 1: Add (2,4):1
Step 2: Add (1,2):2
Step 3: Add (1,3):3
(Skip (3,4) - creates cycle)

MST weight = 6
```

**Complexity:** O(|E| log |E|)

---

## **7. PLANAR GRAPHS**

### **Definition:**
A graph is **planar** if it can be drawn on plane without edge crossings.

### **Examples:**
- **Planar:** K₄, Trees, Cycles
- **Non-planar:** K₅, K₃,₃

---

### **EULER'S FORMULA**

For connected planar graph:

**V - E + F = 2**

Where:
- V = vertices
- E = edges  
- F = faces (including outer face)

**Example:**
```
Square:
V = 4, E = 4, F = 2 (inside + outside)
4 - 4 + 2 = 2 ✓
```

---

### **Consequences:**

**For simple planar graph:**
1. E ≤ 3V - 6
2. At least one vertex has degree ≤ 5

**For bipartite planar graph:**
E ≤ 2V - 4

---

### **Kuratowski's Theorem:**

Graph is planar ⟺ it doesn't contain K₅ or K₃,₃ as subdivision

---

## **8. EULER CIRCUITS & PATHS**

### **Definitions:**

**Euler Path:**
Path that uses every edge exactly once

**Euler Circuit:**
Circuit that uses every edge exactly once

---

### **Theorems:**

**Euler Circuit exists ⟺**
- Graph is connected
- All vertices have **even degree**

**Euler Path exists ⟺**
- Graph is connected
- Exactly **2 vertices** have **odd degree**

---

### **Examples:**

**Example 1:**
```
Graph: Square
All vertices degree 2 (even)
→ Euler Circuit exists ✓
```

**Example 2:**
```
Graph: 
    1---2
    |   |
    3---4
     \ /
      5

Degrees: 1(2), 2(2), 3(3), 4(3), 5(2)
Two odd degrees (3, 4)
→ Euler Path exists from 3 to 4 ✓
→ No Euler Circuit ✗
```

---

### **Fleury's Algorithm:**

Find Euler circuit/path:
```
1. Start at odd-degree vertex (if exists)
2. Follow edges:
   - Don't use bridge unless no choice
3. Remove used edge
4. Repeat until all edges used
```

---

## **9. MULTIGRAPHS**

### **Definition:**
Graph allowing **multiple edges** between vertices.

### **Euler Circuit in Multigraph:**

Same condition: All vertices even degree

**Application:** Chinese Postman Problem
- Find shortest circuit visiting all edges
- Add minimum edges to make all degrees even

---

## **10. HAMILTONIAN GRAPHS**

### **Definitions:**

**Hamiltonian Path:**
Path visiting every **vertex** exactly once

**Hamiltonian Circuit:**
Circuit visiting every **vertex** exactly once

---

### **Theorems:**

**Dirac's Theorem:**
If deg(v) ≥ n/2 for all v in graph with n ≥ 3 vertices
→ Graph has Hamiltonian circuit

**Ore's Theorem:**
If deg(u) + deg(v) ≥ n for every non-adjacent u, v
→ Graph has Hamiltonian circuit

---

### **Examples:**

**Example 1:**
```
Complete graph Kₙ (n ≥ 3)
→ Always Hamiltonian ✓
```

**Example 2:**
```
Cycle Cₙ
→ Itself is Hamiltonian circuit ✓
```

**Example 3:**
```
Petersen Graph
→ Hamiltonian path exists
→ No Hamiltonian circuit
```

---

### **Differences: Euler vs Hamiltonian**

| Property | Euler | Hamiltonian |
|----------|-------|-------------|
| Focuses on | Edges | Vertices |
| Condition | Degree parity | No simple condition |
| Complexity | Polynomial | NP-complete |
| Detection | Easy | Hard |

---

## **11. GRAPH COLORING**

### **Vertex Coloring:**
Assign colors to vertices so adjacent vertices have different colors.

### **Chromatic Number χ(G):**
Minimum number of colors needed.

---

### **Examples:**

**1. χ(Kₙ) = n**
(Complete graph needs n colors)

**2. χ(Cₙ) = 2 if n even, 3 if n odd**

**3. χ(Bipartite) = 2**

**4. χ(Planar) ≤ 4** (Four Color Theorem)

---

### **Greedy Coloring Algorithm:**

```
1. Order vertices v₁, v₂, ..., vₙ
2. For each vertex vᵢ:
    Assign smallest color not used by neighbors
```

**Not optimal but polynomial time**

---

### **Applications:**

1. **Scheduling:** No conflicts
2. **Register Allocation:** Compiler optimization
3. **Map Coloring:** Adjacent regions different colors
4. **Frequency Assignment:** Radio stations

---

### **Edge Coloring:**

**Edge Chromatic Number χ'(G):**
Minimum colors for edges (adjacent edges different colors)

**Vizing's Theorem:**
Δ ≤ χ'(G) ≤ Δ + 1

Where Δ = maximum degree

---

## **IMPORTANT FORMULAS - GRAPH THEORY**

1. **Handshaking:** Σ deg(v) = 2|E|
2. **Complete Graph:** |E| = n(n-1)/2
3. **Tree:** |E| = |V| - 1
4. **Euler's Formula:** V - E + F = 2
5. **Planar:** E ≤ 3V - 6
6. **Chromatic Planar:** χ(G) ≤ 4

---

---

# **SUMMARY OF ALL UNITS**

## **Unit I - Mathematical Logic:**
- Statements, connectives, truth tables
- Tautology, equivalences, normal forms
- Rules of inference, proof methods
- Consistency, contradiction, resolution

## **Unit II - Relations:**
- Sets, relations, properties
- Equivalence, partial order, lattices
- Hasse diagrams, transitive closure
- Functions, semigroups, monoids

## **Unit III - Combinatorics:**
- Counting principles
- Permutations, combinations
- Binomial theorem, multinomial theorem
- Inclusion-exclusion, pigeonhole principle

## **Unit IV - Recurrence Relations:**
- Generating functions
- Solving by substitution, generating functions
- Characteristic roots method
- Homogeneous and non-homogeneous

## **Unit V - Graph Theory:**
- Basic concepts, representations
- Trees, spanning trees (DFS, BFS)
- MST (Prim's, Kruskal's)
- Planar graphs, Euler's formula
- Euler and Hamiltonian graphs
- Graph coloring, chromatic number

---

These comprehensive notes cover all five units with detailed explanations, formulas, examples, and diagrams. Study them systematically and practice problems to master Discrete Mathematics!

---

### 🧑 You

make notes in more detail about all units each and every topic from every unit  provide me answers in detail with required equations,diagrams points and what ever is needed

---
