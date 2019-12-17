(define square (lambda(x) (* x x)))
(define pythagoras
  (lambda (x y)
  (
    sqrt (+ (square x)(square y))
  ))
)