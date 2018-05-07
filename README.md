# theorem-prover

Python3.5 implementation for the method of analytic tableaux. @ OPAT - UDESC

##### Examples
> 1. p -> q, q -> r |= p -> r
> 2. p, (p ^ q) -> r |= r
> 3. (p v ¬p) is true
> 4. p -> q |= ¬p v q
> 5. ¬p v q, ¬q v r |= ¬p v r
> 6. p v q, p -> r, q -> (r v s) |= r
> 7. (p -> (q -> r)) -> ((p -> q) -> (p -> r)) is true
