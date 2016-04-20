(defn main
  []
  (let [input (clojure.string/split-lines (slurp *in*))
        dict  (into {} (map #(clojure.string/split % #" ") (rest (drop-last input))))
        text  (clojure.string/split (last input) #" ")]
    (println (clojure.string/join " " 
                                  (for [word text]
                                    (get dict word word))))))

(main)
