(DEFINE (SQUARE A)
        (* A A)
)
(DEFINE (SUM-INT A B)
  (IF (> A B)
      0
      (+ (SQUARE A) (SUM-INT (+ A 1) B))))