;define variable
(defvar *number* 0)

;set variable
(setf *number* 6)

(format t "(+ 5 4) = ~d ~%" (+ 5 4))
(format t "(- 5 4) = ~d ~%" (- 5 4))
(format t "(* 5 4) = ~d ~%" (* 5 4))
(format t "(/ 5 4) = ~d ~%" (/ 5 4))
(format t "(/ 5 4.0) = ~d ~%" (/ 5 4.0))
(format t "(rem 5 4) = ~d ~%" (rem 5 4))
(format t "(mod 5 4) = ~d ~%" (mod 5 4))