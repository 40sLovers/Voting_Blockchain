(cons 'superman 'batman)
(list 'superman 'batman 'flash)
(cons 'aquaman (list 'superman 'batman))

(format t "First = ~a ~%" (car '(superman batman aquaman)))
(format t "Everything else = ~a ~%" (cdr '(superman batman aquaman)))
(format t "2nd item = ~a ~%" (cadr '(superman batman aquaman flash joker)))
(format t "4th item = ~a ~%" (cadddr '(superman batman aquaman flash joker)))

(format t "is it a list = ~a ~%" (listp '(batman superman)))
(format t "is 3 in list = ~a ~%" (if (member 3 '(2 4 6)) 't nil))


;; (append '(just) '(some) '(random words))
(defparameter *nums* '(2 4 6))
(push 1 *nums*)

(format t "2nd Item in a list ~a ~%" (nth 2 *nums*))

(defvar superman (list :name "Superman" :secret-id "Clark Kent"))
(defvar *hero-list* nil)
(push superman *hero-list*)
(dolist (hero *hero-list*)
    (format t "~{~a : ~a ~}~%" hero))

(defparameter *heroes*
    '((superman (Clark Kent))
    (Flash (Barry Allen))
    (Batman (Bruce Wayne))))

(format t "Superman Data ~a ~%" (assoc 'superman *heroes*))
(format t "Superman is ~a ~%" (cadr (assoc 'superman *heroes*)))

(defparameter *hero-size*
    '((superman (6 ft 3 in) (230 lbs))
    (Flash (6 ft 0 in) (190 lbs))
    (Batman (6 ft 2 in) (210 lbs))))

(format t "Superman is ~a ~%" (cadr (assoc 'Superman *hero-size*)))
(format t "Superman is ~a ~%" (caddr (assoc 'Superman *hero-size*)))
