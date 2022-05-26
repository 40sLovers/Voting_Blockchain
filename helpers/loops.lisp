(setq x 1)

(loop for x from 1 to 10
do (print x))

(loop 
    (format t "~d ~%" x)
    (setq x (+ x 1))
    (when (> x 10) (return x))
)


(loop for x in '(Peter Paul Mary) do
(format t "~s ~%" x))

(loop for y from 100 to 110 do 
(print y))


(dotimes (y 12)
(print y))

