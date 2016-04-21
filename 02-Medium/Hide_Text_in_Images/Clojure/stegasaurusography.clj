(defn binary-substrings
  [binary]
  (loop [bs binary substring [] ret []]
    (if-let [curr (first bs)]
      (if (or (= curr \0)
              (= curr \1)) (let [new-substring (conj substring curr)]
                             (if (= (count new-substring) 8)
                               (recur (rest bs) [] (conj ret new-substring))
                               (recur (rest bs) new-substring ret)))
        (recur (rest bs) [] ret))
      ret)))

(defn main []
  (let [input (clojure.string/replace (read-line) #" " "")
        binary (take-nth 3 (nthrest input 2))]
    (println (apply str (map #(char (Integer/parseInt (apply str %) 2)) 
                             (binary-substrings binary))))))

(main)
