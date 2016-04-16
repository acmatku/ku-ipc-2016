(defn place [piles card]
  (let [[les gts] (->> piles (split-with #(<= (ffirst %) card)))
        newelem (cons card (->> les last first))
        modpile (cons newelem (first gts))]
    (concat les (cons modpile (rest gts)))))

(defn longest [cards]
  (let [piles (reduce place '() cards)]
    (->> piles last first count)))

(defn main
  "An efficient O(n log n) solution to the Longest Increasing Subsequence problem using
  Patience Sort"
  []
  (let [left  (into [] (map #(Integer/parseInt %) (clojure.string/split (read-line) #" ")))
        right (into [] (map #(Integer/parseInt %) (clojure.string/split (read-line) #" ")))
        x-of-is (map first (sort-by second (map vector left right)))] ; index of left's ally
    (println (longest x-of-is))))

(time (main))
