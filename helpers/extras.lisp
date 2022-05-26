(setq *print-case* :capitalize) ; :upcase :downcase


(defparameter names (make-array 3))

(setf (aref names 1) 'Bob)

(format t "~a ~%" (aref names 1))


(setf num-array (make-array '(3 3)
    :initial-contents '((0 1 2)(3 4 5)(6 7 8))))

;; (dotimes (x 3)
;; (dotimes (y 3)
;;     (print(aref num-array x y))))


(defparameter people (make-hash-table))


(setf (gethash '102 people) '(Paul Smith))
(setf (gethash '103 people) '(Sam Smith))
(setf (gethash '107 people) '(John Smith))

(format t "~a ~%" (gethash '102 people))


(maphash #'(lambda (k v) (format t "~a = ~a ~%" k v )) people)

(remhash '103 people)
(terpri)
(maphash #'(lambda (k v) (format t "~a = ~a ~%" k v )) people)


(defstruct customer name address id)
(setq paulsmith (make-customer :name "Paul Smith" :address "123 Main"
 :id 1000))

(format t "~a ~%" (customer-name paulsmith))

(setf (customer-address paulsmith) "125 main")
(write paulsmith)
(terpri)
 (setq sally-smith-1001 (make-customer
 :name "Sally Smith" :address "126 Main" :id 1001))

(write sally-smith-1001)
(terpri)


(with-open-file (my-stream 
"test.txt"
:direction :output
:if-exists :supersede)
(princ "Some Random text" my-stream))

(let ((in (open "test.txt" :if-does-not-exist nil)))
(when in
    (loop for line = (read-line in nil)
    while line do (format t "~a~%" line))
    (close in)
    ))
