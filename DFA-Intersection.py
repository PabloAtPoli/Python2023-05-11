sigma = ["a", "b"]

Q1 = ["q1", "q3"]
F1 = ["q1"]
delta1 = [
    ["q3", "q1"],
    ["q1", "q3"]
]

Q2 = ["q2", "q4"]
F2 = ["q2"]
delta2 = [
    ["q2", "q4"],
    ["q4", "q2"]
]

def intersection_DFA1_and_DFA2(sigma, Q1, q1, F1, delta1, Q2, q2, F2, delta2):
    Q = []
    F = []
    delta = []
    q1_q2 = q1 + q2
    for qi in Q1:
        for qj in Q2:
            Q.append(qi + qj)
            if qi in F1 and qj in F2:
                F.append(qi + qj)
            row = []
            for a in sigma:
                row.append(delta1[Q1.index(qi)][sigma.index(a)] + delta2[Q2.index(qj)][sigma.index(a)])    
            delta.append(row)
    return sigma, Q, q1_q2, F, delta

def print_DFA(sigma, Q, q1_q2, F, delta):
    print("sigma: ", sigma)
    print("Q: ", Q)
    print("q1_q2: ", q1_q2)
    print("F: ", F)
    for q in Q:
        for a in sigma:
            print("delta(", q, ",", a, "): ", delta[Q.index(q)][sigma.index(a)])

sigma, Q, q1_q2,F, delta = intersection_DFA1_and_DFA2(sigma, Q1,"q1", F1, delta1, Q2,"q2", F2, delta2)

print("DFA intersection: ")
print_DFA(sigma, Q, q1_q2, F, delta)
print(delta)



