(ns euler.core
  (:gen-class))

(defn divisible? [x] 
  (or (= (rem x 3) 0) (= (rem x 5) 0) false))

(defn -main [] (print (reduce + (filter divisible? (range 1000)))))