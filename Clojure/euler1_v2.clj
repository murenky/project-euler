(ns euler.core
  (:gen-class))

(defn res [] (+ 
               (reduce + (range 3 1000 3)) 
               (reduce + (filter 
                           (fn [x] (not (= (rem x 3) 0))) 
                           (range 5 1000 5))
                       )
             )
  )

(defn -main [] (print (res)))