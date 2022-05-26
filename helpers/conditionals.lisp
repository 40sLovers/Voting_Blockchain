(defvar *age* 18)

(if (= *age* 18)
    (format t "you can vote~%")
    (format t "you cant vote~%"))

;not is a function lol
(if (not (= *age* 18))
    (format t "you can vote~%")
    (format t "you cant vote~%"))

;just an example. it will be always false.
(if (and (<= *age* 14) (>= *age* 67))
(format t "Work it if you want ~%")
(format t "Time for work ~%"))

(if (or (<= *age* 14) (>= *age* 67))
(format t "Work it if you want ~%")
(format t "Time for work ~%"))

(defvar *num*  2)
(defvar *num-2* 2)
(defvar *num-3* 2)

(if (= *num* 2)
    (progn 
    (setf *num-2* (* *num-2* 2))
    (setf *num-3* (* *num-3* 3))
    ) 
    (format t "Not equal to 2~%")
)

(format t "*num-2* = ~d~%" *num-2*)
(format t "*num-3* = ~d~%" *num-3*)

;print endline.
(terpri)
(defvar *age* 5)
(defun get-school (age)
    (case age
        (5 (print "Kindergarden"))
        (6 (print "first grade"))
        (otherwise (print "middle school"))))
(get-school *age*)



(setf *age* 18)
(setf *num-3* 5)

;like if with progn
(when (= *age* 18)
    (setf *num-3* 18)
    (format t "Go to college you're ~d ~%" *num-3*)

)

(unless (not (= *age* 18))
    (setf *num-3* 20)
    (format t "something random ~%")

)

(defvar *college-ready* nil)
(cond ( (>= *age* 18) 
        (setf *college-ready* 'yes)
        (format t "you're ready for college ~%"))
    ( (< *age* 18)
        (setf *college-ready* 'no)
        (format t "you're not ready for college ~%"))
    (t (format t "Don't know ~%")))
    