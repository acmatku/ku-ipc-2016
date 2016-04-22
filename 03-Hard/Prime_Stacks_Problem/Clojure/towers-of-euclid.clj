(defn sieve [s]
  (cons (first s)
        (lazy-seq (sieve (filter #(not= 0 (mod % (first s)))
                                 (rest s))))))

(def prime-set
  (into #{} (take-while #(> 1000 %) (sieve (iterate inc 2)))))

(defn prime?
  [x]
  (contains? prime-set x))

(defn row-number
  [[h t o]]
  (+ (* 100 h) (* 10 t) o))

(defn goal?
  [[stack1 stack2 stack3]]
  (and (= (count stack1) (count stack2) (count stack3))
       (every? prime? (map row-number (map vector stack1 stack2 stack3)))))

(defn moves
  [[stack1 stack2 stack3]]
  (filterv list? [(when (seq stack1) (list (rest stack1)
                                           (cons (first stack1) stack2)
                                           stack3))
                  (when (seq stack1) (list (rest stack1)
                                           stack2
                                           (cons (first stack1) stack3)))
                  (when (seq stack2) (list (cons (first stack2) stack1)
                                           (rest stack2)
                                           stack3))
                  (when (seq stack2) (list stack1
                                           (rest stack2)
                                           (cons (first stack2) stack3)))
                  (when (seq stack3) (list (cons (first stack3) stack1)
                                           stack2
                                           (rest stack3)))
                  (when (seq stack3) (list stack1
                                           (cons (first stack3) stack2)
                                           (rest stack3)))]))

(defn bfs
  [stack1 stack2 stack3]
  (loop [frontier [[stack1 stack2 stack3]] path [[stack1 stack2 stack3]]]
    (when-let [curr-state (first frontier)]
      (if (goal? curr-state)
        curr-state
        (recur (concat (rest frontier) (moves curr-state)) (conj path curr-state))))))

(defn main []
  (let [stack1 (reverse (map #(Integer/parseInt %) (clojure.string/split (read-line) #" ")))
        stack2 (reverse (map #(Integer/parseInt %) (clojure.string/split (read-line) #" ")))
        stack3 '()]
    (doseq [stack (map reverse (bfs stack1 stack2 stack3))]
      (println (clojure.string/join " " stack)))))

(main)
