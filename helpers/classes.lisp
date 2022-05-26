(setq *print-case* :capitalize) ; :upcase :downcase

(defclass animal()
(name sound))

(defparameter *dog* (make-instance 'animal))

(setf (slot-value *dog* 'name) "Spot")
(setf (slot-value *dog* 'sound) "Woof")

(format t "~a says ~a ~%" 
(slot-value *dog* 'name) (slot-value *dog* 'sound))


(defclass mammal ()
((name 
:initarg :name
:initform (error "Must provide a name"))
(sound
:initarg :sound
:initform "No sound"
; :reader only get 
; :writer only set
:accessor mammal-sound 
)))


(defparameter *king-kong*
    (make-instance 'mammal :name "King-Kong" :sound "Rawwr"))

(format t "~a says ~a ~%" 
(slot-value *king-kong* 'name) (slot-value *king-kong* 'sound))

(defparameter *Fluffy*
    (make-instance 'mammal :name "Fluffy" :sound "Meow"))

(defgeneric make-sound (mammal))

(defmethod make-sound ((the-mammal mammal))
    (format t "~a says ~a ~%" 
    (slot-value the-mammal 'name) 
    (slot-value the-mammal 'sound))
)

(make-sound *king-kong*)
(make-sound *Fluffy*)


(defgeneric (setf mammal-name) (value the-mammal))

(defmethod (setf mammal-name) (value(the-mammal mammal))
(setf (slot-value the-mammal 'name) value))

(defgeneric mammal-name (the-mammal))
(defmethod mammal-name ((the-mammal mammal))
    (slot-value the-mammal 'name))


(setf (mammal-name *king-kong*) "Kong")
(format t "I am ~a ! ~%" (mammal-name *king-kong*))

;declared with accesor in class.
(setf (mammal-sound *king-kong*) "Otelu e viata mea" )
;; (format t "Said ~a ! ~%" (mammal-sound *king-kong*))
(make-sound *king-kong*)

(defclass dog (mammal) ())
(defparameter *rover*
(make-instance 'dog :name "Rover" :sound "woof"))

(make-sound *rover*)




