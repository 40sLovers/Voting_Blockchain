(defvar *num* 2)
(defvar *num-2* 0)


(defmacro ifit (condition &rest body)
    `(if, condition (progn ,@body) (format t "Can't Drive ~%")
))

(setf *age* 16)
(ifit (>= *age* 16)
    (print "You are over 16")
    (print "Time to drive")
    (terpri)
)


(defun add (num1 num2)
    (let  ((sum (+ num1 num2)))
    (format t "~a + ~a = ~a ~%" num1 num2 sum)))

(defmacro letx (var val &rest body)
    `(let ((,var , val)) ,@body))


(defun substract (num1 num2)
    (letx dif (- num1 num2)
    (format t "~a - ~a = ~a ~%" num1 num2 dif)))

(add 10 6)
(substract 10 6)