(defn str->cards [card-str]
  (map #(case %
          "T" 10
          "J" 11
          "Q" 12
          "K" 13
          "A" 14
          (Integer/parseInt %))
       (clojure.string/split card-str #" ")))

(defn str->nums [num-str]
  (map #(Integer/parseInt %) (clojure.string/split num-str #" ")))

(defn war
  [p1-deck p2-deck war-stack]
  (cond (< (count p1-deck) 4) ['() (concat p2-deck p1-deck war-stack)]
        (< (count p2-deck) 4) [(concat p1-deck p2-deck war-stack) '()]
        :else (let [war-stack' (concat war-stack (take 3 p1-deck) (take 3 p2-deck))
                    p1-deck' (nthrest p1-deck 3)
                    p2-deck' (nthrest p2-deck 3)
                    p1-card (first p1-deck')
                    p2-card (first p2-deck')]
                (cond (> p1-card p2-card) [(concat (rest p1-deck') (list p1-card p2-card) war-stack')
                                           (rest p2-deck')]
                      (< p1-card p2-card) [(rest p1-deck')
                                           (concat (rest p2-deck') (list p2-card p1-card) war-stack')]
                      :else (war (rest p1-deck') (rest p2-deck') (concat (list p1-card p2-card) war-stack'))))))

(defn game
  [p1-deck p2-deck]
  (loop [state [p1-deck p2-deck]]
    (let [[p1-d p2-d] state]
      (if (and (seq p1-d) (seq p2-d))
        (let [p1-card (first p1-d)
              p2-card (first p2-d)]
          (cond
            (> p1-card p2-card) (recur [(concat (rest p1-d) (list p1-card p2-card))
                                        (rest p2-d)])
            (< p1-card p2-card) (recur [(rest p1-d)
                                        (concat (rest p2-d) (list p2-card p1-card))])
            :else (recur (war (rest p1-d) (rest p2-d) (list p1-card p2-card)))))
        (if (seq p1-d)
          "PLAYER 1"
          "PLAYER 2")))))

(defn main
  []
  (let [p1-cards (str->cards (read-line))
        p2-cards (str->cards (read-line))]
    (println (game p1-cards p2-cards))))

(main)
