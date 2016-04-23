(defn valid-moves
  [[maze [x y] seeking]]
  (let [up    [x (- y 1)]
        down  [x (+ y 1)]
        left  [(- x 1) y]
        right [(+ x 1) y]] 
    (filter vector? 
            (list (when (or (= (get-in maze up)      \G)
                            (= (get-in maze up)      \ )) [(assoc-in maze [x y] \X) up seeking])
                  (when (or (= (get-in maze down)    \G)
                            (= (get-in maze down)    \ )) [(assoc-in maze [x y] \X) down seeking])
                  (when (or (= (get-in maze left)    \G)
                            (= (get-in maze left)    \ )) [(assoc-in maze [x y] \X) left seeking])
                  (when (or (= (get-in maze right)   \G)
                            (= (get-in maze right)   \ )) [(assoc-in maze [x y] \X) right seeking])
                  (when (and (or (= seeking \E)
                                 (= seeking \A))
                             (= (get-in maze up)    \E)) [(assoc-in maze [x y] \X) up \R])
                  (when (and (or (= seeking \E)
                                 (= seeking \A))
                             (= (get-in maze down)  \E)) [(assoc-in maze [x y] \X) down \R])
                  (when (and (or (= seeking \E)
                                 (= seeking \A))
                             (= (get-in maze left)  \E)) [(assoc-in maze [x y] \X) left \R])
                  (when (and (or (= seeking \E)
                                 (= seeking \A))
                             (= (get-in maze right) \E)) [(assoc-in maze [x y] \X) right \R])
                  (when (and (or (= seeking \R)
                                 (= seeking \A))
                             (= (get-in maze up)    \R)) [(assoc-in maze [x y] \X) up \E])
                  (when (and (or (= seeking \R)
                                 (= seeking \A))
                             (= (get-in maze down)  \R)) [(assoc-in maze [x y] \X) down \E])
                  (when (and (or (= seeking \R)
                                 (= seeking \A))
                             (= (get-in maze left)  \R)) [(assoc-in maze [x y] \X) left \E])
                  (when (and (or (= seeking \R)
                                 (= seeking \A))
                             (= (get-in maze right) \R)) [(assoc-in maze [x y] \X) right \E])))))

(defn bfs
  [orig-maze pos]
  (loop [states (list [orig-maze pos \A])] ; initially seeking \A anything
    (when-let [[maze [x y] seeking :as state] (first states)]
      (if (= (get-in maze [x y]) \G)
        (assoc-in maze [x y] \X)
        (recur (if-let [next-moves (valid-moves state)]
                 (concat (rest states) next-moves)
                 (rest states)))))))

(defn main
  []
  (let [input (clojure.string/split-lines (slurp *in*))
        _     (first input) ; we don't need to record dimensions of the maze
        pos   (map #(Integer/parseInt %) (clojure.string/split (apply str (second input)) #" "))
        maze  (into [] (for [line (drop 2 input)] (into [] (seq line))))]
    (if-let [solution (bfs maze pos)]
      (doseq [row solution]
        (println (apply str row)))
      (println "NO SOLUTION"))))

(main)
