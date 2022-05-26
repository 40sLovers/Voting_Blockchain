(setq *print-case* :capitalize) ; :upcase :downcase


(defun hello()
    (print "hello")
    (terpri))
;; (hello)

(defun get-avg (num-1 num-2)
    (/ (+ num-1 num-2) 2))

(format t "Avg 10 & 50 = ~a ~%" (get-avg 10 50 ))

(defun print-list (w x &optional y z)
    (format t "List = ~a ~%" (list w x y z)))

(print-list 1 2 3)

(defvar *total* 0)

(defun sum (&rest nums)
    (dolist (num nums)
        (setf *total* (+ *total* num))
    )
    (format t "Sum = ~a ~%" *total*)
)
(sum 1 2 3 4 5 6 7)

(defun print-list(&optional &key x y z)
(format t "List: ~a ~%" (list x y z))
)


(print-list :x  1 :y 2)


(defun difference (num1 num2)
    (return-from difference(- num1 num2)))

(format t "10 - 2 = ~a ~%" (difference 10 2))

(defparameter *hero-size*
    '((superman (6 ft 3 in) (230 lbs))
    (Flash (6 ft 0 in) (190 lbs))
    (Batman (6 ft 2 in) (210 lbs))))


(defun get-hero-data (size)
    (format t "~a ~%"
    `(,(caar size) is , (cadar size) and , (caddar size))))

(get-hero-data *hero-size*)

; lol js map in lisp
(format t "A number ~a ~%" (mapcar #'numberp '(1 2 3 f g)))

;; (flet ((func-name (arguments)
;;     function Body))
;;     body))


;local scope functions
(flet ((double-it (num)
    (* num 2))
    (triple-it (num) 
    (* num 3))
    )

    (format t "Double 10 = ~d ~%" (double-it 10 )) 
    (format t "Double & triple 10 = ~d ~%" (triple-it(double-it 10 ))) 
)

;call function into another function
(labels ((double-it (num)
    (* num 2))
    (six-it (num)
     (* (double-it num) 3)))
     (format t " Six-it 2 = ~d~%" (six-it 2)))





;destructing array stuffs
(defun squares (num)
    (values (expt num 2) (expt num 3)))

(multiple-value-bind (a b) (squares 2)
    (format t "2^2 = ~d and 2^3 = ~d ~%" a b))



; higher order functions
(defun times-3 (x) (* 3 x))
(defun times-4 (x) (* 4 x))

(defun multiples (mult-func max-num)
    (dotimes (x max-num)
    (format t "~d : ~d ~%" x (funcall mult-func x))))
(multiples #'times-3 10)
(multiples #'times-4 10)


;lambdas
(mapcar (lambda (x) (print (* x 2))) '(1 2 3 4 5))


