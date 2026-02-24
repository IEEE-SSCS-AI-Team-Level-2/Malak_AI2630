# What does Gamma function even mean or represent ?
gamma function is considered the factorial of the non-integer numbers, since we can simply calculate the factorial of the integer numbers by just using the formula
           
           n! = n*(n-1)*(n-2)*...*1
           
we use the Gamma function to calculate the factorial of the non integer numbers, which is represented as

            Γ(z)= 0∫∞ ​t^(z−1) e^(−t) dt for Re(z)>0


# But what about it's rule in probability ?
- The gamma function could be used for representing the normalization constants in distributions like chi square

  ## and Gamma function could be used to calculate waiting time between certain events
  - let T1,T2,T3,... are events that happens in specific times, λ is the rate, and w1,w2,w3,... is the waiting time between each two successive events
    we can conclude that (Tr is waiting time for the rth event)

        Tr = w1 + w2 + w3 + ...
        Tr ≈ gamma(r,λ)
