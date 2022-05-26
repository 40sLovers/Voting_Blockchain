;;;; Describe program
;;;convention...
;;; comments
;; indented cooment
; comment after one line of code 

#||
Multiline 
comments
||#

; ~% endline
;prints hello world
(format t "Hello world ~%")

; also print
(print "what's your name?")
; global variables with *name_of_variable* -- convention.
(defvar *name* (read))

(defun hello-you (name)
    (format t "Hello ~a! ~%" name))

(setq *print-case* :capitalize) ; :upcase :downcase

(hello-you *name*)