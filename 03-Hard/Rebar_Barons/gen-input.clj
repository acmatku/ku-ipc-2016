(defn main
  []
  (let [left  (range 1 (+ 1 (Math/pow 10 (Integer/parseInt (first *command-line-args*)))))
        right (shuffle left)]
    (spit (second *command-line-args*)
          (str (clojure.string/join " " left)
               "\n"
               (clojure.string/join " " right)
               "\n"))))

(main)
