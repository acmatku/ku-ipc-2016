(defn add-to-house
  [hs k n]
  (assoc hs k (conj (get hs k) (apply str n))))

(defn main
  []
  (let [input (clojure.string/split (slurp *in*) #"\n")
        entries (map (fn [line] [(first line) (drop 2 line)]) (rest input))
        houses (sorted-map "Gryffindor" (sorted-set)
                           "Hufflepuff" (sorted-set)
                           "Ravenclaw"  (sorted-set)
                           "Slytherin"  (sorted-set))]
    (doseq [[house name-set] (reduce (fn [hs [h n]] 
                                       (case h
                                         \G (add-to-house hs "Gryffindor" n)
                                         \H (add-to-house hs "Hufflepuff" n)  
                                         \R (add-to-house hs "Ravenclaw"  n)
                                         \S (add-to-house hs "Slytherin"  n))) 
                                     houses entries)]
      (println (str house ":"))
      (doseq [name name-set]
        (println name)))))

(main)
