(defn str->cards [card-str]
  (map #(case %
          "J" 11
          "Q" 12
          "K" 13
          "A" 14
          (Integer/parseInt %))
       (clojure.string/split card-str #" ")))

(defn str->nums [num-str]
  (map #(Integer/parseInt %) (clojure.string/split num-str #" ")))

(defn war
  [p1-deck p2-deck p1-thresholds p2-thresholds war-stack]
  (cond (< (count p1-deck) 3) ['() p2-deck p1-thresholds p2-thresholds]
        (< (count p2-deck) 3) [p1-deck '() p1-thresholds p2-thresholds]
        :else (let [war-stack' (concat war-stack (take 3 p1-deck) (take 3 p2-deck))
                    p1-deck' (concat (nthrest p1-deck 3))
                    p2-deck' (concat (nthrest p2-deck 3))
                    p1-card (first p1-deck')
                    p2-card (first p2-deck')]
                (cond (> p1-card p2-card) [(concat (rest p1-deck') (list p1-card p2-card) war-stack')
                                           (rest p2-deck')
                                           p1-thresholds
                                           p2-thresholds]
                      (< p1-card p2-card) [(rest p1-deck')
                                           (concat (rest p2-deck') (list p2-card p1-card) war-stack')
                                           p1-thresholds
                                           p2-thresholds]
                      :else (war p1-deck' p2-deck' p1-thresholds p2-thresholds war-stack')))))

(defn game
  [p1-deck p2-deck p1-thresholds p2-thresholds]
  (loop [state [p1-deck p2-deck p1-thresholds p2-thresholds]]
    (let [[p1-d p2-d p1-t p2-t] state]
      (if (and (seq p1-d) (seq p2-d))
        (let [p1-card (first p1-d)
              p2-card (first p2-d)]
          (cond
            (> p1-card p2-card) (recur [(concat (rest p1-d) (list p1-card p2-card))
                                        (rest p2-d)
                                        p1-t
                                        p2-t])
            (< p1-card p2-card) (recur [(rest p1-d)
                                        (concat (rest p2-d) (list p2-card p1-card))
                                        p1-t
                                        p2-t])
            :else (recur (war p1-d p2-d p1-t p2-t '()))))
        (if (seq p1-d)
          "Player 1"
          "Player 2")))))

(defn main
  []
  (let [p1-cards (str->cards (read-line))
        p2-cards (str->cards (read-line))
        p1-thresholds (str->nums (read-line))
        p2-thresholds (str->nums (read-line))]
    (println (game p1-cards p2-cards p1-thresholds p2-thresholds))))

(time (main))
