(define try (lambda (guess x)
    (if (good-enuf?  guess x)
        guess
        (try (improve guess x) x)
    )
))

(define improve (lambda (guess x)(average guess (/ x guess))))

(define good-enuf? (lambda (guess x)(< (abs (- (square guess) x)) 0.001)))

(define sqrt (lambda (x)(try 1 x)))