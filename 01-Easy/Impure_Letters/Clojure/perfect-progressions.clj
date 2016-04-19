(defn count-perfection
  [string]
  (loop [s string c 0 l [\I \P \C]]
    (if (seq s) 
      (case (first l) 
        \I (if (= (first s) \I)
             (recur (rest s) c (rest l))
             (recur (rest s) c l))
        \P (if (= (first s) \P)
             (recur (rest s) c (rest l))
             (recur (rest s) (+ c 1) l))
        \C (if (= (first s) \C)
             c
             (recur (rest s) (+ c 1) l)))
      "INVALID")))

(defn main
  []
  (read-line) ; disregard first number
  (doseq [string (line-seq (java.io.BufferedReader. *in*))]
    (println (count-perfection string))))

(main)
